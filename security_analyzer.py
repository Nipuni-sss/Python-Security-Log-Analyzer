allowed_ips = ["192.168.2.10", "192.168.2.15", "192.168.2.20"]
print("--- SECURITY LOG ANALYZER STARTING ---")
print("Scanning server logs for unauthorized access...\n")
with open("server_logs.txt", "r") as file:
    for line in file:
        ip= line.strip()
        if ip in allowed_ips:
            print(f"[ OK ] Access Granted for: {ip}")
        else:
            print(f"[ 🚨 SECURITY ALERT ] Unauthorized Access Detected from IP: {ip}")
print("\n--- SCAN COMPLETE ---")


       