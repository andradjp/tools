import socket

HOST = '10.1.6.45'
PORT = 10515

def send(data):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dados = str(data).encode('ascii')
        sock.sendto(dados, (HOST, PORT))
    except Exception as e:
        print(e)


