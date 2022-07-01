import socket
import pickle


class Server():
    HOST = ""
    PORT = 5000
    PACKET_SIZE = 1024
    socket = None

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

        with conn:
            pass

