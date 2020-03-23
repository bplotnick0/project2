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




f.close()


###################################################################################################################################