from os import system
from colorama import Fore
from threading import Lock
from datetime import datetime
from ctypes import windll
from pystyle import Center,Colors,Colorate

lock = Lock()

class Console:
    
    @staticmethod
    def printsc(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}Account Created{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
    
    @staticmethod
    def printe(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}Error Occurred{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printi(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}Info{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printm(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}Mail Verified{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printjs(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTBLUE_EX}Joined Server{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
        
    @staticmethod
    def printhm(content: str):
        lock.acquire()
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTWHITE_EX}{datetime.strftime(datetime.now(), '%X').replace(':',f'{Fore.LIGHTBLACK_EX}:{Fore.LIGHTWHITE_EX}')}{Fore.LIGHTBLACK_EX}] {Fore.LIGHTBLACK_EX}[{Fore.LIGHTMAGENTA_EX}Humanization Completed{Fore.LIGHTBLACK_EX}]{Fore.LIGHTWHITE_EX} > {content}")
        lock.release()
    
class Tools:
    
    @staticmethod
    def clear():
        system('cls')

    @staticmethod
    def setTitle(threads: int, proxies: int, created: int):
        windll.kernel32.SetConsoleTitleW(f"Seasmash Guilded Creator  |  Threads: {threads}  |  Loaded Proxies: {proxies}  |  Created: {created}  |  Made by github.com/seadhy")

    @staticmethod
    def printLogo():
        print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter("""

           ▄████████    ▄████████    ▄████████    ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████    ▄████████    ▄█    █▄    
          ███    ███   ███    ███   ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███   ███    ███   
          ███    █▀    ███    █▀    ███    ███   ███    █▀  ███   ███   ███   ███    ███   ███    █▀    ███    ███   
          ███         ▄███▄▄▄       ███    ███   ███        ███   ███   ███   ███    ███   ███         ▄███▄▄▄▄███▄▄ 
        ▀███████████ ▀▀███▀▀▀     ▀███████████ ▀███████████ ███   ███   ███ ▀███████████ ▀███████████ ▀▀███▀▀▀▀███▀  
                 ███   ███    █▄    ███    ███          ███ ███   ███   ███   ███    ███          ███   ███    ███   
           ▄█    ███   ███    ███   ███    ███    ▄█    ███ ███   ███   ███   ███    ███    ▄█    ███   ███    ███   
         ▄████████▀    ██████████   ███    █▀   ▄████████▀   ▀█   ███   █▀    ███    █▀   ▄████████▀    ███    █▀   

                      ⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
                      ┇      [Discord] https://discord.gg/6hP3mHKSqf       ┇
                      ┇      [Github]  https://github.com/seadhy           ┇
                      ⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟


                      """)))
