****Digital Evidence Log V1.0****

**Project Overview**

This project is a simple digital evidence logging tool designed to support basic DFIR (Digital Forensics & Incident Response) workflows. It allows an investigator to record case details, generate a timestamped evidence entry, and automatically produce an MD5 hash to verify integrity.
The script demonstrates foundational skills in Python automation, file handling, and forensic record‑keeping.


---


**Objectives**

- Build a lightweight tool to simulate real‑world evidence logging.
- Practice Python fundamentals such as input handling, file operations, and directory management.
- Demonstrate understanding of forensic integrity concepts through hashing.
- Strengthen workflow thinking around case documentation and structured logging.


---


**Features**

- Collects case number, officer name, evidence title, and description.
- Automatically creates case folders if they do not already exist.
- Generates a timestamp in YYYY‑MM‑DD HH:MM:SS format.
- Produces a formatted evidence entry containing all metadata.
- Generates an MD5 hash of the entry to provide a digital fingerprint.
- Saves each evidence entry as a .txt file inside the appropriate case directory.


---


**Skills Demonstrated**

- Python scripting and automation
- File and directory handling (os, open(), path management)
- Hashing and integrity verification (hashlib)
- Timestamp generation (datetime)
- Basic DFIR workflow design
- Clean code structure and user‑input handling

---


**Project Structure**

| Component | Description |
|----------|-------------|
| main script | Core logic of the tool |
| supporting files | Keys, configs, or resources |
| output or logs | Example results or evidence |


---


**How to Run**

- Ensure Python 3 is installed.
- Save the script in your working directory.
- Open a terminal and run: python3 DFIR_Evidence_Log_v1.py
- Follow the on‑screen prompts to enter case details.
- The script will create a folder for the case and save the evidence entry inside it.


---


**Security Considerations**

- MD5 is used for educational purposes; in real forensic environments, stronger hashing algorithms (e.g., SHA‑256) are preferred.
- User input is not validated or sanitized — this is acceptable for a learning tool but should be improved for production use.
- No encryption or access control is implemented; this script is intended for demonstration, not operational deployment.


--


**What I Learned**

- How to structure a Python script around a real‑world DFIR workflow.
- The importance of timestamps and consistent formatting in forensic documentation.
- How hashing supports integrity verification and chain‑of‑custody principles.
- Practical experience with directory creation and file writing in Python.
- How to design a simple but functional command‑line tool.


--


**Future Improvements**

- Add digital signature support (e.g., RSA signing).
- Replace MD5 with SHA‑256 or SHA‑3.
- Implement input validation and error handling.
- Add a verification mode to check hashes against stored entries.
- Build a GUI version for easier use by non‑technical investigators.
- Export logs in JSON or CSV for ingestion into forensic platforms.
