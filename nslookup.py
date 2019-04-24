# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import socket
import scanning
import toolkit
import platform

from colorama import Fore, init
init()

def nslookupscan():
    print "\n--->Nslookup type=(A, ANY, CNAME, MX, NS, PTR, SOA, SRV)\n"
    commands = raw_input("[!] Insert option(s): nslookup ")
    path=raw_input("[!] dns/host: ")
    try:
        ip = socket.gethostbyname(path)
        print (Fore.GREEN+"[*] Scanning "+ip+"\n")
        comandos = commands.split(",")
        for y in range(len(comandos)):
            cmd ="nslookup -type="+comandos[y]+" "+path
            print (Fore.YELLOW+"[*] Launching "+cmd+"\n")
            result=os.popen(cmd)
            datos=result.readlines()
            for x in range(len(datos)):
                if datos[x] == "\n":
                    continue
                else:
                    print (Fore.GREEN+"[+] "+Fore.CYAN+datos[x])
        sp="N"
        sp = raw_input(Fore.GREEN+"[*] "+Fore.RESET+"You wanna scan the ports of the host: "+ip+" [y/N]: ")
        if (sp=="Y" or sp=="YES" or sp=="YeS" or sp=="Yes" or sp=="yes" or sp=="yeS" or sp=="yES" or sp=="yEs" or sp=="y"):
            scanning.scan(ip)
        elif(sp=="N" or sp=="NO" or sp=="No" or sp=="no" or sp=="nO" or sp=="n"):
            exit(0)
    except:
        if platform.system() == "Linux"or platform.system() == "Unix":
            print "Error this module doesn't works on linux"

def nslookupscanOPT(commands,path):
    print "\n--->Nslookup type=(A, ANY, CNAME, MX, NS, PTR, SOA, SRV)\n"
    try:
        ip = socket.gethostbyname(path)
        print (Fore.GREEN+"[*] Scanning "+ip+"\n")
        comandos = commands.split(",")
        for y in range(len(comandos)):
            cmd ="nslookup -type="+comandos[y]+" "+path
            print (Fore.YELLOW+"[*] Launching "+cmd+"\n")
            result=os.popen(cmd)
            datos=result.readlines()
            for x in range(len(datos)):
                if datos[x] == "\n":
                    continue
                else:
                    print (Fore.GREEN+"[+] "+Fore.CYAN+datos[x])
        sp="N"
        sp = raw_input(Fore.GREEN+"[*] "+Fore.RESET+"You wanna scan the ports of the host: "+ip+" [y/N]: ")
        if (sp=="Y" or sp=="YES" or sp=="YeS" or sp=="Yes" or sp=="yes" or sp=="yeS" or sp=="yES" or sp=="yEs" or sp=="y"):
            scanning.scan(ip)
        elif(sp=="N" or sp=="NO" or sp=="No" or sp=="no" or sp=="nO" or sp=="n"):
            exit(0)
    except:
        if platform.system() == "Linux"or platform.system() == "Unix":
            print "Error this module doesn't works on linux"