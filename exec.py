# Execute a command on your local machine (e.g., list the files in the project directory)
project_dir = "path/to/your/project"
stdin, stdout, stderr = ssh.exec_command(f"ls {project_dir}")

# Print the output of the command
for line in stdout.readlines():
    print(line.strip())

# Close the connection
ssh.close()
