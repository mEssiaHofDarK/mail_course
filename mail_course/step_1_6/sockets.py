import os
import socket
import threading


def server(conn):
    while True:
        data = conn.recv(1024)
        if not data or data.decode() == 'close':
            break
        conn.send(data)
    conn.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    t = threading.Thread(target=server, args=(conn,))
    t.start()
