#!/usr/bin/env python3
import sys
import socket
from datetime import datetime as dt
import pyfiglet

ascii_banner = pyfiglet.figlet_format("HOST UP OR NOT ")
print(ascii_banner)

RIP    = input("Enter a remote host to scan: ")
TARGET  = socket.gethostbyname(RIP)

# some totally useless thing 
print ("-" * 40)
print ("Your target is been scaned ", TARGET)
print ("-" * 40)

time1 = dt.now()

# just setting the range till where it can scan you can even increase the value 
try:
    for port in range(1,10000):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((TARGET, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))

except KeyboardInterrupt:
    print ("Oh No stopping the scan ")
    sys.exit()

except socket.gaierror:
    print ('I guess there is some probleme with hostname ')
    sys.exit()

except socket.error:
    print ("I am unable to connect to the server maybe server is down")
    sys.exit()

# Checking the time again
time2 = dt.now()

# nothing much is happening here its just checking how much your time is wasted by running this bad script
total =  time2 - time1

print ('HOOHHO YOUR SCAN IS COMPLETED ', total)
print ("you can check me on twitter @Hac78040354")

