import socket as s


discon_msg = "DISCONNECT"
HEADER = 64
FORMAT = "utf-8"
PORT = 	int(input("[ENTER SERVER PORT]: "))
SERVER = input("[ENTER SERVER IP:] ")
ADDR = (SERVER,PORT)


client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
	message = msg.encode(FORMAT)
	send_len = str(len(message)).encode(FORMAT)
	send_len += b' ' * (HEADER - len(send_len))
	client.send(send_len)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))


while True:
	n = input("YOU: ")
	if n == discon_msg:
		send(discon_msg)
		break
	else:
		send(n)
