Attack01 


#Auto Add Policy Vulnerability - SSH



setupAttack01 starts a docker container where you got 3 network participants. The real 
server, the client and the attacker. The attacker accepts every username/password combination. 
You can start the script by running this command: 

sudo ./setupAttack01
Now you created 3 Docker Containers which you can access by the following commands

sudo docker exec -it paramiko_server bash
sudo docker exec -it paramiko_client bash
sudo docker exec -it paramiko_attacker bash 

To start the scripts within the containers use:

python3 server.py
python3 client.py
python3 attacker.py

Note that you always have to start the server/attacker script before the client script. 

First test wether the client can connect to the server. Therefore enter the paramiko_server and client
container and start the server and afterwards the client. 


Moving on the the actual attack you have to change the setup script. Look for this line in the 
client script: 
ssh.connect("paramiko_server", username='username', password='password', port=2222)

and change it to: 
ssh.connect("paramiko_attacker", username='username', password='password', port=2223)

Safe the file and start the script again: 
sudo ./setupAttack01

Enter the paramiko_attacker and paramiko_client container and repeat the steps like before with
the actual server.
The server should print out on the client side: This is the Attacker Server.

In a real life attack the attacker would obviously not change the IP the client connects to 
but would perform are MitM attack with ARP Spoofing(Not possible in docker environment).

