# -*- coding: UTF-8 -*-
#!/usr/bin/python

import time
import json
try:
    import banners
    from colorama import Fore, init
    init()
except:
    print "First execute pip install -r requeriments.txt"
    exit()
banners.randomBanner()
def setup():
    print "\n[*] Starting Configuration..."
    print Fore.GREEN+"----- * Checking Dependencies * -----"
    depiterator = 0
    missing = 0
    for d in checkDependencies() :
        if d[1] == 'fail':
            print Fore.RED+"[-] "+Fore.CYAN+"Dependence "+ d[depiterator] + " not found."+Fore.RESET
            missing = missing + 1
        else:
            print Fore.BLUE+"[+] "+Fore.CYAN+"Dependence "+ d[depiterator]+ " found."+Fore.RESET
    if missing > 0 :
        print Fore.RED+"[-] Please install the previous dependencies."
        exit(0)
    print Fore.GREEN+"----- * Checking ApiKeys      * -----"
    pasteKeys()
    print Fore.RED+"[*]"+Fore.CYAN+" Putting up the ApiKeys on data.json file"
    time.sleep(1)
    print Fore.YELLOW+"[*] Ready to use"
    
def checkDependencies():
    dependencies = []
    dep = open('requeriments.txt','r')
    for x in dep.readlines():
        x = x.replace("\n","")
        print Fore.GREEN+"[*]"+Fore.CYAN+" Checking "+x.capitalize()+" Requeriment."
        try:
            __import__(x)
            dependencies.append([x,'ok'])
        except:
            dependencies.append([x,'fail'])

    return dependencies

def pasteKeys():
    file = "data.json"
    data = eval(open(file, 'r').read())
    apis = ['Shodan_Api_Key']
    for a in apis:
        key = raw_input(Fore.GREEN + "[+]" + Fore.CYAN + " Insert your " + a + ": " + Fore.RESET)
        data['keys'][a]=key
    data['starting']=1
    with open(file, 'w') as fp:
        json.dump(data, fp)

if __name__ == '__main__':
    setup()
