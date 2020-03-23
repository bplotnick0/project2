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
        
        # if data[-2:].strip() == "NS":
        #     if boolean == False:
        #         st = data.split(' ')
        #         tssckt.connect((st[0].strip(), tslistenport))
        #         boolean = True
        #     tssckt.send(line.lower())
        #     tsdata = tssckt.recv(100)
        #     writetofile(tsdata, resolved)
            
        # else:
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
rshostname = sys.argv[1]
rslistenport = int(sys.argv[2])
tslistenport = int(sys.argv[3])
lssckt.connect((rshostname, rslistenport))
print("connectd")
dispatch(f, lssckt)
lssckt.close() 