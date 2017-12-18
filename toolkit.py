import scanning
import netscan
import nslookup
import optparse
import banners
import geoip


from socket import *
from threading import *
def toolkit():
    parser = optparse.OptionParser('usage %prog '+\
		'-M <Menu option> -P <Parameters>')
    parser.add_option('-M','--menu', dest='MenuOption', type='string', \
		help='|Insert the number of option')
    parser.add_option('-P','--Parameters', dest='parameter', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-H','--Host', dest='host', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-p','--Port', dest='port', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-R','--Range', dest='range', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-C', dest='command', type='string', \
		help='ScanToolkit commands')
    
    (options, args) = parser.parse_args()
    Moption = options.MenuOption
    if (Moption == "1"):
        parameters= str(options.range).split(",")
        if parameters[0] != "None":   
            try:
                banners.randomBanner()
                netscan.netscanOPT(int(parameters[0]),int(parameters[1]))
            except Exception, e:
                print str(e)
            exit(0)
        else:
            try:
                banners.randomBanner()
                netscan.netscanOPT(1,255)
            except Exception, e:
                print str(e)
            exit(0)
    elif(Moption == "2"):
        host = str(options.host)
        ports = str(options.port)      
        if ports != "None":
            try:
                banners.randomBanner()
                scanning.scanP(host,ports)
            except Exception, e:
                print str(e)
        else:
            try:
                banners.randomBanner()
                scanning.scan(host)
            except Exception, e:
                print str(e)
        exit(0)
    elif(Moption == "3"):
        parameters= str(options.parameter)
        host = str(options.host)
        try:
            banners.randomBanner()
            nslookup.nslookupscanOPT(parameters,host)
        except Exception, e:
            print str(e)
        exit(0)
    elif(Moption == "4"):
        host = str(options.host)
        if host != "None":
            try:
                banners.randomBanner()
                geoip.remoteIpOPT(host)
            except Exception, e:
                print str(e)
        else:
            try:
                banners.randomBanner()
                geoip.myIpOPT()
            except Exception, e:
                print str(e)
        exit(0)
    elif(Moption == "Help" or Moption == "HELP" or Moption == "help"):
        sos()
        exit(0)

    banners.randomBanner()
    print "\nMenu"
    print "1. Local Host Discover."
    print "2. Ports Scanner."
    print "3. NSlookup Windows."
    print "4. IPv4 Geolocation."

    menu = raw_input("Option: ")
    if(menu=="1"):
        netscan.netscan()
    elif(menu=="2"): 
        scanning.scanNA()
    elif(menu=="3"):
        nslookup.nslookupscan()
    elif(menu=="4"):
        geoip.GeoIp()
    elif(menu=="Exit" or menu=="EXIT" or menu=="exit"):
        exit(0)

def sos():
    banners.randomBanner()
    print "[*] Menu"
    print "\t1. Local Host Discover."
    print "\t2. Ports Scanner."
    print "\t3. NSlookup Windows."
    print "\t4. IPv4 Geolocation."
    print "[*] Options:"
    print "\t-M --menu <Menu Option> \n\t-P --Parameters <Parameters> \n\t-H --Host <dns/host/IPv4> \n\t-p --Port <port> \n\t-R --Range <range>"
    print "[*] Examples:"
    print "\t-- Local Host Discover\n\t\ttoolkit.py -M 1 -R <range hosts> "
    print "\t-- Ports Scanner\n\t\tAll ports\ttoolkit.py -M 2 -H <ip_address>"
    print "\t\tSpecific ports\ttoolkit.py -M 2 -H <ip_address> -P <port>,<port>"
    print "\t-- Nslookup \n\t\ttoolkit.py -M 3 -H <DNS> -P A,ANY,CNAME,MX,NS,PTR,SOA,SRV"
    print "\t-- IpGeolocation\n\t\tMyIp Address\ttoolkit.py -M 4 "
    print "\t\tSpecific Ip\ttoolkit.py -M 4 -H <ip_address>"
    
if __name__ == '__main__':
	toolkit()
