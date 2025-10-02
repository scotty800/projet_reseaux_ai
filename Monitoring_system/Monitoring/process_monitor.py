import psutil

procs = [(p.info["pid"], p.info["name"], p.info["cpu_percent"]) 
         for p in psutil.process_iter(["pid", "name", "cpu_percent"])]

top5 = sorted(procs, key=lambda x: x[2], reverse=True)[:5]

with open("process_report.txt", "w") as f:
    for pid, name, cpu in top5:
        f.write(f"{pid}, {name}, {cpu}%\n")