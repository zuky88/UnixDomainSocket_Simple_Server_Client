import socket
import os

class UnixSocket():
    def __init__(self, path, size) -> None:
        super().__init__()
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.path = path
        self.size = size
        self.conn = ''
        self.address = ''
    def check_socketfile(self):
        if os.path.exists(self.path):
            os.remove(self.path)
    def server_listen(self):
        self.s.bind(self.path)
        self.s.listen()
    def receive(self):
        try:
            self.conn, self.address = self.s.accept()
            data = self.conn.recv(self.size)
        except Exception as e:
            print('>UnixSocket(py3) receive error:{0}'.format(e))
        return data
    def client_send(self, data:list):
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            self.s.connect(self.path)
            self.s.send(bytes(data))
        except Exception as e:
            self.s.close()
