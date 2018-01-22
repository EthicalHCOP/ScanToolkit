#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from colorama import Fore, init

init()

version = "v.1.2"

def randomBanner():
    ban = random.randrange(1,10)
    if ban == 1  or ban == 2:
        banner1()
    elif ban == 3 or ban == 4:
        banner2()
    elif ban == 5 or ban == 6:
        banner3()
    elif ban == 7 or ban == 8:
        banner4()    
    else:  
        banner5()


def banner1():
    print "_______________________________________________________________________________"+Fore.LIGHTGREEN_EX
    print "                                                                               "
    print "                 ========    =======    =======    ===      ==                 "
    print "                 ==          ==         ==   ==    == ==    ==                 "
    print "                 ==          ==         ==   ==    ==  ==   ==                 "
    print "                 ========    ==         =======    ==   ==  ==                 "
    print "                       ==    ==         ==   ==    ==    == ==                 "
    print "                       ==    ==         ==   ==    ==     = ==                 "
    print "                 ========    =======    ==   ==    ==      ===                 "
    print "                                                                               "
    print " ========     ========     ========     ==       ==     ==   ==    ========    "
    print "    ==       ==      ==   ==      ==    ==       ==   ==     ==       ==       "
    print "    ==       ==      ==   ==      ==    ==       ==  ==      ==       ==       "
    print "    ==       ==      ==   ==      ==    ==       ====        ==       ==       "
    print "    ==       ==      ==   ==      ==    ==       ==  ==      ==       ==       "
    print "    ==       ==      ==   ==      ==    ==       ==   ==     ==       ==       "
    print "    ==       ==      ==   ==      ==    ==       ==    ==    ==       ==       "
    print "    ==        ========     ========     ======   ==     ==   ==       ==  "+Fore.RESET+version+""
    print "__________________________________ScanToolkit__________________________________"
    print "|      "+Fore.RED+"A toolkit written on python and made only for educational purposes."+Fore.RESET+"    |"
    print "|By: "+Fore.BLUE+"EthicalHackingCOP "+Fore.RESET+"Github:"+Fore.BLUE+"https://github.com/EthicalHackingCOP/ScanToolkit"+Fore.RESET+"|"
    print "|_____________________________________________________________________________|"

def banner2():
    print "_______________________________________________________________________________"
    print Fore.BLUE+"                                                                               "
    print "                           _..---.._                                           "
    print "                        .-"+Fore.RED+"__|_____|__"+Fore.BLUE+"'-.                                       "
    print "                     .'"+Fore.RED+"\    |     |    /"+Fore.BLUE+"'-.                                    "
    print "                   .'  "+Fore.RED+"|    |     |    |   "+Fore.BLUE+"'.                                  "
    print "                  / "+Fore.RED+"\__|____|_____|____|____/"+Fore.BLUE+"\                                 "
    print "                 /     "+Fore.RED+"|    |     |    |      "+Fore.BLUE+"\                                "
    print "                ;      "+Fore.RED+"|    |     |    |       "+Fore.BLUE+";                               "
    print "                ;"+Fore.RED+"______|____|_____|____"+Fore.CYAN+"..........."+Fore.BLUE+"                             "
    print "                |      "+Fore.RED+"|    |     |  "+Fore.CYAN+"============== "+Fore.BLUE+"                           "
    print "                ;      "+Fore.RED+"|    |     |"+Fore.CYAN+"===            ==="+Fore.BLUE+"                          "
    print "                 \  "+Fore.RED+"___|____|_____"+Fore.CYAN+"==="+Fore.GREEN+"Ip:xx.xx.xx.xx"+Fore.CYAN+"==="+Fore.BLUE+"                         "
    print "                  \\"+Fore.RED+"/   |    |     "+Fore.CYAN+"==="+Fore.GREEN+"Ports:22,25,80"+Fore.CYAN+"=== "+Fore.BLUE+"                        "
    print "                   '.  "+Fore.RED+"|    |     "+Fore.CYAN+"==="+Fore.GREEN+"Country: JPN  "+Fore.CYAN+"==="+Fore.BLUE+"                         "
    print "                     '-"+Fore.RED+"/ ___|_____"+Fore.CYAN+"==="+Fore.GREEN+"HostName:Zt.jp"+Fore.CYAN+"==="+Fore.BLUE+"                         "
    print "                       '- _ "+Fore.RED+"|     "+Fore.CYAN+"==="+Fore.GREEN+"Org: Zt kart  "+Fore.CYAN+"==="+Fore.BLUE+"                         "
    print "     ________              '* -.-  "+Fore.CYAN+"===            ==="+Fore.BLUE+"                          "
    print "    |   _____|                      "+Fore.CYAN+"============== \\"+Fore.BLUE+"                         " 
    print "    |  |_____ CAN                     "+Fore.CYAN+"''''''''''''\  \\"+Fore.BLUE+"                        "
    print "    |_____   |____________                         "+Fore.CYAN+"\  \\"+Fore.BLUE+"                       "
    print "     _____|  |_____  _____|                         "+Fore.CYAN+"\  \\"+Fore.BLUE+"                      "
    print "    |________|    |  |                               "+Fore.CYAN+"\  \\"+Fore.BLUE+"                     "
    print "                  |  |                                "+Fore.CYAN+"\  \\"+Fore.BLUE+"                    "
    print "                  |  |                                 "+Fore.CYAN+"\  \\"+Fore.BLUE+"                   "
    print "                  |__| OOLKIT "+version+"                     "+Fore.CYAN+"\_-'"+Fore.RESET+"                   "
    print "                                                                               "
    print "__________________________________ScanToolkit__________________________________"
    print "|      "+Fore.RED+"A toolkit written on python and made only for educational purposes."+Fore.RESET+"    |"
    print "|By: "+Fore.BLUE+"EthicalHackingCOP "+Fore.RESET+"Github:"+Fore.BLUE+"https://github.com/EthicalHackingCOP/ScanToolkit"+Fore.RESET+"|"
    print "|_____________________________________________________________________________|"

def banner3():
    print "_______________________________________________________________________________"
    print "                                                                               "
    print "         ____________________________________________________________          "
    print "        | .========================================================. |         "
    print "        | |                                                        | |         "
    print "        | | "+Fore.GREEN+"ScanToolkit "+version+" 'Scan your environments and systems'"+Fore.RESET+" | |         "
    print "        | | "+Fore.GREEN+"ScanToolkit "+version+" 'Scan your environments and systems'"+Fore.RESET+" | |         "
    print "        | | "+Fore.GREEN+"ScanToolkit "+version+" 'Scan your environments and systems'"+Fore.RESET+" | |         "
    print "        | | "+Fore.GREEN+"ScanToolkit "+version+" 'Scan your environments and systems'"+Fore.RESET+" | |         "
    print "        | | "+Fore.GREEN+"ScanToolkit "+version+" 'Scan your environments and systems'"+Fore.RESET+" | |         "
    print "        | | "+Fore.GREEN+"ScanToolkit "+version+" 'Sca"+Fore.RESET+"                                 | |         "
    print "        | |           .-----.    /                                 | |         "
    print "        | |          /       \  /                                  | |         "
    print "        | |         |         |/ \                                 | |         "
    print "        | |          \_______//  /                                 | |         "
    print "        | |          __(____)/  /                                  | |         "
    print "        | .=========/ ,_ _    _/===================================. |         "
    print "        |___________\___\_)   |______________________________________|         "
    print "                      |_______|                                                "
    print "                      |  | |  |                                                "
    print "                      |__| |__|                                                "
    print "                      (__) (__)                                                "
    print "                                                                               "
    print "__________________________________ScanToolkit__________________________________"
    print "|      "+Fore.RED+"A toolkit written on python and made only for educational purposes."+Fore.RESET+"    |"
    print "| By:"+Fore.BLUE+"EthicalHackingCOP "+Fore.RESET+"Github:"+Fore.BLUE+"https://github.com/EthicalHackingCOP/ScanToolkit"+Fore.RESET+"|"
    print "|_____________________________________________________________________________|"

def banner4():
    print "_______________________________________________________________________________________________"
    print Fore.LIGHTGREEN_EX+"                                              /$$                      /$$/$$      /$$  /$$    "
    print "                                             | $$                     | $| $$     |__/ | $$    "
    print "  /$$$$$$$ /$$$$$$$ /$$$$$$ /$$$$$$$        /$$$$$$   /$$$$$$  /$$$$$$| $| $$   /$$/$$/$$$$$$  "
    print " /$$_____//$$_____/|____  $| $$__  $$      |_  $$_/  /$$__  $$/$$__  $| $| $$  /$$| $|_  $$_/  "
    print "|  $$$$$$| $$       /$$$$$$| $$  \ $$        | $$   | $$  \ $| $$  \ $| $| $$$$$$/| $$ | $$    "
    print " \____  $| $$      /$$__  $| $$  | $$        | $$ /$| $$  | $| $$  | $| $| $$_  $$| $$ | $$ /$$"
    print " /$$$$$$$|  $$$$$$|  $$$$$$| $$  | $$        |  $$$$|  $$$$$$|  $$$$$$| $| $$ \  $| $$ |  $$$$/"
    print "|_______/ \_______/\_______|__/  |__/         \___/  \______/ \______/|__|__/  \__|__/  \____/  "
    print "                                                                                        "+version+Fore.RESET
    print "__________________________________________ScanToolkit__________________________________________"
    print "|              "+Fore.RED+"A toolkit written on python and made only for educational purposes."+Fore.RESET+"            |"
    print "|         By:"+Fore.BLUE+"EthicalHackingCOP "+Fore.RESET+"Github:"+Fore.BLUE+"https://github.com/EthicalHackingCOP/ScanToolkit"+Fore.RESET+"        |"
    print "|_____________________________________________________________________________________________|"

def banner5():
    print "_______________________________________________________________________________"+Fore.CYAN
    print "                     \./                            |>>>                       "
    print "                        \./                         |                          "
    print "                   /'\                |>>>      _  _|_  _         |>>>         "
    print Fore.LIGHTGREEN_EX+"  ____"+Fore.CYAN+"                                |        |;| |;| |;|        |            "
    print Fore.LIGHTGREEN_EX+" / ___|  ___ __ _ _ __"+Fore.CYAN+"            _  _|_  _    \\.    .  /    _  _|_  _        "
    print Fore.LIGHTGREEN_EX+" \___ \ / __/ _` | '_ \\"+Fore.CYAN+"          |;|_|;|_|;|    \\:. ,  /    |;|_|;|_|;|       "
    print Fore.LIGHTGREEN_EX+"  ___) | (_| (_| | | | |"+Fore.CYAN+"         \\..      /    ||;   . |    \\.    .  /       "
    print Fore.LIGHTGREEN_EX+" |__________\__,_|_|_|_|  "+Fore.LIGHTBLUE_EX+" _ _ "+Fore.CYAN+"   \\.  ,  /     ||:  .  |     \\:  .  /        "
    print Fore.LIGHTBLUE_EX+"   |_   ____   ___ | | | _(_| |_"+Fore.CYAN+"   ||:   |_   _ ||_ . _ | _   _||:   |         "
    print Fore.LIGHTBLUE_EX+"     | |/ _ \ / _ \| | |/ | | __|"+Fore.CYAN+"  ||:  .|||_|;|_|;|_|;|_|;|_|;||:.  |         "
    print Fore.LIGHTBLUE_EX+"     | | (_) | (_) | |   <| | |_ "+Fore.CYAN+"  ||:   ||.    .     .      . ||:  .|         "
    print Fore.LIGHTBLUE_EX+"     |_|\___/ \___/|_|_|\_|_|\__|"+Fore.CYAN+"  ||: . || .     . .   .  ,   ||:   |         "
    print "              "+Fore.LIGHTRED_EX+version+Fore.CYAN+"                ||:   ||:  ,  _______   .   ||: , |         "
    print "                                   ||:   || .   /+++++++\    . ||:   |         "
    print "                                   ||:   ||.    |+++++++| .    ||: . |         "
    print Fore.GREEN+"                                __"+Fore.CYAN+" ||: . ||: ,  |+++++++|.  . _||_   |         "
    print Fore.GREEN+"      ,+-.,__    ,-~-_.~-__--`~    '--~~__"+Fore.CYAN+"|.    |+++++__|"+Fore.GREEN+"----~    ~`---,__       "
    print "---*''       \"\"''                         ~---__"+Fore.CYAN+"|"+Fore.GREEN+",--~'                    '\"\""+Fore.RESET
    print "__________________________________ScanToolkit__________________________________"
    print "|      "+Fore.RED+"A toolkit written on python and made only for educational purposes."+Fore.RESET+"    |"
    print "| By:"+Fore.BLUE+"EthicalHackingCOP "+Fore.RESET+"Github:"+Fore.BLUE+"https://github.com/EthicalHackingCOP/ScanToolkit"+Fore.RESET+"|"
    print "|_____________________________________________________________________________|"