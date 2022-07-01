import socket

class Server():

    def __init__(self, HOST, PORT, PACKET_SIZE) -> None:
        self.HOST = HOST
        self.PORT = PORT
        self.PACKET_SIZE = PACKET_SIZE
        pass

    def startServer(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))
        self.socket.listen()

        conn, adress = self.socket.accept()
        
        f = open("./server/hi.txt", "rb")

        with conn:
            chunk = f.read(1024)
            while chunk:
                conn.sendall(chunk)
                chunk = f.read(1024)




server = Server("192.168.188.51", 5000, 1024)
server.startServer()

