import psutil, time, csv

with open('system_metrics.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Cpu_percent', 'ram_percent',])
    while True:
        Cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), Cpu, ram])
        print(f"Cpu: {Cpu}% | RAM: {ram}%")
        time.sleep(5)