import paramiko

def create_ssh_connection(hostname, port, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    return ssh

# Use "localhost" or "127.0.0.1" as the hostname to connect to the local SSH server
hostname = "localhost"
port = 22
username = "Username"
password = "Password"

# Create a connection
ssh = create_ssh_connection(hostname, port, username, password)
