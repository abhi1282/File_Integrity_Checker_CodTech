import hashlib
import os
import time

def calculate_file_hash(filepath):
    """Calculate the hash of a file using SHA-256."""
    hash_function = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                hash_function.update(chunk)
        return hash_function.hexdigest()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied for {filepath}.")
        return None

def monitor_files(filepaths):
    """Monitor a list of files for changes by comparing hash values."""
    # Calculate initial hashes for the files
    file_hashes = {}
    print("\n[+] Initial file hashes calculated:")
    
    for filepath in filepaths:
        file_hash = calculate_file_hash(filepath)
        if file_hash:
            file_hashes[filepath] = file_hash
            print(f"  {filepath}: {file_hash}")
        else:
            print(f"  {filepath}: Error in calculating hash")

    print("\n[+] Monitoring files for changes...\n")
    
    try:
        while True:
            for filepath in filepaths:
                current_hash = calculate_file_hash(filepath)
                if current_hash != file_hashes.get(filepath):
                    print(f"\n[!] File changed: {filepath}")
                    print(f"  Previous hash: {file_hashes[filepath]}")
                    print(f"  New hash: {current_hash}")
                    file_hashes[filepath] = current_hash
            time.sleep(1)  # Delay between checks to avoid high CPU usage
    except KeyboardInterrupt:
        print("\n[+] Monitoring stopped. Exiting...")

def get_file_paths():
    """Prompt the user to input file paths for monitoring."""
    filepaths = []
    print("Note: If the file path contains spaces, enclose it in double quotes.")
    while True:
        filepath = input("Enter the file path to monitor (or type 'done' to finish): ").strip()
        if filepath.lower() == 'done':
            break
        elif os.path.isfile(filepath):
            filepaths.append(filepath)
            print(f"  - Added {filepath} to monitor.")
        else:
            print(f"  Error: {filepath} is not a valid file path. Please try again.")
    return filepaths

if __name__ == "__main__":
    print("=" * 50)
    print("     Welcome to the File Integrity Monitor")
    print("=" * 50)
    
    # Get user input for files to monitor
    files_to_monitor = get_file_paths()
    
    if files_to_monitor:
        # Start monitoring the files
        monitor_files(files_to_monitor)
    else:
        print("[-] No valid file paths entered. Exiting...")
    print("=" * 50)
