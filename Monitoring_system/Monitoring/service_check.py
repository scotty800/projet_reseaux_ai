import socket

host = "example.com"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

try:
    sock.connect((host, port))
    print("Service UP")
except:
    print("Service DOWN")

sock.close()
    