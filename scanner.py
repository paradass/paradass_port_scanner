#Basic port scanner with python -Burak "paradass" Görez

import socket
import argparse

class Scanner:
    def __init__(self):
        self.general_ports = {
            20: "ftp",
            21: "ftp",
            22: "ssh",
            23: "telnet",
            25: "smtp",
            53: "dns",
            67: "dhcp",
            68: "dhcp",
            69: "tftp",
            80: "http",
            110: "pop3",
            123: "ntp",
            137: "net bios",
            138: "net bios",
            139: "net bios",
            143: "imap",
            161: "snmp",
            162: "snmp",
            389: "ldap",
            443: "https",
            445: "smb",
            514: "syslog",
            587: "smtp & tls",
            993: "imaps",
            995: "pop3s"
        }

    def scan(self):
        parser = argparse.ArgumentParser(description="Socket port scanner by paradass",add_help=False)
        parser.add_argument("-t","--target",required=True,type=str,help="Set target")
        parser.add_argument("-r","--port_range",type=str,default="1000",help="Set port scan range")
        args = parser.parse_args()
        
        try:
            if "-" in args.port_range:
                start,end = map(int, args.port_range.split("-"))
            else:
                start,end = (0,int(args.port_range))
        except:
            print("Invalid port range!")

        end = min(end,65535)
            
        print("Finding TCP ports:")
        for i in range(start,end):
                st = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                result = st.connect_ex((args.target,i))
                st.close()
                if result == 0:
                    service = self.general_ports.get(i,"unknown")
                    print(f"{i} {service}")
                    

scanner = Scanner()
scanner.scan()