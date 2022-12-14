#!/bin/python3

import sys
from datetime import datetime
import socket

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])

else:
    print("Invalid syntax!")
    print("Usage: python3 crappy-port-scanner.py 192.168.1.2")

#Banner
print("-" * 50)
print("Scanning target:" + str(target))
print("Scanning started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in (20, 443):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        status = s.connect_ex((target, port))
        if status == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()
except socket.gaierror:
    print("\nCouldn't resolve hostname")
    sys.exit()
except socket.error:
    print("\nCouldn't connect to server")
    sys.exit()
except NameError:
    print("\nWrong target IP format")
    sys.exit()