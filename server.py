from base64 import decode
from dataclasses import dataclass
import json
import socket
from unittest import result
from urllib import response

HOST="127.0.0.1"
PORT=65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
  server.bind((HOST, PORT))
  server.listen()
  conn, addr = server.accept()
  with conn:
    print(f"Connected by {addr}")
    while True:
      data = conn.recv(1024)
      if not data:
        break
      data_string = data.decode("ascii")
      data_json = json.loads(data_string)
      if data_json["method"] == 'echo':
        response = {
          "id": data_json["id"],
          "result": {
            "message": data_json["params"]["message"]
          }
        }
        conn.sendall(bytes(json.dumps(response), "ascii"))
      else:
        break
