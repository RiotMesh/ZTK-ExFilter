from colorama import init as initColorama
from colorama import Fore, Back, Style
from lib.custom_input import *
from lib.messager import Message
import pandas as pd

### --------------------------------------------- ###

initColorama()

_APPNAME_   = Fore.CYAN + "ZTK.BaseSep"
_APPVER_    = Fore.LIGHTBLACK_EX + "v0.1"
_DEVELOPER_ = Fore.GREEN + "RiotMesh"

### --------------------------------------------- ###

print("[ " + _APPNAME_ + " " + _APPVER_ + " - by " + _DEVELOPER_ + Style.RESET_ALL + " ]")

excelFilePath = input_("Имя Excel файла или путь к нему: ")

### --------------------------------------------- ### TEMPLATE: CALCULATE DIAPASONS

doc = pd.read_excel(excelFilePath, index_col='n Тел Д', usecols=[0])
print(Fore.LIGHTBLACK_EX + "Выполняются подсчёты ...")

totalD0 = 0
for number in doc.index:
    if number >= 640000 and number <= 649999:
        totalD0 += 1
print(Fore.LIGHTBLUE_EX + "Диапазон 0 (3640000 - 3649999): " + Style.RESET_ALL + str(totalD0))

totalD1 = 0
for number in doc.index:
    if number >= 691000 and number <= 691099:
        totalD1 += 1
print(Fore.LIGHTBLUE_EX + "Диапазон 1 (3691000 - 3691099): " + Style.RESET_ALL + str(totalD1))

totalD2 = 0
for number in doc.index:
    if number >= 691800 and number <= 692099:
        totalD2 += 1
print(Fore.LIGHTBLUE_EX + "Диапазон 2 (3691800 - 3692099): " + Style.RESET_ALL + str(totalD2))

totalD3 = 0
for number in doc.index:
    if number >= 692800 and number <= 692999:
        totalD3 += 1
print(Fore.LIGHTBLUE_EX + "Диапазон 3 (3692800 - 3692999): " + Style.RESET_ALL + str(totalD3))

totalD4 = 0
for number in doc.index:
    if number >= 699000 and number <= 699199:
        totalD4 += 1
print(Fore.LIGHTBLUE_EX + "Диапазон 4 (3699000 - 3699199): " + Style.RESET_ALL + str(totalD4))

totalD5 = 0
for number in doc.index:
    if number >= 699600 and number <= 699799:
        totalD5 += 1
print(Fore.LIGHTBLUE_EX + "Диапазон 5 (3699600 - 3699799): " + Style.RESET_ALL + str(totalD5))

totalNums = totalD0 + totalD1 + totalD2 + totalD3 + totalD4 + totalD5
print(Fore.LIGHTGREEN_EX + "Всего номеров: " + Style.RESET_ALL + str(totalNums))

input_("Нажмите любую клавишу чтобы выйти...")
