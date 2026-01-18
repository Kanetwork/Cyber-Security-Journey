import hashlib
import datetime
import os

def generate_case_entry():
    print("--- Digital Evidence Log V1.0 ---")

    # Ask for case details from the user, via the input function 
    Case_Number = input("Enter Case Number: ").strip()
    Officer_Name = input("Investigating Officer: ")
    Evidence_Title = input("Title of Evidence: ")
    Evidence_Desc = input("Description of Evidence: ")
    
    # continuation of user input, However asks for a folder name within the current directory,
    # where it checks if the directory already exixst and prepares to add the file to the directory.
    Base_Dir = input("Select folder: ")
    Case_Dir = os.path.join(Base_Dir, Case_Number)

    # First part creates Base_Dir and Case_Dir if not present.
    if not os.path.exists(Case_Dir):
        os.makedirs(Case_Dir)
        print(f"[!] New directory created for {Case_Number}")
    else:
        print(f"[*] Adding to existing directory for {Case_Number}")

    # Get current time in the following format. Y-M-D H:M:S
    Timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Formatting of the log
    log_entry = f"[{Timestamp}] CASE: {Case_Number} | Officer {Officer_Name} | TITLE: {Evidence_Title} | EVID: {Evidence_Desc}"

    # Create digital fingerprint (HASH)
    entry_hash = hashlib.md5(log_entry.encode()).hexdigest()
    final_record = f"{log_entry} | HASH: {entry_hash}\n"

    # Saving the file
    File_Path = os.path.join(Case_Dir, f"{Evidence_Title}.txt")

    with open(File_Path, "a") as f:
        f.write(final_record)

    print(f"\n[SUCCESS] Entry secured at: {File_Path}")
    print(f"Digital Fingerprint (MD5): {entry_hash}")

if __name__ == "__main__":
    generate_case_entry()