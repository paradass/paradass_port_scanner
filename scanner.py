#Basic port scanner with python -Burak "paradass" Görez

import socket
import argparse

class Scanner:
    def __init__(self):
        self.general_ports = {
            20: "ftp-data",
            21: "ftp",
            22: "ssh",
            23: "telnet",
            25: "smtp",
            53: "dns",
            67: "dhcp (server)",
            68: "dhcp (client)",
            69: "tftp",
            80: "http",
            110: "pop3",
            119: "nntp",
            123: "ntp",
            135: "msrpc",
            137: "netbios-ns",
            138: "netbios-dgm",
            139: "netbios-ssn",
            143: "imap",
            161: "snmp",
            162: "snmp-trap",
            179: "bgp",
            389: "ldap",
            443: "https",
            445: "smb",
            465: "smtps",
            514: "syslog",
            515: "printer (lpd)",
            520: "rip",
            546: "dhcpv6-client",
            547: "dhcpv6-server",
            587: "smtp (submission)",
            636: "ldaps",
            873: "rsync",
            902: "vmware",
            989: "ftps-data",
            990: "ftps",
            993: "imaps",
            995: "pop3s",
            1080: "socks",
            1433: "mssql",
            1434: "mssql-monitor",
            1521: "oracle",
            1701: "l2tp",
            1723: "pptp",
            2049: "nfs",
            2082: "cpanel",
            2083: "cpanel (ssl)",
            2181: "zookeeper",
            2375: "docker api",
            2376: "docker api tls",
            3306: "mysql",
            3389: "rdp",
            3690: "svn",
            4444: "metasploit",
            4650: "isdn",
            5000: "unpn / flask-dev",
            5432: "postgresql",
            5672: "rabbitmq",
            5900: "vnc",
            5984: "couchdb",
            6379: "redis",
            6667: "irc",
            8000: "http-alt",
            8080: "http-proxy",
            8081: "http-alt",
            8443: "https-alt",
            8888: "http-alt / proxy",
            9000: "sonar / php-fpm",
            9200: "elasticsearch",
            11211: "memcached",
            27017: "mongodb",
            27018: "mongodb",
            50000: "sap"
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