import paramiko
import sys

def ssh_connection(hostname, port, username, password):
    try:
        # Create a new SSH client
        ssh_client = paramiko.SSHClient()

        # Automatically add the server's public key (this is insecure and should be done with caution)
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Establish the SSH connection
        ssh_client.connect(hostname, port, username, password)

        print(f'Successfully connected to {hostname}')

        # Execute a command on the remote server and fetch its output
        stdin, stdout, stderr = ssh_client.exec_command('uname -a')
        print('Output of the command:')
        print(stdout.read().decode('utf-8'))

        # Close the SSH connection
        ssh_client.close()

    except paramiko.AuthenticationException:
        print('Authentication failed. Please check your username and password.')
    except paramiko.SSHException as ssh_exception:
        print(f'SSH error: {ssh_exception}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('Usage: python ssh_connection.py hostname port username password')
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])
    username = sys.argv[3]
    password = sys.argv[4]

    ssh_connection(hostname, port, username, password)
