## SUMMIT ##


**Challenge Overview**

Examine 'samples' received from the Sphinx, from the pentesting team, and apply the appropriate response to block the malware 
---
**Objective**

After participating in one too many incident response activities, PicoSecure has decided to conduct a threat simulation and detection engineering engagement to bolster its malware detection capabilities. You have been assigned to work with an external penetration tester in an iterative purple-team scenario. The tester will be attempting to execute malware samples on a simulated internal user workstation. At the same time, you will need to configure PicoSecure's security tools to detect and prevent the malware from executing.

Following the Pyramid of Pain's ascending priority of indicators, your objective is to increase the simulated adversaries' cost of operations and chase them away for good. Each level of the pyramid allows you to detect and prevent various indicators of attack.

---
**Skills applied**

- Problem solving
- Manage firewall rules
- Manage DNS filters
- Creating custom rules

---
**Flag**

1. THM{f3cbf08151**********************}

Observations: After examining 'Sample 1' within the 'Maware Sandbox' it is tagged as 'Troja.Metasploit.A'.  Further down it provided 3 different HASH Types

a. MD5	cbda8ae000aa9cbe7c8b982bae006c2a

b. SHA1	83d2791ca93e58688598485aa62597c0ebbf7610

c. SHA256	9c550591a25c6228cb7d74d970d133d75c961ffed2ef7180144859cc09efca8c

Within the tools available on the VM, there is a 'Manage Hashes' tool. This is going to be used to mitigate 'Sample 1'. 

Method: taking one of the HASH values, i used cbda8ae000aa9cbe7c8b982bae006c2a, and pasted it into the free text box and ensured MD5 is selcted, after submission a emial is recieved with the first flag

---
2.THM{2ff48a3421**********************}

Observations: Within 'Sample 2' There is both HASH value and now we have internet connections the tag of the file is 'Troja.Metasploit.A'. Main thing i notice if the HTTP GET request being made. This is likely to be vector requiring to be blocked along with the HASH Value. Whe attempting to submit the HASH Value, the response directs you to tray another method, resulting in another tool being considered.

The offending IP in the GET Request is 	154.35.10.113:4444 (IP:154.35.10.113 on Port:4444) 

Method: Within theFirewall rule manager, i am met with 4 fields to fill. the following was selected;

Type: Egress (To prevent outbound traffic)

Source IP: Any (To apply to all users on my network)

Destination IP:154.35.10.113 (Malicious IP)

Action: Deny (to prevent access)

---
3. THM{4eca9e2f61**********************}

Observations: 'Sample 3' provides both HASH values and HTTP GET requests as before, however this time there is the inclusion of DNS. Following the attempt within Flag 2, i am going to apply the rule on the 'DNS Filter'. Within the DNS requests there is two DNS accessed

a. services.microsoft.com

b. emudyn.bresonicz.info

Whilst on initial glance i lean towards 'emudyn.bresonicz.info' being the malicious link. To verify, this i am going to review the HTTP Requests, i can see the GET requests were made to 62.123.140.9 on both ports 1337 and 80 which resovle to an .exe and apparent sub domain within emudyn.bresonicz.info

On the DNS Rule manager the following ws entered;

Rule Name: Malware_Site

Category: Malware

Domain Name: emudyn.bresonicz.info

Action: Deny

---
4. THM{c956f455fc**********************}

Observations: 'Sample 4' provides HASH Values, HTTP GET Requests and DNS requests, there is now a inclusion of Registry Activity. Smaple 4 which is our testing malware as disabled out Windows defender.

There is 3 events witihn the Registry, however there is one which causes issue due to the proccess accessed.

(PID) Process: (3806) sample4.exe	

Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection

Operation: write	

Name: DisableRealtimeMonitoring

Method: Within the Sigma Rule Builder, i accessed 'Sysmon Event Logs' which manges Windows System Services, which Windowws Defender belongs. I then selected 'Registry Modifications' as there is a chnage to our registry. For the Rule i applied the following;

Registry Key: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection (This is what was changed)

Registry Name:DisableRealtimeMonitoring (The associated name to the registry)

Value: 1 (1= On)

ATT&CK ID: DEFENSE EVASION (TA0005) (This is the ATT&CK ID from MITRE) 

---
5. THM{46b21c4410**********************}

Observations: On the email there is an different file to the 'Sample' which is called 'outgoing_connections.log' Extract below (first 4 row);

2023-08-15 09:00:00 | Source: 10.10.15.12 | Destination: 51.102.10.19 | Port: 443 | Size: 97 bytes
2023-08-15 09:23:45 | Source: 10.10.15.12 | Destination: 43.10.65.115 | Port: 443 | Size: 21541 bytes
2023-08-15 09:30:00 | Source: 10.10.15.12 | Destination: 51.102.10.19 | Port: 443 | Size: 97 bytes
2023-08-15 10:00:00 | Source: 10.10.15.12 | Destination: 51.102.10.19 | Port: 443 | Size: 97 bytes

Within this there is a series connections all from IP 10.10.15.12, the location vary, however one repeats at 30 min intervals. This is 51.102.10.19 over Port 443 sending 97 bytes. Which is unusual, so an inspection of 'Sample 5' is required. 

Within the Network Activity, i can see a series of POST requests to 51.102.10.19:443 (IP: 51.102.10.19 Port:443), the IP matches the connections Log. 

On the Sigma Rule Builder, within the Sysmons Event Logs there is a Network Connections where the following rules was applied

Remote IP: Any (Origionally i typed 51.102.10.19, which was an incorrect value to retrive the flag, after reviewing the Email for this Flag i noticed 'so I can easily change the types of protocols' this prompted me to change to rule to apply to a wider net, hence Any)

Remote Port: Any (As above)

Size: 97 bytes (tThis remained constnat)

Frequency: 1800 (30 min in seconds)

ATT &CK ID: Command and Control (C2) 

---
6. THM{c8951b2ad2**********************}

Observations: Within the email received there is a file tiltled  'Commands.Log' within it is the following;

dir c:\ >> %temp%\exfiltr8.log
dir "c:\Documents and Settings" >> %temp%\exfiltr8.log
dir "c:\Program Files\" >> %temp%\exfiltr8.log
dir d:\ >> %temp%\exfiltr8.log
net localgroup administrator >> %temp%\exfiltr8.log
ver >> %temp%\exfiltr8.log
systeminfo >> %temp%\exfiltr8.log
ipconfig /all >> %temp%\exfiltr8.log
netstat -ano >> %temp%\exfiltr8.log
net start >> %temp%\exfiltr8.log

Looking at this, it appears as though files are being extracted and stored into a file named 'exfiltr8.log' 
(Breakdown ex 'systeminfo' = interprets system infor, '>>' = gets the info and sends it to a location, '%temp%' the extracted dats is sent to the %temp% folder, where the data is stored in a file called 'exfiltr8.log'

Within the sample 6 is file activity namely Dropped Files using cmd.exe %temp%\exfiltr8.log is created.

Within the Sigma Rule Builder, and the Sysmons Event Logs is File Creation and Modification where the following rule was applied;

File Path: %temp% (prevents action within the folder)

Filename: exfiltr8.log (prevents action within file)

ATT&ID: Extraction

