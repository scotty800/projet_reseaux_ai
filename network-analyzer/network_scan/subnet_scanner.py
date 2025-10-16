import ipaddress, subprocess, csv

subnet = ipaddress.ip_network(input("192.168.1.0/24"))
hosts_up = []

for ip in subnet.hosts():
    result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)], stdout=subprocess.DEVNULL)
    if result.returncode == 0:
        hosts_up.append(str(ip))

with open('hosts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["IP"])
    for ip in hosts_up:
        writer.writerow([ip])

print(f"{len(hosts_up)} hôtes trouvés.")
