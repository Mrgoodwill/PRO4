# ssh_client.py
import paramiko

# Update these variables with your server's IP and port
HOST = '127.0.0.1'
PORT = 2222

# Update these variables with the same username and password as the server
USERNAME = 'your_username'
PASSWORD = 'your_password'

def ssh_client_connection():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh_client.connect(HOST, PORT, USERNAME, PASSWORD)
    print(f'Successfully connected to {HOST}:{PORT}')

    stdin, stdout, stderr = ssh_client.exec_command("echo 'Hello, Paramiko!'")
    print('Output of the command:')
    print(stdout.read().decode('utf-8'))

    ssh_client.close()

if __name__ == '__main__':
    ssh_client_connection()
