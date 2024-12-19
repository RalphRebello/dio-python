import os


print('#' * 60)

ip_host = input("informe o ip ou host -> ")
print('-' * 60)
os.system(f'ping -c 3 {ip_host}')
print('-' * 60)