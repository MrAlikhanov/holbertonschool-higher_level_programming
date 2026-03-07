#!/usr/bin/env python3
import socket
import json

HOST = '127.0.0.1'
PORT = 65432


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        conn, addr = server_socket.accept()
        with conn:
            chunks = []
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                chunks.append(data)

            raw = b''.join(chunks)
            dictionary = json.loads(raw.decode('utf-8'))

            print("Received Dictionary from Client:")
            print(dictionary)
