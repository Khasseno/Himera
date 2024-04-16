# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HIMERA.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"HIMERA")
        MainWindow.resize(586, 539)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(30,0,60,1), stop: 1 rgba(0,0,0,1));\n"
"font-family: Nozhik;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label_welcome = QLabel(self.centralwidget)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setGeometry(QRect(100, 50, 401, 41))
        self.label_welcome.setStyleSheet(u"background-color: none;\n"
"color: white;\n"
"font-size: 55px;\n"
"\n"
"")
        self.progress_embed = QProgressBar(self.centralwidget)
        self.progress_embed.setObjectName(u"progress_embed")
        self.progress_embed.setGeometry(QRect(40, 435, 211, 31))
        self.progress_embed.setStyleSheet(u"QProgressBar::chunk{\n"
"	background-color: rgba(115,81,132,150);\n"
"}")
        self.progress_embed.setValue(100)
        self.progress_embed.setAlignment(Qt.AlignCenter)
        self.button_embed_add = QPushButton(self.centralwidget)
        self.button_embed_add.setObjectName(u"button_embed_add")
        self.button_embed_add.setGeometry(QRect(40, 190, 211, 31))
        self.button_embed_add.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 18px;")
        self.button_embed = QPushButton(self.centralwidget)
        self.button_embed.setObjectName(u"button_embed")
        self.button_embed.setGeometry(QRect(40, 395, 211, 31))
        self.button_embed.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 18px;")
        self.button_save = QPushButton(self.centralwidget)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(40, 480, 211, 31))
        self.button_save.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 18px;")
        self.text_embed = QPlainTextEdit(self.centralwidget)
        self.text_embed.setObjectName(u"text_embed")
        self.text_embed.setGeometry(QRect(40, 280, 211, 101))
        self.text_embed.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"font-family: Times New Roman;\n"
"color: white;\n"
"font-size: 14px;")
        self.label_audio_embed = QLabel(self.centralwidget)
        self.label_audio_embed.setObjectName(u"label_audio_embed")
        self.label_audio_embed.setGeometry(QRect(40, 230, 211, 31))
        self.label_audio_embed.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"font-family: Times New Roman;\n"
"color: rgba(255,255,255,190);\n"
"")
        self.label_audio_embed.setAlignment(Qt.AlignCenter)
        self.label_embed = QLabel(self.centralwidget)
        self.label_embed.setObjectName(u"label_embed")
        self.label_embed.setGeometry(QRect(90, 140, 111, 31))
        self.label_embed.setStyleSheet(u"background-color: none;\n"
"color: rgba(255,255,255,190);\n"
"font-size: 38px;\n"
"\n"
"")
        self.label_extract = QLabel(self.centralwidget)
        self.label_extract.setObjectName(u"label_extract")
        self.label_extract.setGeometry(QRect(390, 140, 121, 31))
        self.label_extract.setStyleSheet(u"background-color: none;\n"
"color: rgba(255,255,255,190);\n"
"font-size: 38px;\n"
"\n"
"")
        self.button_extract_add = QPushButton(self.centralwidget)
        self.button_extract_add.setObjectName(u"button_extract_add")
        self.button_extract_add.setGeometry(QRect(340, 190, 211, 31))
        self.button_extract_add.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 18px;")
        self.label_audio_extract = QLabel(self.centralwidget)
        self.label_audio_extract.setObjectName(u"label_audio_extract")
        self.label_audio_extract.setGeometry(QRect(340, 230, 211, 31))
        self.label_audio_extract.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"font-family: Times New Roman;\n"
"color: rgba(255,255,255,190);\n"
"")
        self.label_audio_extract.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 320, 211, 191))
        self.label.setStyleSheet(u"background-color: rgba(255,255,255,40);\n"
"border: 1px solid rgba(255,255,255,60);\n"
"font-family: Times New Roman;\n"
"color: white;\n"
"font-size: 14px;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.button_extract = QPushButton(self.centralwidget)
        self.button_extract.setObjectName(u"button_extract")
        self.button_extract.setGeometry(QRect(340, 280, 211, 31))
        self.button_extract.setStyleSheet(u"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-size: 18px;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0410\u0421 \u041f\u0420\u0418\u0412\u0415\u0422\u0421\u0422\u0412\u0423\u0415\u0422 HIMERA!", None))
        self.progress_embed.setFormat(QCoreApplication.translate("MainWindow", " ", None))
        self.button_embed_add.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c \u0410\u0423\u0414\u0418\u041e", None))
        self.button_embed.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041d\u0415\u0414\u0420\u0418\u0422\u042c", None))
        self.button_save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u041e\u0425\u0420\u0410\u041d\u0418\u0422\u042c", None))
        self.text_embed.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0432\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u044f", None))
        self.label_audio_embed.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0435 \u0430\u0443\u0434\u0438\u043e", None))
        self.label_embed.setText(QCoreApplication.translate("MainWindow", u"\u0412\u041d\u0415\u0414\u0420\u0415\u041d\u0418\u0415", None))
        self.label_extract.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0417\u0412\u041b\u0415\u0427\u0415\u041d\u0418\u0415", None))
        self.button_extract_add.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0410\u0413\u0420\u0423\u0417\u0418\u0422\u042c \u0410\u0423\u0414\u0418\u041e", None))
        self.label_audio_extract.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0433\u0440\u0443\u0436\u0435\u043d\u043d\u043e\u0435 \u0430\u0443\u0434\u0438\u043e", None))
        self.label.setText("")
        self.button_extract.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0417\u0412\u041b\u0415\u0427\u042c", None))
    # retranslateUi

