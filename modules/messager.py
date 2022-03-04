from colorama import init as initColorama
from colorama import Fore, Back, Style
initColorama()

### --------------------------------------------- ### RIOT MESH

class Message:

    totalInfo       = 0
    totalWarnings   = 0
    totalErrors     = 0
    totalCalls      = 0

    prefInfo        = "[ INFO ] "
    prefWarning     = "[ WARNING ] "
    prefError       = "[ ERROR ] "

    colorInfo       = Style.RESET_ALL
    colorWarning    = Fore.LIGHTYELLOW_EX
    colorError      = Fore.LIGHTRED_EX

    def Info(self, mess):
        print(self.colorInfo + self.prefInfo + mess + Style.RESET_ALL)
        self.totalInfo += 1

    def Warning(self, mess):
        print(self.colorWarning + self.prefWarning + mess + Style.RESET_ALL)
        self.totalWarnings += 1

    def Error(self, mess):
        print(self.colorError + self.prefError + mess + Style.RESET_ALL)
        self.totalErrors += 1

    def GetStats(self):
        print("[ Messager Lib - Stats ]")
        print("Total INFO:      " + str(self.totalInfo))
        print("Total WARNING:   " + str(self.totalWarnings))
        print("Total ERROR:     " + str(self.totalErrors))
        print("Total messages:  " + str(self.totalCalls))