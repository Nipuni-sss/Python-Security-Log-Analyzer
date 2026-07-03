# Python-Security-Log-Analyzer

A simple automated tool designed to scan server access logs and detect unauthorized access attempts based on an IP Whitelist.

##  How it Works
1. **Reads Logs:** Scans the `server_logs.txt` file line by line.
2. **Checks Authorization:** Compares each IP address against a list of pre-approved IPs (Whitelist).
3. **Generates Alerts:** Instantly flags unknown or malicious IP addresses with a security alert.

## Project Structure
* `security_analyzer.py` - The core Python script containing the detection logic.
* `server_logs.txt` - A mock log file containing allowed and unauthorized IP addresses.

##  Features Demonstrated
* Automated Log Analysis
* Threat Detection & Profiling
* IP Whitelisting Implementation
* Safe File Handling in Python
