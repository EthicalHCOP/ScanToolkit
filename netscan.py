import os
import sys
import platform
import socket

from datetime import datetime
from colorama import Fore, init
init()

def netscan():
    print (Fore.YELLOW+"\n--> Host Discover")
    pc_name = socket.gethostname()
    pc_ip = socket.gethostbyname(pc_name)
    print ("You IPv4 is: "+Fore.YELLOW+pc_ip)
    ip = pc_ip
    ipDividida = ip.split('.')
     
    try:
        red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
        comienzo = int(input("Insert the first number to start the scan: "))
        fin = int(input("Insert the last number to finish the scan: "))
    except:
        print(Fore.RED+"[!] Error")
        sys.exit(1)
     
     
    if (platform.system()=="Windows"):
        ping = "ping -n 1"
    else :
        ping = "ping -c 1"
        
    tiempoInicio = datetime.now()
    print ("\n"+Fore.GREEN+"[*] Starting Scanner")
    print (Fore.GREEN+"[*] Scanning from "+red+str(comienzo)+" to "+red+str(fin))
    
    for subred in range(comienzo, fin+1):
        direccion = red+str(subred)
        response = os.popen(ping+" "+direccion)
        for line in response.readlines():
            if ("ttl" in line.lower()):
                '''NameHost = socket.gethostbyaddr(direccion)
                print"[+] "+direccion+"/"+NameHost[0]+" Host is Active "'''
                print(Fore.GREEN + "[+] "+Fore.CYAN+ direccion +Fore.WHITE +" / Host is Active ")
                break
                
    tiempoFinal = datetime.now()
    tiempo = tiempoFinal - tiempoInicio
    print (Fore.GREEN+"[*] Scanner finished. The estimated time was"+ Fore.RED+" %s"%tiempo)

def netscanOPT(start,end):
    print (Fore.YELLOW+"\n--> Host Discover")
    pc_name = socket.gethostname()
    pc_ip = socket.gethostbyname(pc_name)
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


    for subred in range(start, end+1):
        direccion = red+str(subred)
        response = os.popen(ping+" "+direccion)
        for line in response.readlines():
            if ("ttl" in line.lower()):
                '''NameHost = socket.gethostbyaddr(direccion)
                print"[+] "+direccion+"/"+NameHost[0]+" Host is Active "'''
                print(Fore.GREEN + "[+] "+Fore.CYAN+ direccion +Fore.WHITE +" / Host is Active ")
                break
                
    tiempoFinal = datetime.now()
    tiempo = tiempoFinal - tiempoInicio
    print (Fore.GREEN+"[*] Scanner finished. The estimated time was"+ Fore.RED+" %s"%tiempo)
