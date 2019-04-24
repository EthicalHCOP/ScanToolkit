# -*- coding: UTF-8 -*-
#!/usr/bin/python

import shodan
from colorama import Fore, init
init()

def shodanS(key):
        option = raw_input("\n1: Shodan Search.\n2: Shodan Host Scanner\nOpt:")
        if option == "1":
                queryok = True
                while queryok:
                        query = raw_input("Insert Query: ")
                        if query != "":
                                queryok = False
                searchQuery(query,key)
        elif option == "2":
                hostok = True
                while hostok:
                        host = raw_input("Insert Host: ")
                        if host != "":
                                hostok = False
                searchHost(host,key)
        else:
                print "Incorrect Option."
                
def searchQuery(query,key):
        
        api = shodan.Shodan(key)
        try:
                results = api.search(query)
                for result in results['matches']:
                        print Fore.GREEN +"IP: "+Fore.RED+str(result['ip_str'])
                        print Fore.MAGENTA + result['data']+"\n"+Fore.RESET
        except shodan.APIError, e:
                print 'Error: %s' % e


def searchHost(host,key):
        api = shodan.Shodan(key)
        host = api.host(host)
        
        print Fore.GREEN +"\nIp: \t\t\t" +Fore.RED+str(host['ip_str'])
        print Fore.GREEN +"Country: \t\t" +Fore.RED+ str(host['country_name']) + "(" + str(host['country_code']) + ")"
        print Fore.GREEN +"Organization: \t\t" +Fore.RED+ str(host['org'])
        print Fore.GREEN +"ISP: \t\t\t"+Fore.RED + str(host['isp'])
        domains = ""
        for d in host['hostnames']:
                domains = domains + "" + str(d) + " "
        print Fore.GREEN +"Domains: \t\t"+Fore.RED+domains
        print Fore.GREEN +"Last Update: \t\t"+Fore.RED + str(host['last_update'])
        print Fore.GREEN +"ASN: \t\t\t"+Fore.RED + str(host['asn'])
        print Fore.GREEN +"Operative System: \t"+Fore.RED + str(host.get('os', 'n/a'))
        ports = ""
        for p in host['ports']:
                ports = ports + "" + str(p) + " "
        print Fore.GREEN +"Ports: \t\t\t"+Fore.RED+ports+Fore.RESET        
        for banner in host['data']:
                print Fore.GREEN +"\nPort-> "+Fore.RED+str(banner['port'])
                print Fore.BLUE +"\n"+str(banner['data'])+Fore.RESET 
