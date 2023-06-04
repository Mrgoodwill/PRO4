import paramiko
import socket
import threading
import subprocess

class SSHServer (paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'username') and (password == 'password'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

    def check_channel_exec_request(self, channel, command):
        output = subprocess.check_output(command, shell=True)
        channel.send(output)
        channel.send_exit_status(0)
        return True


ssh_host = "0.0.0.0"
ssh_port = 2222
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_server.bind((ssh_host, ssh_port))
sock_server.listen(100)

print('Server started. Waiting for connections...')

while True:
    client, addr = sock_server.accept()
    print(f'Got a connection from {addr}.')
    transport = paramiko.Transport(client)
    transport.add_server_key(paramiko.RSAKey(filename='test_rsa.key'))
    ssh_server = SSHServer()
    try:
        transport.start_server(server=ssh_server)
        print('SSH negotiation started.')
    except paramiko.SSHException:
        print('SSH negotiation failed.')
        continue
    chan = transport.accept(20)
    print('Channel accepted.')
    chan.send("This is the real server.\n")

