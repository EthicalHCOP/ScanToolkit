import socket
from colorama import Fore, init
init()

def scanNA():
    points=0
    print (Fore.GREEN+"\n--> Ports Scanner")
    while(points != 3):
        ip = raw_input("Insert IPv4: ")

        lengthip= len(ip)
        
        for i in range (0,lengthip):
            if (ip[i]=="."):
                points = points+1
        if(points==3):
            break
        else:
            print (Fore.RED+"this not is a IPv4")
        break
        exit(0)
    
    
    ALL = "Y"
    ALL = raw_input("you want scan all ports?[Y/n] ")
    if(ALL==""):
        ALL = "Y"        
    if(ALL == "Y" or ALL =="y" or ALL =="YES" or ALL =="yes" or ALL =="YeS" or ALL =="YEs" or ALL =="yES"):
        port = [1,7,9,13,17,19,20,21,22,23,25,37,43,53,67,68,69,70,79,80,88,110,111,113,119,123,135,137,138,139,143,161,162,177,389,443,445,465,500,512,513,514,515,520,587,591,631,666,690,993,995,1080,1337,1352,1433,1434,1494,1512,1521,1701,1720,1723,1761,1863,1935,2049,2082,2083,2086,2427,3030,3074,3128,3306,3389,3396,3690,4662,4672,4899,5000,5060,5190,5222,5223,5269,5432,5517,5631,5632,5400,5500,5600,5700,5800,5900,6000,6112,6129,6346,6347,6348,6349,6350,6355,6667,6880,6969,7100,8000,8008,8080,8118,9009,9898,10000,19226,12345,25565,31337,45003]   
        length = len(port)
        print (Fore.CYAN+"Scanning...")
        for x in range(0, length):
            sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sock.connect_ex((ip,port[x])):
                '''
                if(port[x] == 53 or port[x] ==67  or port[x] ==68 or port[x] ==69 or port[x] ==123 or port[x] ==161 or port[x] ==500 or port[x] ==514 or port[x] ==520 or port[x] ==1701 or port[x] ==1720 or port[x] ==2427 or port[x] ==3074 or port[x] ==4672 or port[x] ==5060 or port[x] ==5632 or port[x] ==6112 or port[x] ==6347 or port[x] ==6348 or port[x] ==6349 or port[x] ==6350 or port[x] ==6355 or port[x] ==7100 ):
                    print "The port "+str(port[x])+"/udp is close"
                elif(port[x] == 43):
                    print "The port "+str(port[x])+"/betocp is close"
                else:
                    print "The port "+str(port[x])+"/tcp is close"
             '''   
            else:
                if(port[x] == 53 or port[x] ==67  or port[x] ==68 or port[x] ==69 or port[x] ==123 or port[x] ==161 or port[x] ==500 or port[x] ==514 or port[x] ==520 or port[x] ==1701 or port[x] ==1720 or port[x] ==2427 or port[x] ==3074 or port[x] ==4672 or port[x] ==5060 or port[x] ==5632 or port[x] ==6112 or port[x] ==6347 or port[x] ==6348 or port[x] ==6349 or port[x] ==6350 or port[x] ==6355 or port[x] ==7100 ):
                    print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[x])+Fore.CYAN+"/udp is open")
                elif(port[x] == 43):
                    print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[x])+Fore.CYAN+"/betocp is open")
                else:
                    print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[x])+Fore.CYAN+"/tcp is open")
        print "[*] Was been scanned "+str(length)+" ports successfull."
    else:
        port = input("Insert Port to scann: ")
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((ip,port)):
            '''
            if(port == 53 or port ==67  or port ==68 or port ==69 or port ==123 or port ==161 or port ==500 or port ==514 or port ==520 or port ==1701 or port ==1720 or port ==2427 or port ==3074 or port ==4672 or port ==5060 or port ==5632 or port ==6112 or port ==6347 or port ==6348 or port ==6349 or port ==6350 or port ==6355 or port ==7100 ):
                print "The port "+str(port)+"/udp is close"
            elif(port == 43):
                print "The port "+str(port)+"/betocp is close"
            else:
                print "The port "+str(port)+"/tcp is close"
            '''
        else:
            print (Fore.CYAN+"Scanning...")
            if(port == 53 or port ==67  or port ==68 or port ==69 or port ==123 or port ==161 or port ==500 or port ==514 or port ==520 or port ==1701 or port ==1720 or port ==2427 or port ==3074 or port ==4672 or port ==5060 or port ==5632 or port ==6112 or port ==6347 or port ==6348 or port ==6349 or port ==6350 or port ==6355 or port ==7100 ):
                print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port)+Fore.CYAN+"/udp is open")
            elif(port == 43):
                print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port)+Fore.CYAN+"/betocp is open")
            else:
                print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port)+Fore.CYAN+"/tcp is open")

def scan(ip):
    
    points=0
    print (Fore.GREEN+"\n--> Ports Scanner")
    while(points != 3):
        lengthip= len(ip)
        
        for i in range (0,lengthip):
            if (ip[i]=="."):
                points = points+1
        if(points==3):
            break
        else:
            print (Fore.RED+"this not is a IPv4")
            points=3
            exit(0)
    
    
    ALL = "Y"       
    if(ALL == "Y"):
        port = [1,7,9,13,17,19,20,21,22,23,25,37,43,53,67,68,69,70,79,80,88,110,111,113,119,123,135,137,138,139,143,161,162,177,389,443,445,465,500,512,513,514,515,520,587,591,631,666,690,993,995,1080,1337,1352,1433,1434,1494,1512,1521,1701,1720,1723,1761,1863,1935,2049,2082,2083,2086,2427,3030,3074,3128,3306,3389,3396,3690,4662,4672,4899,5000,5060,5190,5222,5223,5269,5432,5517,5631,5632,5400,5500,5600,5700,5800,5900,6000,6112,6129,6346,6347,6348,6349,6350,6355,6667,6880,6969,7100,8000,8008,8080,8118,9009,9898,10000,19226,12345,25565,31337,45003]   
        length = len(port)
        print (Fore.CYAN+"Scanning...")
        for x in range(0, length):
            sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if sock.connect_ex((ip,port[x])):
                '''
                if(port[x] == 53 or port[x] ==67  or port[x] ==68 or port[x] ==69 or port[x] ==123 or port[x] ==161 or port[x] ==500 or port[x] ==514 or port[x] ==520 or port[x] ==1701 or port[x] ==1720 or port[x] ==2427 or port[x] ==3074 or port[x] ==4672 or port[x] ==5060 or port[x] ==5632 or port[x] ==6112 or port[x] ==6347 or port[x] ==6348 or port[x] ==6349 or port[x] ==6350 or port[x] ==6355 or port[x] ==7100 ):
                    print "The port "+str(port[x])+"/udp is close"
                elif(port[x] == 43):
                    print "The port "+str(port[x])+"/betocp is close"
                else:
                    print "The port "+str(port[x])+"/tcp is close"
             '''   
            else:
                if(port[x] == 53 or port[x] ==67  or port[x] ==68 or port[x] ==69 or port[x] ==123 or port[x] ==161 or port[x] ==500 or port[x] ==514 or port[x] ==520 or port[x] ==1701 or port[x] ==1720 or port[x] ==2427 or port[x] ==3074 or port[x] ==4672 or port[x] ==5060 or port[x] ==5632 or port[x] ==6112 or port[x] ==6347 or port[x] ==6348 or port[x] ==6349 or port[x] ==6350 or port[x] ==6355 or port[x] ==7100 ):
                    print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[x])+Fore.CYAN+"/udp is open")
                elif(port[x] == 43):
                    print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[x])+Fore.CYAN+"/betocp is open")
                else:
                    print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[x])+Fore.CYAN+"/tcp is open")
        print "[*] Was been scanned "+str(length)+" ports successfull."

def scanP(ip,ports):
    points=0
    print "\n--> Ports Scanner"
    while(points != 3):
        lengthip= len(ip)
        
        for i in range (0,lengthip):
            if (ip[i]=="."):
                points = points+1
        if(points==3):
            break
        else:
            print "this not is a IPv4"
            points=3
            exit(0)

    port = ports.split(",")
    print "Scanning..."
    for j in range(len(port)):
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex((ip,int(port[j]))):
            if(port[j] == 53 or port[j] ==67  or port[j] ==68 or port[j] ==69 or port[j] ==123 or port[j] ==161 or port[j] ==500 or port[j] ==514 or port[j] ==520 or port[j] ==1701 or port[j] ==1720 or port[j] ==2427 or port[j] ==3074 or port[j] ==4672 or port[j] ==5060 or port[j] ==5632 or port[j] ==6112 or port[j] ==6347 or port[j] ==6348 or port[j] ==6349 or port[j] ==6350 or port[j] ==6355 or port[j] ==7100 ):
                print (Fore.GREEN+"[-] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[j])+Fore.CYAN+"/udp is close")
            elif(port[j] == 43):
                print (Fore.GREEN+"[-] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[j])+Fore.CYAN+"/betocp is close")
            else:
                print (Fore.GREEN+"[-] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[j])+Fore.CYAN+"/tcp is close")
        else:
            if(port[j] == 53 or port[j] ==67  or port[j] ==68 or port[j] ==69 or port[j] ==123 or port[j] ==161 or port[j] ==500 or port[j] ==514 or port[j] ==520 or port[j] ==1701 or port[j] ==1720 or port[j] ==2427 or port[j] ==3074 or port[j] ==4672 or port[j] ==5060 or port[j] ==5632 or port[j] ==6112 or port[j] ==6347 or port[j] ==6348 or port[j] ==6349 or port[j] ==6350 or port[j] ==6355 or port[j] ==7100 ):
                print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[j])+Fore.CYAN+"/udp is open")
            elif(port[j] == 43):
                print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[j])+Fore.CYAN+"/betocp is open")
            else:
                print (Fore.GREEN+"[+] "+Fore.CYAN+"Port "+Fore.MAGENTA+str(port[j])+Fore.CYAN+"/tcp is open")
    exit(0)
