import paramiko

# Create an SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # This is to automatically add the server's SSH key (Not recommended in production)

# Connect to the SSH server
ssh.connect('localhost', username='username', password='password', port=2222)

# Execute a command on the server
stdin, stdout, stderr = ssh.exec_command('ls')

# Print the output of the command
print(stdout.read().decode())

# Close the session and the channel
stdout.channel.close()
stdin.close()

# Close the SSH connection
ssh.close()
