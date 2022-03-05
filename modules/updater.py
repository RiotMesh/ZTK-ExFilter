import requests, urllib3

actualVersionAdress     = "http://lvfn4k-lab.h1n.ru/ZTK/ExFilter/actual_version.txt"
updateArchive           = "http://lvfn4k-lab.h1n.ru/ZTK/ExFilter/update.zip"

def CheckInternet(url='http://yandex.ru'):
    for timeout in [1, 5, 10, 15]:
        try:
            urllib3.urlopen(url, timeout=timeout)
            return True
        except Exception as mess:
            print(mess)
            return False

def CheckServer():
    return CheckInternet(actualVersionAdress)

def CheckUpdates():
    return requests.get(actualVersionAdress).text
