from socket import *
from random import *

port = 12000
s_soc = socket(AF_INET, SOCK_STREAM)
s_soc.bind(('localhost', port))
s_soc.listen(1)
serverName = "Dev Patel's Server"
print(serverName + " is now ONLINE")

while True:
        con, addr = s_soc.accept()
        data = con.recv(1024).decode()

        data = data.split()
        number = int(data[-1])
        name = data[0]
        for i in range(1,len(data)-1):
                name = name + " " + data[i]
        print(name)
        print(serverName)

        random = randint(1,100)
        number = number + random

        resp = serverName + " " + str(random) + " " + str(number)
        con.send(resp.encode())
        print("Sent")
        con.close()
