from datetime import datetime
import socket
import re
import nmap
import os

x = datetime.day

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
local_ip_address = s.getsockname()[0]
ip = ".".join(re.split(r"\.", local_ip_address)[:3])

with open('discovery_file.txt' + str(x), 'w') as log_nmap:
    for i in range(1, 255, 1):
        nm = nmap.PortScanner()
        host = (str(ip) + "." + str(i))
        response = os.system('ping -c1' + host)
        if response != 1:
            scan = nm.scan(host, ports=all, arguments='-P0')
            log_nmap.write(scan + '\n')
