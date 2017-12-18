# ScanToolkit
*Is a toolkit capable to realize ports scan, host discover ,nslookup service and IPv4 Geolocation*

```[javascript]
Usage: toolkit.py -M <Menu option> <Option>

Menu
1. Local Host Discover
2. Ports Scanner
3. NSlookup Windows type=(A, ANY, CNAME, MX, NS, PTR, SOA, SRV)
4. IPv4 Geolocation

Options:
  -h, --help                               Show this help message and exit
  -M MENUOPTION, --menu = MENUOPTION       Insert the number of option
  -P PARAMETER, --Parameters = PARAMETER   Insert parameters separated by comma
  -H HOST, --Host = HOST                   Insert parameters separated by comma
  -p PORT, --Port = PORT                   Insert parameters separated by comma
  -R RANGE, --Range = RANGE                Insert parameters separated by comma
  
Examples:
  Host Discover:                toolkit.py -M 1 -R <port_range>
  Port Scanner: All ports       toolkit.py -M 2 -H <ip_address>
                Specific ports  toolkit.py -M 2 -H <ip_address> -P <port>,<port>
  Nslookup:                     toolkit.py -M 3 -H <ip_address> -P A,ANY,CNAME,MX,NS,PTR,SOA,SRV
  IpGeolocation:
                MyIp Address    toolkit.py -M 4
                Specific Ip     toolkit.py -M 4 -H <ip_address>
```
