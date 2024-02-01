import socket
serv = ('127.0.0.1', 12345)
HOST, PORT = serv[0], serv[1]
s = socket.socket()
name = input(str("\nenter your name: "))
print("trying to connect to ", HOST, "(", PORT, ")\n")
s.connect(serv)
print("connected\n")
s.send(name.encode())
s_name = s.recv(1024).decode()
print(s_name, "has connected to the chat room")
print("\nenter 'bye' to exit chat room\n")
while True:
    msg = str(input("me: "))
    if msg == "bye":
        print("left chat room")
        s.send(msg.encode())
        print("\n")
        s.close()
        break
    s.send(msg.encode())
    msg = s.recv(1024).decode()
    if(msg=='bye'):
        print("exit initiated by server")
        s.close()
        break
    print(s_name, ":", msg)
