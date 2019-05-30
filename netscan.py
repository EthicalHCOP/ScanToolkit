# -*- coding: UTF-8 -*-
#!/usr/bin/python

import os
import sys
import platform
import socket
import netifaces

from datetime import datetime
from colorama import Fore, init
init()

def netscan(start,end):
    ifc = []
    ifaces_allowed = ['wlan0','eth0','tun0']
    interfaces = netifaces.interfaces()
    for x in interfaces:
        if x in ifaces_allowed and platform.system()!="Windows":
            dts = []
            dts.append(x)
            try:
                datos = netifaces.ifaddresses(x)
                variables = datos.keys()
                dts.append(datos[2][0]['addr'])
                ifc.append(dts)
            except:
                continue
        else:
            dts = []
            dts.append(x)
            try:
                datos = netifaces.ifaddresses(x)
                variables = datos.keys()
                dts.append(datos[2][0]['addr'])
                ifc.append(dts)
            except:
                continue
    print (Fore.YELLOW+"\n--> Host Discover")
    itr = 1
    
    safe_ifc = ifc
    for x in ifc:
        print "---------------|"+str(itr)+"|---------------"
        print "|\t"+x[0]+": "+x[1]+"\t|"
        print "---------------------------------"
        itr += 1
    print (Fore.YELLOW+"\n[+] Select a interface number to scan: ")
    iface = input()
    pc_ip = safe_ifc[iface-1][1]
    print ("You IPv4 is: "+Fore.YELLOW+pc_ip)
    ip = pc_ip
    ipDividida = ip.split('.')
     
    try:
        red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
    except:
        print(Fore.RED+"[!] Error")
        sys.exit(1)
     
     
    if (platform.system()=="Windows"):
        ping = "ping -n 1"
    else :
        ping = "ping -c 1"
        
    tiempoInicio = datetime.now()
    print ("\n"+Fore.GREEN+"[*] Starting Scanner")
    print (Fore.GREEN+"[*] Scanning from "+red+str(start)+" to "+red+str(end))


    for subred in range(int(start), int(end)+1):
        direccion = red+str(subred)
        response = os.popen(ping+" "+direccion)
        for line in response.readlines():
            if ("ttl" in line.lower()):
                print(Fore.GREEN + "[+] "+Fore.CYAN+ direccion +Fore.WHITE +" / Host is Active ")
                break
                
    tiempoFinal = datetime.now()
    tiempo = tiempoFinal - tiempoInicio
    print (Fore.GREEN+"[*] Scanner finished. The estimated time was"+ Fore.RED+" %s"%tiempo)
