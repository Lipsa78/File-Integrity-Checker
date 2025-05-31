# File-Integrity-Checker

*COMPANY*: CODETECHIT SOLUTIONS

*NAME*: LIPSA MOHANTY

*INTERN ID*: CT04DM1494

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## Internship Task-1: File Integrity Checker – Description

A File Integrity Checker is a software tool designed to ensure that files have not been altered, corrupted, or tampered with over time. It works by generating and comparing cryptographic hash values (digital fingerprints) of files to detect any changes.

This particular tool uses the SHA-256 hashing algorithm to compute a unique hash for each selected file. When a file is scanned for the first time, the tool calculates its hash and saves it in a separate .hash file. During future scans, it recalculates the current hash of the file and compares it to the previously saved one.

If the hashes match, the file is confirmed to be intact. If the hashes are different, it indicates that the file has been modified—either intentionally or due to corruption. This makes the tool especially useful for verifying the integrity of important documents such as PDFs, Word files, PowerPoint presentations, and text files.

The tool includes a graphical user interface (GUI) built with Tkinter, making it easy to use for people with no programming knowledge. Users can select multiple files at once, and the application will check each for integrity. It also logs the results of each scan, including timestamps, to a file named integrity_log.txt.

By ensuring the consistency and authenticity of files, a file integrity checker plays a critical role in data security, digital forensics, auditing, and backup validation. It is especially helpful in environments where file reliability is crucial, such as academic research, legal document management, and IT systems administration.

This tool is simple, lightweight, and effective for anyone needing to track changes to their files and protect against unexpected modifications.

#OUTPUT: 
---
