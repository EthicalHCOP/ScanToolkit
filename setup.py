import banners
import time
from colorama import Fore, init
init()

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
    print Fore.RED+"[*]"+Fore.CYAN+" Putting up the ApiKeys on toolkit.py file"
    time.sleep(3)
    print Fore.YELLOW+"[*] Ready to use"
    
def checkDependencies():
    dependencies = []
    print Fore.GREEN+"[*]"+Fore.CYAN+" Checking Shodan Api"
    try:
        import shodan
        dependencies = [['shodan','ok']]
    except:
        dependencies = [['shodan','fail']]

    return dependencies    

def pasteKeys():
    fileread ='toolkit.py'
    Data = []
    text = open(fileread,'r')
    line = 1
    for x in text:
        line = line + 1
        Data.append(x)
    apis=['Shodan_Api_Key']
    keys = []
    for a in apis:
        key = raw_input(Fore.GREEN+"[+]"+Fore.CYAN+" Insert your "+a+": "+Fore.RESET)
        keys.append([a,key])
    Data[13]="    Keys = "+str(keys)+" \n"
    Data[198]= "        start = 1\n"
    write = open(fileread,'w')
    item = 0
    for y in Data:
        write.write(Data[item])
        item=item+1

if __name__ == '__main__':
        setup()
