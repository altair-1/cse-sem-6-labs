import socket
HOST = '127.0.0.1'
PORT = 31621 # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("\nwaiting for incoming connections\n")
data,addr = s.recvfrom(1024)
print("received connection from ", addr[0], "(", addr[1], ")\n")
s_name, addr = s.recvfrom(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\n")
print("enter [e] to exit chat room\n")
name = input(str("enter your name: "))
s.sendto(name.encode('ascii') , addr)
while True:
    msg = input(str("enter message: "))
    if msg == "[e]":
        msg = "left chat room"
        s.sendto(msg.encode() , addr)
        print("\n")
        break
    s.sendto(msg.encode() , addr)
    msg, addr = s.recvfrom(1024)
    msg = msg.decode()
    print(s_name, ":", msg)
