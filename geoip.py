# -*- coding: UTF-8 -*-
#!/usr/bin/python

import requests
from colorama import Fore, init
init()


def GeoIp():
	print "Insert Ip To Scan. (No Ip for My Ip Address)"
	host = raw_input("IPv4: ");
	if host != "":
		try:
			remoteIpOPT(host)
		except Exception, e:
			print "\n[!] Error: "+str(e)
	else:
		try:
			myIpOPT()
		except Exception, e:
			print "\n[!] Error: "+str(e)

def remoteIpOPT(host):
	request = requests.get('http://ipinfo.io/'+host+'/json').text
	request = request.split("\n")

	Datos= []

	for x in request:
		if x == "{" or x == "}":
			continue
		Datos.append(x)
	Matriz = []

	for y in Datos:
		a = [y.split("\"")[1],y.split("\"")[3]]
		Matriz.append(a)
	iterate = 0

	print("\n"+Fore.MAGENTA + "Scanning Ip Address: " + host +Fore.WHITE)

	for z in Matriz:
		if Matriz[iterate][0] == "loc":
			url = "https://maps.google.com/?q="+str(Matriz[iterate][1]).split(",")[0]+","+str(Matriz[iterate][1]).split(",")[1]+""
		print(Fore.GREEN + Matriz[iterate][0]+": "+ Fore.RED + Matriz[iterate][1])
		iterate = iterate + 1

	print(Fore.MAGENTA + url + Fore.WHITE)

def myIpOPT():
	request = requests.get('http://ipinfo.io/').text
	request = request.split("\n")

	Datos= []

	for x in request:
		if x == "{" or x == "}":
			continue
		Datos.append(x)
	Matriz = []

	for y in Datos:
		a = [y.split("\"")[1],y.split("\"")[3]]
		Matriz.append(a)
	iterate = 0
	print("\n"+Fore.MAGENTA + "Your Ip Address:" + Fore.WHITE)
	for z in Matriz:
		if Matriz[iterate][0] == "loc":
			url = "https://maps.google.com/?q="+str(Matriz[iterate][1]).split(",")[0]+","+str(Matriz[iterate][1]).split(",")[1]+""
		print(Fore.GREEN + Matriz[iterate][0]+": "+ Fore.RED + Matriz[iterate][1])
		iterate = iterate + 1

	print(Fore.MAGENTA + url + Fore.WHITE)