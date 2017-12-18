#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
from colorama import Fore, init

init()

version = "v.1.1"

def randomBanner():
    ban = random.randrange(1,7)
    if ban == 1  or ban == 2:
        banner1()
    elif ban == 3 or ban == 4:
        banner2()
    else:  
        banner3()


def banner1():
    print "_______________________________________________________________________________"
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
    print "    ==        ========     ========     ======   ==     ==   ==       ==  "+version+""
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