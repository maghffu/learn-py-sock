# echo-client.py

import socket
import json

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    reqData = {"id": 42, "method": "echo", "params": {"message": "Hello"}}
    data_string = json.dumps(reqData)
    s.sendall(bytes(data_string, 'ascii'))
    data = s.recv(1024)

print(f"Received {data!r}")