import requests
from threading import Thread
from time import sleep

actualVersionAdress     = "http://lvfn4k-lab.h1n.ru/ZTK/ExFilter/actual_version.txt"
updateArchive           = "http://lvfn4k-lab.h1n.ru/ZTK/ExFilter/update.zip"
Thread0_Data            = []

def Thread0_Action():
    i = 0
    while i <= 5:
        Thread0_Data.append("Hello!")
        i += 1
        sleep(1)

Thread0 = Thread(target=Thread0_Action)

def CheckInternet(url='http://yandex.ru'):
    for timeout in [1, 5, 10, 15]:
        try:
            requests.get(url, timeout=timeout)
            return True
        except Exception as mess:
            print(mess)
            return False

def CheckServer():
    return CheckInternet(actualVersionAdress)

def CheckUpdates():
    return requests.get(actualVersionAdress).text

def StartThread():
    Thread0.start()
