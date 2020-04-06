import socket
import threading
import array
import sys
import select
import Queue

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
f = open("PROJ2-DNSTS1.txt", "r")



for line in f:
    #split each word in each line into an index of array
    line = line.split(' ')
    # print(line[1])
    h = line[0]
    i = line[1]
    fl = line[2]

    addToTable(DnsTable, h, i, fl)

f.close()


def searchname(data, sckt):
    for entry in DnsTable:
        if (entry.hostName).strip() == hostnme.strip():
            print((entry.hostName).strip() == hostnme.strip())
            string = (entry.hostName + " " + entry.IP + " " + entry.Flag).strip()
            sckt.send(string)
            return
    


###################################################################################################################################

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
server.bind(('localhost', 50000))
server.listen(5)
inputs = [server]
outputs = []
message_queues = {}

while inputs:
    readable, writable, exceptional = select.select(
        inputs, outputs, inputs)
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            connection.setblocking(0)
            inputs.append(connection)
            message_queues[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            searchname(data, s)
            if data:
                # message_queues[s].put(data)
                # if s not in outputs:
                #     outputs.append(s)
            else:
                # if s in outputs:
                #     outputs.remove(s)
                # inputs.remove(s)
                s.close()
                # del message_queues[s]

    # for s in writable:
    #     try:
    #         next_msg = message_queues[s].get_nowait()
    #     except Queue.Empty:
    #         outputs.remove(s)
    #     else:
    #         s.send(next_msg)

    # for s in exceptional:
    #     inputs.remove(s)
    #     if s in outputs:
    #         outputs.remove(s)
    #     s.close()
    #     del message_queues[s]