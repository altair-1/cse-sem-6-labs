import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_host = '127.0.0.1'
udp_port = 9991
msg = 'hi'
s.sendto(msg.encode(),(udp_host,udp_port))
tm = s.recv(1024)
print('current time from server: ', tm.decode())
s.close()
