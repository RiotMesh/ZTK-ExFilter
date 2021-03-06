from colorama import init as initColorama
from colorama import Fore, Back, Style
from numpy import array
from lib.custom_input import *
from lib.messager import Message
from array import *
import pandas as pd

### -------------------------------------------------------------------- ABOUT PROGRAMM

initColorama()

_APPNAME_   = Fore.CYAN + "ZTK.BaseSep (x86 Edition)"
_APPVER_    = Fore.LIGHTBLACK_EX + "v0.1.1"
_DEVELOPER_ = Fore.GREEN + "RiotMesh"

print("[ " + _APPNAME_ + " " + _APPVER_ + " - by " + _DEVELOPER_ + Style.RESET_ALL + " ]")

### -------------------------------------------------------------------- ###

excelFilePath = input_("Имя Excel файла или путь к нему: ")

print(Fore.LIGHTBLACK_EX + "Выполняются подсчёты ...")

doc = pd.read_excel(excelFilePath, index_col='n Тел Д', usecols=[0])

### ----------FROM------TO---------------------------------------------- RANGES

allRanges = [[640000, 649999],
            [691000, 691099],
            [691800, 692099],
            [692800, 692999],
            [699000, 699199],
            [699600, 699799]]

allRangesSum = array('i', [])

### -------------------------------------------------------------------- CALCULATE NUMBERS COUNT IN RANGES

i = 0
while i < len(allRanges):

    allRangesSum.append(0)

    for number in doc.index:

        if number >= allRanges[i][0] and number <= allRanges[i][1]:

            allRangesSum[i] += 1

    i += 1

### -------------------------------------------------------------------- CALCULATE NUMBERS COUNT

allRangesNumbers = 0
for count in allRangesSum:
    allRangesNumbers += count

### -------------------------------------------------------------------- PRINT INFO

i = 0
while i < len(allRanges):

    print(Fore.LIGHTBLUE_EX + "Диапазон " + str(i) +
        " (" + str(allRanges[i][0]) + " - " + str(allRanges[i][1]) + "): " +
        Style.RESET_ALL + str(allRangesSum[i]))

    i += 1

print(Fore.LIGHTGREEN_EX + "Всего номеров: " + Style.RESET_ALL + str(allRangesNumbers))

input_("Нажмите любую клавишу чтобы выйти...")