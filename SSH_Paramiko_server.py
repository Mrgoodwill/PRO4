# ssh_server.py
import socket
import paramiko
import threading

# Update these variables with your server's IP and port
HOST = '127.0.0.1'
PORT = 2222

# Update these variables with the desired username and password
USERNAME = 'your_username'
PASSWORD = 'your_password'

class Server(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        if username == USERNAME and password == PASSWORD:
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

def handle_client(client_socket):
    transport = paramiko.Transport(client_socket)
    transport.add_server_key(paramiko.RSAKey.generate(1024))
    transport.start_server(server=Server())

    channel = transport.accept(20)
    if channel is not None:
        channel.exec_command("echo 'Hello, Paramiko!'")

    transport.close()

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f'Listening for connections on {HOST}:{PORT}')

    while True:
        client_socket, addr = server.accept()
        print(f'Connection from {addr}')
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
