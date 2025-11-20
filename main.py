import os
import time

# from core.{FileName} import *
from colorama import Fore, init
from pystyle import Colorate, Colors
init(autoreset=True)


class SonnTemplate:
    def __init__(self):
        self.banner_art = r"""

                             _________  ____  ____
                            / ___/ __ \/ __ \/ __ \
                           (__  ) /_/ / / / / / / /
                          /____/\____/_/ /_/_/ /_/
                         _________________________
                                       @empireofuv
        """
        self.home_art = r"""

        [01] > Option 1         [02] > Option 2         [03] > Option 3
        [04] > Option 4         [05] > Option 5         [06] > Option 6
                                [07] > Exit

        """
        self.setup()

    def setup(self):
        os.system("cls")
        self.homemenu()

    def banner(self):
        print(Colorate.Vertical(Colors.red_to_black, self.banner_art))

    def homemenu(self):
        while True:
            os.system("title sonn@MAIN")
            os.system("cls")
            self.banner()
            print(Colorate.Vertical(Colors.red_to_black, self.home_art))
            inp = input(Fore.RED + "[sonn@MAIN] > ")

            if inp == "1":
                # function
            elif inp == "2":
                # function
                pass
            elif inp == "3":
                # function
                pass
            elif inp == "4":
                # function
                pass
            elif inp == "5":
                # function
                pass
            elif inp == "6":
                # function
                pass
            elif inp == "7":
                # function
                pass
            else:
                print(Fore.RED + "[-] Invalid option. Try again." + Fore.RESET)
                time.sleep(1)
                self.homemenu()

    # How to make a page handler
    # def {PAGENAME}(self):
    #   while True:
    #   os.system('title {TITLEHERE}')
    #   os.system('cls')
    #   self.banner()
    #   print({PageOptions})
    #   inp = input(Fore.RED + "{InputHere}" + Fore.RESET)
    #
    #   if inp = "1":
    #       function
    # else:
    #       print(Fore.RED + "Invalid option. Try again." + Fore.RESET)
    # time.sleep(1)
    # self.{PageName}


# Usage
if __name__ == "__main__":
    sonntemp = SonnTemplate()
