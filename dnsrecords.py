import requests
from colorama import Fore, init
init()


def DNSRecord():
	print Fore.LIGHTGREEN_EX+"[*] Insert DNS To Scan."
	host = raw_input(Fore.LIGHTGREEN_EX+"[*] DNS: "+Fore.LIGHTRED_EX);
	api= "https://api.hackertarget.com/hostsearch/?q="
	request = requests.get(api+host).text
	if request == "API count exceeded":
		print -Fore.LIGHTRED_EX+"[-] you has been use this API many times and you has been locked. try it again more later."
		exit(0)
	dnsList=[]
	ipList=[]
	hosts=0
	for x in request.split("\n"):
		try:
			if str(x).split(",")[0] != "":
				dnsList.append(str(x).split(",")[0])
			ipList.append(str(x).split(",")[1])
			hosts += 1
		except:
			continue
	print Fore.CYAN+"*---------------------------------------------------------------*"
	print "|\t\t\t   DNS Records\t\t\t\t|"
	print "|"+Fore.LIGHTBLUE_EX+"\t\tDNS\t\t|\t     IPv4\t\t"+Fore.CYAN+"|"
	for dns in dnsList:
		for ip in ipList:
			print Fore.CYAN+"|"+Fore.LIGHTYELLOW_EX+"\t"+dns + "\t"+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTYELLOW_EX+"\t"+ip+"\t\t"+Fore.CYAN+"|"+Fore.RESET 		
			break
	print Fore.CYAN+"*---------------------------------------------------------------*"+Fore.RESET
	hd = raw_input("[*] wish you print the headers from de hosts? y/N: ")
	if hd == "Y" or hd == "y" or hd == "YES" or hd == "YEs" or hd == "Yes" or hd == "yes" or hd == "YeS" or hd == "yeS" or hd == "yEs" or hd == "yES":
		for dns in dnsList:
			print Fore.CYAN+"*---------------------------------------------------------------*"+Fore.RESET
	   		print Fore.YELLOW+"[*]"+Fore.CYAN+" Headers for "+Fore.LIGHTRED_EX+dns
	   		lines = getHeader(dns)
	   		lines = str(lines).split("\n")
	   		for l in lines:
	   			if l == "":
	   				continue
	   			else:
	   				print Fore.LIGHTBLUE_EX+"[+] "+Fore.LIGHTGREEN_EX+l
	   		print Fore.CYAN+"*---------------------------------------------------------------*"+Fore.RESET
	print Fore.LIGHTBLUE_EX+"[+] "+Fore.LIGHTCYAN_EX+"Host Founds: "+Fore.LIGHTRED_EX+str(hosts)+Fore.LIGHTCYAN_EX +" for "+Fore.YELLOW +host+Fore.RESET

def DNSRecordOpt(host):
	api= "https://api.hackertarget.com/hostsearch/?q="
	request = requests.get(api+host).text
	if request == "API count exceeded":
		print Fore.LIGHTRED_EX+"[-] you has been use this API many times and you has been locked. try it again more later."
		exit(0)
	dnsList=[]
	ipList=[]
	hosts=0
	for x in request.split("\n"):
		try:
			if str(x).split(",")[0] != "":
				dnsList.append(str(x).split(",")[0])
			ipList.append(str(x).split(",")[1])
			hosts += 1
		except:
			continue
	print Fore.CYAN+"*---------------------------------------------------------------*"
	print "|\t\t\t   DNS Records\t\t\t\t|"
	print "|"+Fore.LIGHTBLUE_EX+"\t\tDNS\t\t|\t     IPv4\t\t"+Fore.CYAN+"|"
	for dns in dnsList:
		for ip in ipList:
			print Fore.CYAN+"|"+Fore.LIGHTYELLOW_EX+"\t"+dns + "\t"+Fore.LIGHTBLUE_EX+"|"+Fore.LIGHTYELLOW_EX+"\t"+ip+"\t\t"+Fore.CYAN+"|"+Fore.RESET 		
			break
	print Fore.CYAN+"*---------------------------------------------------------------*"+Fore.RESET
	hd = raw_input("[*] wish you print the headers from de hosts? y/N: ")
	if hd == "Y" or hd == "y" or hd == "YES" or hd == "YEs" or hd == "Yes" or hd == "yes" or hd == "YeS" or hd == "yeS" or hd == "yEs" or hd == "yES":
		for dns in dnsList:
			print Fore.CYAN+"*---------------------------------------------------------------*"+Fore.RESET
	   		print Fore.YELLOW+"[*]"+Fore.CYAN+" Headers for "+Fore.LIGHTRED_EX+dns
	   		lines = getHeader(dns)
	   		lines = str(lines).split("\n")
	   		for l in lines:
	   			if l == "":
	   				continue
	   			else:
	   				print Fore.LIGHTBLUE_EX+"[+] "+Fore.LIGHTGREEN_EX+l
	   		print Fore.CYAN+"*---------------------------------------------------------------*"+Fore.RESET
	print Fore.LIGHTBLUE_EX+"[+] "+Fore.LIGHTCYAN_EX+"Host Founds: "+Fore.LIGHTRED_EX+str(hosts)+Fore.LIGHTCYAN_EX +" for "+Fore.YELLOW +host+Fore.RESET

def getHeader(dns):
	api= "https://api.hackertarget.com/httpheaders/?q="
	request = requests.get(api+dns).text
	return request