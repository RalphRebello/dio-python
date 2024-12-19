import os

with open('hosts.txt') as file:
    hosts = file.read()
    #print(hosts)
    hosts = hosts.splitlines()

#print(hosts)

for host in hosts:
    os.system(f'ping -c 3 {host}')
    #print(host)
