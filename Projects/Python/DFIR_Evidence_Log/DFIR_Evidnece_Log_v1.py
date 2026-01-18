import hashlib
import datetime
import os

def generate_case_entry():
    print("--- Digital Evidence Log V1.0 ---")

    # Collect case information from the user. 
    # .strip() removes accidental spaces at the start/end of the case number.
    Case_Number = input("Enter Case Number: ").strip()
    Officer_Name = input("Investigating Officer: ")
    Evidence_Title = input("Title of Evidence: ")
    Evidence_Desc = input("Description of Evidence: ")
    
    # Ask the user for a base directory where the case folder will be stored. 
    # The final case directory will be: Base_Dir / Case_Number
    Base_Dir = input("Select folder: ")
    Case_Dir = os.path.join(Base_Dir, Case_Number)

    # Create the case directory if it does not already exist. 
    # os.makedirs() will also create any missing parent folders inside Base_Dir.
    if not os.path.exists(Case_Dir):
        os.makedirs(Case_Dir)
        print(f"[!] New directory created for {Case_Number}")
    else:
        print(f"[*] Adding to existing directory for {Case_Number}")

    # Generate a timestamp in the format YYYY-MM-DD HH:MM:SS. 
    # This ensures consistent forensic logging.
    Timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build the evidence log entry using all collected information. 
    # This forms the human-readable record stored in the evidence file.
    log_entry = f"[{Timestamp}] CASE: {Case_Number} | Officer {Officer_Name} | TITLE: {Evidence_Title} | EVID: {Evidence_Desc}"

    # Create a digital fingerprint of the log entry using MD5 hashing. 
    # MD5 is used here for learning purposes; stronger hashes are recommended.
    entry_hash = hashlib.md5(log_entry.encode()).hexdigest()

    # Combine the log entry and its hash into the final record written to file.
    final_record = f"{log_entry} | HASH: {entry_hash}\n"

    # Build the full path for the evidence file. 
    # Each evidence item is saved as: Case_Dir / Evidence_Title.txt
    File_Path = os.path.join(Case_Dir, f"{Evidence_Title}.txt")

    # Open the evidence file in append mode ("a") so new entries are added without overwriting
    with open(File_Path, "a") as f:
        f.write(final_record)

    # Display confirmation to the user, including the file location and generated hash.
    print(f"\n[SUCCESS] Entry secured at: {File_Path}")
    print(f"Digital Fingerprint (MD5): {entry_hash}")

# Run the script only if executed directly (not imported as a module).
if __name__ == "__main__":
    generate_case_entry()