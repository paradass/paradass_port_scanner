#Basic port scaner with python -Burak "paradas" Görez

import socket
import argparse

class Scaner:

    def __init__(self):
        self.set_program()

    @staticmethod
    def scan(target_ip):
        print("Open ports:")
        for port in range(1,1025):
                try:
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    result = s.connect_ex((target_ip,port))
                    if result == 0:
                        print(f"{port}")
                except:
                    pass

    def set_program(self):
        parser = argparse.ArgumentParser(description="Basic port scaner")
        parser.add_argument("-t","--target",type=str,help="Target ip adress",required=True)
        args = parser.parse_args()

        print(f"Target: {args.target}")
        self.scan(args.target)


scaner = Scaner()