import socket
# Import socket module
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host = '172.16.59.52' # Host IP
udp_port = 12345
# specified port to connect
msg = "UDP Program third time!"
print('UDP target IP:', udp_host)
print('UDP target Port:', udp_port)
sock.sendto(msg.encode(),(udp_host,udp_port))
sock.sendto(msg.encode(),(udp_host,udp_port))
sock.close()
