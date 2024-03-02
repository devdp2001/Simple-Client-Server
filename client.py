from socket import *
s_name, s_port = 'localhost', 12000

c_soc = socket(AF_INET, SOCK_STREAM)
c_soc.connect((s_name, s_port))
print('Connected to Remote Server')

number = input("Input a number from 1-100: ")
name = input("What is your name? ")
data = name + " " + number

c_soc.send(data.encode())
print('Data sent... waiting for response.')

resp = c_soc.recv(1024)
print(resp.decode())
c_soc.close()

