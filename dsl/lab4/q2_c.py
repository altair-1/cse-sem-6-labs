import socket
# Port to listen on (non-privileged ports are > 1023)
serv = ('127.0.0.1', 31621)
HOST, PORT =  serv[0], serv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
name = input(str("\nenter your name: "))
print("\ntrying to connect to ", HOST, "(", PORT, ")\n")
s.sendto(b"" , serv)
print("connected\n")
s.sendto(name.encode('ascii') , serv)
s_name = s.recv(1024).decode()
print(s_name, "has connected to the chat room\n")
print("enter [e] to exit chat room\n")
while True:
    msg, addr = s.recvfrom(1024)
    msg = msg.decode()
    print(s_name, ":", msg)
    msg = input(str("enter message: "))
    if msg == "[e]":
        msg = "left chat room"
        s.sendto(msg.encode() , serv)
        print("\n")
        break
    s.sendto(msg.encode() , serv)
