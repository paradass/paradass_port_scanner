#Basic port scaner with python -Burak "paradass" Görez

import socket
import argparse

class Scaner:
    def __init__(self):
        self.general_ports = [0] * 1000
        self.general_ports[20] = "ftp"
        self.general_ports[21] = "ftp"
        self.general_ports[22] = "ssh"
        self.general_ports[23] = "telnet"
        self.general_ports[25] = "smtp"
        self.general_ports[53] = "dns"
        self.general_ports[67] = "dhcp"
        self.general_ports[68] = "dhcp"
        self.general_ports[69] = "tftp"
        self.general_ports[80] = "http"
        self.general_ports[110] = "pop3"
        self.general_ports[123] = "ntp"
        self.general_ports[137] = "net bios"
        self.general_ports[138] = "net bios"
        self.general_ports[139] = "net bios"
        self.general_ports[143] = "imap"
        self.general_ports[161] = "snmp"
        self.general_ports[162] = "snmp"
        self.general_ports[389] = "ldap"
        self.general_ports[443] = "https"
        self.general_ports[445] = "smb"
        self.general_ports[514] = "syslog"
        self.general_ports[587] = "smtp & tls"
        self.general_ports[993] = "imaps"
        self.general_ports[995] = "pop3s"

    def scan(self):
        parser = argparse.ArgumentParser(description="Socket port scaner by paradass",add_help=False)
        parser.add_argument("-t","--target",required=True,type=str,help="Set target")
        parser.add_argument("-r","--port_range",type=str,default="1000",help="Set port scan range")

        args = parser.parse_args()
        target:str = args.target
        _range:str = args.port_range
        ranges = []
        
        try:
            if "-" in _range:
                ranges = _range.split("-")
                ranges[0] = int(ranges[0])
                ranges[1] = int(ranges[1])
            else:
                ranges = [-1,-1]
                _range = int(_range)
        except:
            print("False port range!")
        
        threshold = [0,0]

        if ranges[0] == -1:
            threshold = [1,_range]
        else:
            threshold = ranges
        
        if threshold[1] > 65535:
            threshold[1] = 65535
            
        print("Finding tcp ports:")
        for i in range(threshold[0],threshold[1]):
                st = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                result = st.connect_ex((target,i))
                st.close()
                if result == 0:
                    if i > len(self.general_ports) or self.general_ports[i] == 0:
                        print(f"{i} unknown")
                    else:
                        print(f"{i} {self.general_ports[i]}")
                    

scaner = Scaner()
scaner.scan()