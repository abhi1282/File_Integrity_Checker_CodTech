# File_Integrity_Checker_CodTech

**COMPANY**: CODTECH IT SOLUTIONS

**NAME**: ABHINANDAN BAIS

**DOMAIN**: CS & EH

**INTERN ID**: CT08GXK

**BATCH DETAILS**: December 30th, 2024 to January 30th, 2025

**MENTOR NAME**: NEELA SANTOSHI

# DESCRIPTION OF THE TOOL

The File Integrity Checker is a robust Python-based application designed to ensure file integrity by monitoring changes to specified files. It achieves this by calculating and comparing SHA-256 hash values, providing users with a reliable mechanism to detect unauthorized modifications. Here’s a detailed breakdown of its functionality:

Key Features:
Secure Hashing with SHA-256:

The tool uses the SHA-256 algorithm to compute unique hash values for files. Even minor changes in file content result in a completely different hash, ensuring precise detection of alterations.
Real-Time File Monitoring:

Once initialized, the tool continuously monitors the selected files. It recalculates hash values at intervals and compares them to previously recorded hashes. Any discrepancies trigger an immediate alert.
Interactive File Selection:

Users are prompted to enter file paths interactively. The tool validates each path, ensuring only accessible and valid files are monitored.
Detailed Change Alerts:

When a file is modified, the tool provides detailed alerts, including:
The file path.
The old (previously recorded) hash value.
The new hash value after the modification.
Error Handling:

Handles common issues gracefully, such as:
Missing files (FileNotFoundError).
Permission restrictions (PermissionError).
Invalid file paths entered by users.
Efficient Operation:

To minimize resource usage, the tool includes a delay between monitoring cycles, making it suitable for long-term deployment.
Use Cases:
Data Integrity Assurance:
Ideal for ensuring critical files (e.g., configuration files, logs, or sensitive documents) remain unaltered in security-sensitive environments.

Incident Detection and Response:
Useful for identifying security breaches or unauthorized access, as it flags any changes to monitored files.

Compliance and Auditing:
Aids organizations in adhering to data integrity regulations or conducting audits.

How It Works:
The user is prompted to input file paths interactively.
The tool calculates the initial hash for each file and displays the results.
Monitoring begins, comparing current file hashes to stored values at regular intervals.
If a change is detected, the tool alerts the user and updates the hash record.

Sample Output:-
Initial Setup:
![Screenshot 2025-01-12 190142](https://github.com/user-attachments/assets/720338bc-b69c-40fb-af83-46997a4bb4a4)
Output after file modification:



