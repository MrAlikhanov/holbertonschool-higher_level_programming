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


def send_data(dictionary):
    try:
        serialized = json.dumps(dictionary).encode('utf-8')

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            client_socket.sendall(serialized)

    except ConnectionRefusedError:
        print("Error: Could not connect to the server.")
    except Exception as e:
        print(f"An error occurred: {e}")
