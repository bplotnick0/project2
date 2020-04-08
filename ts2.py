import socket
import threading
import array
import sys

#DNS table entry class
class DnsEntry:
    def __init__(self, hostName, IP, Flag):
        self.hostName = hostName
        self.IP = IP
        self.Flag = Flag

###############################################################################################    



#DNS table array
DnsTable = []




#method to create table entry object and append to global DNS table ########################################################      
def addToTable(table, hostname, IP, Flag):
        x = DnsEntry(hostname, IP, Flag)
        table.append(x)  

# read from file ##############################################################################################
f = open("PROJ2-DNSTS2.txt", "r")



for line in f:
    #split each word in each line into an index of array
    line = line.split(' ')
    # print(line[1])
    h = line[0]
    i = line[1]
    fl = line[2]

    addToTable(DnsTable, h, i, fl)

#testi testin test

#desktop
f.close()


def searchname(data, sckt):
    for entry in DnsTable:
        if (entry.hostName).strip() == data.strip():
            print((entry.hostName).strip() == data.strip())
            string = (entry.hostName + " " + entry.IP + " " + entry.Flag).strip()
            sckt.send(string.encode('utf-8'))
            return
    


###################################################################################################################################

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
# port = int(lslistenport)

client.bind(('', 5003))        # Bind to the port
client.listen(5)                 # Now wait for client connection.
c, addr = client.accept()     # Establish connection with client.
print("connected")
while True:
    hstnme = c.recv(100).decode('utf-8')
    searchname(hstnme, c)
    print(hstnme)
    if not hstnme:
        break
c.close()   
