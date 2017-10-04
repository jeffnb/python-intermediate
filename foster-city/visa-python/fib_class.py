import socket
from threading import Thread


class Server(Thread):

    def __init__(self, conn):
        super().__init__()
        self._conn = conn

    def run(self):
        conn.send(str.encode("Welcome, type your info\n"))

        while True:
            data = conn.recv(2048)
            if not data:
                break
            reply = "Server output: " + data.decode("utf-8")
            conn.sendall(str.encode(reply))
        conn.close()


host = ""
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((host, port))
except socket.error as e:
    print(str(e))

sock.listen(5)
print("Waiting for connection")

while True:
    conn, addr = sock.accept()
    print("connected to:" + addr[0] + ":" + str(addr[1]))

    t_server = Server(conn)
    t_server.start()