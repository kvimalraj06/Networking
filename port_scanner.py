#necessary modules

import sys
import socket
from datetime import datetime

#To Handle Argument Error
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid number of arguments")

#Banner
print("Scanning on ip: {}".format(target))
print("Starting time: {}".format(datetime.now()))

#checking the ports

try:
    for p in range(1, 65535):
        connect_create = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        connect_result = connect_create.connect_ex((target, p))

        if connect_result == 0:
            print("port {} is open".format(p))
            connect_create.close()
        """else:
            print("port {} is closed".format(p))
            connect_create.close()"""

except KeyboardInterrupt:
    print("\n exiting program")
    sys.exit()
except socket.gaierror:
    print("Host can't be resolved")
    sys.exit()
except socket.error:
    print("can't connect to the server")
    sys.exit()