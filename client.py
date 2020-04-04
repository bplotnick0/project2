import socket
import array
import sys
 
 



resolved = open("RESOLVED.txt", "w")

def dispatch(file, lssckt): #send /receive queries
    # boolean = False
    for line in file:
        lssckt.send(line.lower())
        data = lssckt.recv(100)
        print(data)
        writetofile(data, resolved)
    resolved.close()
        

def writetofile(res, file):
    file.write(res)
    file.write("\n")



#################################################################################################
tslistenport = int(sys.argv[3])
ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
# ts.connect((host,tslistenport))




f =  open("PROJI-HNS.txt", "r")

lssckt= socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
lshostname = sys.argv[1]
lslistenport = int(sys.argv[2])
lssckt.connect((lshostname, lslistenport))
print("connectd")
dispatch(f, lssckt)
lssckt.close() 