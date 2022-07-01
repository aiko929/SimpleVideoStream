import socket


HOST = "92.116.29.26"
PORT = 5000


PACKET_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(PACKET_SIZE)

print(f"Received {data!r}")



    

# f = pickle.load(data)


# f = f.save("cat.png")

f = open("./backend/test.txt", "wb")
f.write(data)
f.close()