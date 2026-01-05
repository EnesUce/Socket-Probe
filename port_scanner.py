import os
import socket
target_ip = "10.0.2.4"
for port in range(1, 100):
    print(f"Checking port {port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    outcome = s.connect_ex((target_ip, port))
    s.close()
    if outcome == 0:    
        os.system(f"nc {target_ip} {port}")
    else:
        print(f"port {port} is closed")