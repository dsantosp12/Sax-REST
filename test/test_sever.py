import socket
import json

s = socket.socket()
s.bind(("127.0.0.1", 4028))
s.listen()

while True:
    conn, addr = s.accept()

    msg = conn.recv(1024)

    print("Server got: {}".format(msg.decode()))

    conn.send("{}".format(json.dumps(
        {
            "Time": "Test"
        }
    )).encode())
