import sys
import os
import numpy as np
import scipy.io.wavfile as wav

from PIL import Image

from src.himera_src import embedDataToWav, extractDataFromWav, StegoNotFoundException
from GUI.HimeraMain import Ui_MainWindow
from GUI.Resources.setup import setup_res

from PySide6.QtCore import QObject, Qt, QDir, QThread, Signal, QMutex, QMetaObject, Q_ARG
from PySide6.QtGui import QMouseEvent, QPixmap, QIcon, QFontDatabase, QTextOption, QPalette, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QFileDialog, QMessageBox, QLabel, QProgressBar

class EmbedThread(QThread):
    progressChange = Signal(str, str, QProgressBar)
    
    def __init__(self, mainWindow) -> None:
        super(EmbedThread, self).__init__(None)
        self.mainWindow: HIMERA = mainWindow
        self.mutex = QMutex()
        
    def run(self):
        self.mutex.lock()
        self.progressChange.emit("rgba(115,81,132,150)", "Процесс запущен...", self.mainWindow.ui.progress_embed)
        self.mutex.unlock()

        self.mainWindow.stegoFileData = embedDataToWav(self.mainWindow.filePathToEmbed, self.mainWindow.ui.text_embed.toPlainText())
        self.mutex.lock()
        self.progressChange.emit("rgba(102,0,153,150)", "Процесс завершён!!!", self.mainWindow.ui.progress_embed)
        self.mutex.unlock()
            
        
        
class ExtractThread(QThread):
    errorSignal = Signal(str)
    
    def __init__(self, mainWindow) -> None:
        super(ExtractThread, self).__init__(None)
        self.mainWindow: HIMERA = mainWindow
        self.mutex = QMutex()
        
    def run(self):
        try:
            data = extractDataFromWav(self.mainWindow.filePathToExtract)
            self.mutex.lock()
            self.mainWindow.ui.label.setText(data)
            self.mutex.unlock()
        except StegoNotFoundException:
            self.errorSignal.emit("Стеганография в данном аудиофайле не найдена")

class HIMERA(QMainWindow):
    def __init__(self) -> None:
        super(HIMERA, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        setup_res()
        
        QFontDatabase.addApplicationFont("./Resources/Fonts/Nozhik.ttf")
        
        self.filePathToEmbed = ""
        self.filePathToExtract = ""
        self.stegoFileData: tuple[int, np.ndarray[np.int16]] = None

        self.embedThread = EmbedThread(self)
        self.extractThread = ExtractThread(self)
        self.embedThread.progressChange.connect(self.__progressBarChange)
        self.extractThread.errorSignal.connect(self.__show_massage_box)
        
        self.ui.button_embed_add.clicked.connect(self.__addAudioFileToEmbed)
        self.ui.button_embed.clicked.connect(self.__embedDataToAudio)
        self.ui.button_save.clicked.connect(self.__saveFile)

        self.ui.button_extract_add.clicked.connect(self.__addAudioFileToExtract)
        self.ui.button_extract.clicked.connect(self.__extractDataFromAudio)
      
    
    def __saveFile(self):
        if not any(self.stegoFileData):
            self.__show_massage_box("Нет данных для сохранения")
            return None
        
        try:
            fileDialog = QFileDialog()
            fileDialog.setFilter(QDir.Filter.Dirs)
            saveFilePath = fileDialog.getSaveFileName(self,
                                                        "Выберите путь для сохранения аудиофайла",
                                                        f"./{self.ui.label_audio_embed.text().split('.')[0]}-stego",
                                                        "Audio (*.wav)")[0]
            wav.write(saveFilePath, self.stegoFileData[0], self.stegoFileData[1])
        except:
            return None
    
    def __addAudioFileToExtract(self):
        try:
            fileDialog = QFileDialog()
            fileDialog.setFilter(QDir.Filter.Files)
            self.filePathToExtract = fileDialog.getOpenFileName(self,
                                                                "Выберите аудиофайл для извлечения данных",
                                                                "./",
                                                                "Audio (*.wav)")[0]
            self.ui.label_audio_extract.setText(self.filePathToExtract.split("/")[-1])
        except:
            return None
        
    def __addAudioFileToEmbed(self):
        try:
            fileDialog = QFileDialog()
            fileDialog.setFilter(QDir.Filter.Files)
            self.filePathToEmbed = fileDialog.getOpenFileName(self,
                                                                "Выберите аудиофайл для внедрения данных",
                                                                "./",
                                                                "Audio (*.wav)")[0]
            self.ui.label_audio_embed.setText(self.filePathToEmbed.split("/")[-1])
        except:
            return None
    
    def __extractDataFromAudio(self):
        if not os.path.exists(self.filePathToExtract):
            self.__show_massage_box("Файл для внедрения данных не найден")
            return None
        
        try: 
            self.extractThread.start()
        except:
            self.__show_massage_box("Произошла ошибка.\nНам очень жаль Вас :(")
        
    def __embedDataToAudio(self):
        if not os.path.exists(self.filePathToEmbed):
            self.__show_massage_box("Файл для внедрения данных не найден")
            return None
        
        if self.ui.text_embed.toPlainText() == "":
            self.__show_massage_box("Введите какой-либо текст")
            return None

        try: 
            self.embedThread.start()
        except:
            self.__show_massage_box("Произошла ошибка.\nВозможно, размера аудиофайла недостаточно для внедрения ваших данных")
            
    def __progressBarChange(self, color: str, format: str, progressBar: QProgressBar):
        progressBar.setStyleSheet("QProgressBar::chunk{"
                                  f"    background-color: {color};"
                                  "}")
        progressBar.setFormat(format)
        progressBar.setValue(100)
            
    def __show_massage_box(self, message):
        message_box = QMessageBox(self)
        message_box.setText(message)
        message_box.setStyleSheet("background-color: white;\
                                    color: black;\
                                    font-family: none;")
        message_box.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HIMERA()
    
    window.setWindowTitle("HIMERA")
    window.setFixedSize(window.width(), window.height())
    
    window.show()
    
    sys.exit(app.exec())