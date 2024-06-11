import socket as s
import threading as t
import ollama


def check_service_running(host, port):
    try:
        with s.create_connection((host, port), timeout=2):
            return True
    except (s.timeout, ConnectionRefusedError, OSError):
        print(f"Ollama not running")
        return False

if check_service_running('localhost', 11434): pass
else: exit()

def response(msg):  
  messages = [
    {
      'role': 'user',
      'content': msg,
    },
  ]
  response = ollama.chat('<model_name>', messages=messages)
  return response['message']['content']

def get_network_ip():
    so = s.socket(s.AF_INET, s.SOCK_DGRAM)
    so.connect(("8.8.8.8", 80))
    ip_address = so.getsockname()[0]
    so.close()
    return ip_address

discon_msg = "DISCONNECT"

HEADER = 64
FORMAT = "utf-8"

PORT = int(input("[ENTER HOSTING PORT]: "))
SERVER = get_network_ip()
ADDR = (SERVER,PORT)

server = s.socket(s.AF_INET, s.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected")
	connected = True
	while connected:
		msg_len = conn.recv(HEADER).decode(FORMAT)
		if msg_len:
			msg_len = int(msg_len)
			msg = conn.recv(msg_len).decode(FORMAT) #blocking statement
			if msg == discon_msg:
				connected = False
			
			print(f'{addr} {msg}')
			res = response(msg)
			conn.send(res.encode(FORMAT))
			
	conn.close()

def start():
	server.listen()
	print(f"[LISTENING] server is listening on {SERVER}")
	while True:
		conn, addr = server.accept() # blockling statement
		thread = t.Thread(target=handle_client, args=(conn,addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {t.active_count() -1 }") 
		
print("[STARTING] server is starting...")
start()


