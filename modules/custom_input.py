from colorama import init as initColorama
from colorama import Fore, Back, Style

initColorama()

inputPrefix = ">> "

def input_(message):
    return input(Fore.LIGHTGREEN_EX + inputPrefix + Style.RESET_ALL + message)