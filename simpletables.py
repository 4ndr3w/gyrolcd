import socket
import struct
import threading

MCAST_GRP = '225.225.225.225'
MCAST_PORT = 2225
data = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

def worker():
    while True:
        incoming = sock.recv(256).split("~")
        if len(incoming) == 2:
            data[incoming[0]] = incoming[1]

def set(key,value):
    data[key] = value
    sock.sendto(key+"~"+value, (MCAST_GRP, MCAST_PORT))

def get(key, default):
    if key in data:
    	return data[key]
    else:
	return default

thread = threading.Thread(target=worker)
thread.daemon = True
thread.start();

