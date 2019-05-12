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
    print Fore.GREEN+"----- * Checking ApiKeys      * -----"
    pasteKeys()
    print Fore.RED+"[*]"+Fore.CYAN+" Putting up the ApiKeys on data.json file"
    time.sleep(1)
    print Fore.YELLOW+"[*] Ready to use"

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
