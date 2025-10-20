import ipaddress
import subprocess
import csv
import platform
from concurrent.futures import ThreadPoolExecutor

# Input avec strip et valeur par défaut
user_input = input("Entrez le subnet (par défaut 192.168.1.0/24) : ").strip()
if not user_input:
    user_input = "192.168.1.0/24"

subnet = ipaddress.ip_network(user_input, strict=False)
hosts_up = []

# Commande ping selon OS
ping_cmd_base = ["ping", "-c", "1", "-W", "1"] if platform.system() != "Windows" else ["ping", "-n", "1", "-w", "1000"]

def ping(ip):
    result = subprocess.run(ping_cmd_base + [str(ip)], stdout=subprocess.DEVNULL)
    return str(ip) if result.returncode == 0 else None

with ThreadPoolExecutor(max_workers=50) as executor:
    for ip in executor.map(ping, subnet.hosts()):
        if ip:
            hosts_up.append(ip)

# Écriture CSV
with open('hosts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IP"])
    writer.writerows([[ip] for ip in hosts_up])

print(f"{len(hosts_up)} hôtes trouvés.")
