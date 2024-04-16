import scipy.io.wavfile as wav
import numpy as np
import faker
import os

class StegoNotFoundException(Exception):
    def __init__(self, *args, filename) -> None:
        super().__init__(*args)
        self.filename = filename

    def __str__(self) -> str:
        return "Стеганография в файле {} не найдена".format(self.filename)

def dataToBitStream(data: str):
    return "".join(bin(byte)[2:].zfill(8) for byte in data.encode())

def bitStreamToData(bitStream: str):
    result = []
    for i in range(0, len(bitStream), 8):
        result.append(bitStream[i: i+8])
        
    return bytes(result)

def extractDataFromWav(wavFilePath: str, lsb_value: int = 1):
    # ===================== Проверка наличия файла
    if not os.path.exists(wavFilePath):
        raise FileExistsError(f"Файл по пути {wavFilePath} не найден")

    # ===================== Сбор данных с аудиофайла
    sample_rate, npWavData = wav.read(wavFilePath)
    
    if len(npWavData.shape) == 2:
        wavData = [couple[0] for couple in npWavData]
    else:
        wavData = npWavData.tolist()
    
    # ===================== Извлечение данных из аудиофайла
    bitStream = ""
    for byte in wavData:
        bitStream += bin(byte)[2:].zfill(16)[-lsb_value:]

    data = []
    for i in range(0, len(bitStream), 8):
        data.append(int(bitStream[i:i+8], 2))
        if bytes(data[-8:]) == b"!HIMERA!":
            data = data[:-8]
            break
    else:
        raise StegoNotFoundException(filename=wavFilePath.split('/')[-1])

    return bytes(data).decode('utf-8')
    
def embedDataToWav(wavFilePath: str, data: str | bytes, lsb_value: int = 1):
    # ===================== Проверка наличия файла
    if not os.path.exists(wavFilePath):
        raise FileExistsError(f"Файл по пути {wavFilePath} не найден")
    
    # ===================== Представление текста в виде битов (Пример: 110101011010010011)
    data = data if isinstance(data, str) else data.decode('utf-8')
    data += "!HIMERA!"
    bitStreamData = dataToBitStream(data) 
    
    # ===================== Сбор данных с аудиофайла
    sample_rate, npWavData = wav.read(wavFilePath)
    
    if len(npWavData.shape) == 2:
        wavData = [couple[0] for couple in npWavData]
    else:
        wavData = npWavData.tolist()
        
    # ===================== Внесение данных в аудиофайл
    if len(wavData) < len(bitStreamData) // lsb_value:
        return None

    newWavData = []
    for wavByte, lsbBit in zip(wavData[:len(bitStreamData) // lsb_value], 
                                bitStreamData):
        newWavByte = (wavByte >> lsb_value << lsb_value) | int(lsbBit)
        newWavData.append(newWavByte)
    
    # ===================== Формирование новых данных
    newWavData = newWavData + wavData[len(bitStreamData) // lsb_value:]
    
    if len(npWavData.shape) == 2:
        newNpWavData = np.array([(a, b) for a, b in zip(newWavData, [couple[1] for couple in npWavData])], np.int16)
    else:
        newNpWavData = np.array(newWavData, np.int16)
    
    return (sample_rate, newNpWavData)

if __name__ == "__main__":
    # fake = faker.Faker()
    
    # data = "Это мой текст"
    data = "This is text"
    
    embedDataToWav("../dataset/1Channel.wav", data, "../dataset-stego/1Channel-stego.wav", 1)
    extractedData = extractDataFromWav("../dataset-stego/1Channel-stego.wav", 1)
    
    print(f"{data=}")
    print(f"{extractedData=}")
    print(f"{extractedData==data}")
    
    # bitStream = dataToBitStream(data)
    # dataFromBitStream = bitStreamToData(bitStream)
    
    # print(f"{data=}") 
    # print(f"{bitStream=}") 
    # print(f"{dataFromBitStream=}") 