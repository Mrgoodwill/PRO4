import paramiko
import time
import socket

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the SSH server
connected = False
while not connected:
    try:
        ssh.connect("paramiko_server", username='username', password='password', port=2222)
        connected = True
    except paramiko.ssh_exception.NoValidConnectionsError:
        print("Failed to connect, waiting for 5 seconds before retrying...")
        time.sleep(5)

# Execute a command on the server
stdin, stdout, stderr = ssh.exec_command('ls')

# Set the timeout
stdout.channel.settimeout(2.0)

# Read and print the output of the command
try:
    while True:
        line = stdout.channel.recv(1024).decode()
        if not line:
            break
        print(line, end='')
except socket.timeout:
    print("No more data.")


# Countdown and automatic disconnection
countdown = 15
while countdown > 0:
    print(f"{countdown} seconds until the connection terminates")
    time.sleep(1)
    countdown -= 1

# Close the session and the channel
stdout.channel.close()
stdin.close()

# Close the SSH connection
ssh.close()
