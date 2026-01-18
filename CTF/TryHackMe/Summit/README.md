# SUMMIT — TryHackMe Write‑Up

## Challenge Overview
Examine the malware “samples” received from the Sphinx (the pentesting team) and apply the appropriate response to block the malware.

---

## Objective
PicoSecure is conducting a threat simulation and detection engineering engagement to strengthen its malware detection capabilities. You are working with an external penetration tester in a purple‑team scenario. The tester will attempt to execute malware samples on a simulated internal workstation, while you configure PicoSecure’s security tools to detect and prevent the malware.

Following the Pyramid of Pain, your goal is to increase the adversary’s operational cost by detecting and blocking indicators at progressively more difficult levels.

---

## Skills Applied
- Problem solving  
- Managing firewall rules  
- Managing DNS filters  
- Creating custom detection rules  

---

# Flag 1 — THM{f3cbf08151**********************}

### Observations
Sample 1 is tagged as **Trojan.Metasploit.A** in the Malware Sandbox. It provides three hash values:

- **MD5:** cbda8ae000aa9cbe7c8b982bae006c2a  
- **SHA1:** 83d2791ca93e58688598485aa62597c0ebbf7610  
- **SHA256:** 9c550591a25c6228cb7d74d970d133d75c961ffed2ef7180144859cc09efca8c  

The VM includes a **Manage Hashes** tool used to mitigate malicious files.

### Method
I submitted the MD5 hash (`cbda8ae000aa9cbe7c8b982bae006c2a`) using the Manage Hashes tool. After selecting MD5 and submitting, an email arrived containing the first flag.

---

# Flag 2 — THM{2ff48a3421**********************}

### Observations
Sample 2 again shows **Trojan.Metasploit.A**, but now includes network activity. The HTTP GET request reveals a malicious outbound connection to:

**154.35.10.113:4444**

Submitting the hash alone prompts a message suggesting another method is required — indicating a firewall rule is needed.

### Method
Using the Firewall Rule Manager:

- **Type:** Egress  
- **Source IP:** Any  
- **Destination IP:** 154.35.10.113  
- **Action:** Deny  

This blocks outbound traffic to the malicious IP.

---

# Flag 3 — THM{4eca9e2f61**********************}

### Observations
Sample 3 includes hashes, HTTP GET requests, and now DNS activity. Two domains appear:

- services.microsoft.com  
- emudyn.bresonicz.info  

Reviewing the HTTP requests shows connections to **62.123.140.9**, resolving to subdomains of *emudyn.bresonicz.info*, confirming it as malicious.

### Method
Using the DNS Filter:

- **Rule Name:** Malware_Site  
- **Category:** Malware  
- **Domain Name:** emudyn.bresonicz.info  
- **Action:** Deny  

---

# Flag 4 — THM{c956f455fc**********************}

### Observations
Sample 4 includes registry activity. The malware disables Windows Defender by modifying:

- **Process:** sample4.exe (PID 3806)  
- **Registry Key:** HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection  
- **Value Name:** DisableRealtimeMonitoring  
- **Operation:** Write  

### Method
Using the Sigma Rule Builder → Sysmon Event Logs → Registry Modifications:

- **Registry Key:** HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection  
- **Registry Name:** DisableRealtimeMonitoring  
- **Value:** 1  
- **ATT&CK ID:** Defense Evasion (TA0005)  

---

# Flag 5 — THM{46b21c4410**********************}

### Observations
The email includes **outgoing_connections.log**, showing repeated connections every 30 minutes:


Sample 5 confirms POST requests to **51.102.10.19:443**, which routinely occurse ever 30 mins and to the size of 97 bytes.

### Method
Using Sigma Rule Builder → Sysmon Event Logs → Network Connections:

- **Remote IP:** Any  
- **Remote Port:** Any  
- **Size:** 97 bytes  
- **Frequency:** 1800 seconds (30 minutes)  
- **ATT&CK ID:** Command and Control (C2)  

The hint in the email (“so I can easily change the types of protocols”) indicated the rule needed to be broad, not IP‑specific.

---

# Flag 6 — THM{c8951b2ad2**********************}

### Observations
The email includes **Commands.log**, containing:

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


This shows system information being collected and written to **exfiltr8.log** in the `%temp%` directory.

Sample 6 also shows file creation activity via `cmd.exe` at `%temp%\exfiltr8.log`.

### Method
Using Sigma Rule Builder → Sysmon Event Logs → File Creation and Modification:

- **File Path:** %temp%  
- **Filename:** exfiltr8.log  
- **ATT&CK ID:** Exfiltration  

---

## Conclusion
This challenge demonstrates how layered detection engineering — hashes, firewall rules, DNS filtering, registry monitoring, network behavior, and file activity — can significantly increase an adversary’s operational cost and reduce their ability to execute malware successfully.
