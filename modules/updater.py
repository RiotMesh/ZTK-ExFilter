import urllib

actualVersionAdress = "http://lvfn4k-lab.h1n.ru/ZTK/ExFilter/actual_version.txt"
updateArchive = "http://lvfn4k-lab.h1n.ru/ZTK/ExFilter/update.zip"

def CheckInternetConnection():

    try:
        urllib.urlopen(actualVersionAdress)
        return True
    except IOError:
        return False

def IsNeedUpdate():
    
    print(urllib.urlopen(actualVersionAdress))