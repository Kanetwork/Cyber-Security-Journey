## Wireshark guide

## useful commands

| Filter Command | What It Does | Why use it?|
| :--- | :--- | :--- |
| ip.addr == xxx.xxx.xxx.xxx | Shows everything involving this IP. | To focus on the "Victim" or the "Attacker" only. |
| ip.src == 192.168.1.5 | Shows traffic coming FROM this IP. | What is the suspect sending out? (Commands? Stolen data?)|
| ip.dst == 192.168.1.5| Shows traffic going TO this IP. | Who is attacking the victim? |
| tcp.stream eq 5 | Follows a single conversation. | Reconstructs the entire chat/session from start to finish.|
| http.request.method == "POST" | Shows data being uploaded/sent. | Is the attacker stealing passwords or uploading files? |
| tcp.flags.syn == 1 | Shows attempts to start a connection. | If you see thousands of these quickly, it’s a Scan or Brute Force. | 
| dns | Shows website lookups. | Look for weird names (e.g., x894[.]malware[.]com). |
| frame.len > 500 | Shows packets larger than 500 bytes. | Malware commands are usually small. Big packets often mean Data Theft. |
| http | Web Traffic | Unencrypted web browsing. You can read everything!| 
| ssh | Secure Shell | Remote access to Linux. Encrypted, but you can see who is connecting. |
| ftp | File Transfer | Old school file sharing. Passwords are sent in plain text! |
| icmp | Ping | Used to check if a computer is alive. Too much of this = Suspicious. |
