import paramiko
import os

ip = "192.168.1.10"
username = "user"
password = "password"

output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(ip, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command('uname -a && df -h')

output = stdout.read().decode()
with open(f"data/config_{ip}.txt", 'w') as file:
    file.write(output)

ssh.close()