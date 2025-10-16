import socket, csv

with open("hosts.csv") as file:
    hosts = [row.strip() for row in file.readlines()[1:]]

with open("data/reports/port_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["IP", "PORT", "STATUS"])
    
    for ip in hosts:
        for port in range(20, 1025):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.3)
            result = s.connect_ex((ip, port))
            if result == 0:
                writer.writerow([ip, port, "OPEN"])
            s.close()