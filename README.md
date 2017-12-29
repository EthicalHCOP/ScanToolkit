# ScanToolkit
*Is a toolkit capable to realize ports scan, host discover ,nslookup service, IPv4 Geolocation and Shodan Api*

```[javascript]
[First Configuration] Usage: setup.py 
Usage: toolkit.py -M <Menu option> <Option>

Menu
1. Local Host Discover.
2. Ports Scanner.
3. NSlookup Windows type=(A, ANY, CNAME, MX, NS, PTR, SOA, SRV).
4. IPv4 Geolocation.
5. Shodan Api.

Options:
  -h, --help                               Show this help message and exit
  -M MENUOPTION, --menu = MENUOPTION       Insert the number of option
  -P PARAMETER, --Parameters = PARAMETER   Insert parameters separated by comma
  -H HOST, --Host = HOST                   Insert parameters separated by comma
  -p PORT, --Port = PORT                   Insert parameters separated by comma
  -R RANGE, --Range = RANGE                Insert parameters separated by comma
  -Q Query, --Query = Query 			   Shodan Query
  
Examples:
  Host Discover:                 toolkit.py -M 1 -R <port_range>
  Port Scanner:  All ports       toolkit.py -M 2 -H <ip_address>
                 Specific ports  toolkit.py -M 2 -H <ip_address> -P <port>,<port>
  Nslookup:                      toolkit.py -M 3 -H <ip_address> -P A,ANY,CNAME,MX,NS,PTR,SOA,SRV
  IpGeolocation: MyIp Address    toolkit.py -M 4
                 Specific Ip     toolkit.py -M 4 -H <ip_address>
  Shodan Api     Search   		 toolkit.py -M 5 -Q "Query"
				 Host Scanner    toolkit.py -M 5 -H <ip_address>
```
