import socket
import array
import sys
import select


#read in ports/hostnames
lslistenport = int(sys.argv[1])
ts1hostname = int(sys.argv[2])
ts1listenport = int(sys.argv[3])
ts2hostname = int(sys.argv[4])
ts2listenport = int(sys.argv[5])
host = socket.gethostname()

ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
ts1.connect((ts1hostname, ts1listenport))
ts2.connect((ts2hostname, ts2listenport))

ts1notfound = False
def sendhostnme(hstnme, clientsckt):
    
    ts1.send(hstnme)
    ts2.send(hstnme)

    ts1.settimeout(5.0)
    ts2.settimeout(5.0)

    try:
        print("ts1 try")
        ts1data = ts1.recv(1024).decode('utf-8')
        print(ts1data)

        if not ts1data:
            pass
        else:
            clientsckt.send(ts1data.encode('utf-8'))
            return
    except socket.timeout:
        print("no response")
        ts1notfound = True
  
        
    try:
        print("ts2 try")
        ts2data = ts2.recv(1024).decode('utf-8')
        print(ts2data)

        if not ts2data:
            pass
        else:
            clientsckt.send(ts2data.encode('utf-8'))
            return
    except socket.timeout:
        if ts1notfound == True:
            errorstr =  (hstnme.decode('utf-8').strip()  + ' - Error:HOST NOT FOUND').strip()
            print(errorstr)
            clientsckt.send(errorstr.encode('utf-8'))
            ts1notfound = False

     









# connect to client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
# port = int(lslistenport)
# print(port)
client.bind(('', lslistenport))        # Bind to the port
client.listen(5)                 # Now wait for client connection.
c, addr = client.accept()     # Establish connection with client.
print("connected")
while True:
    hstnme = c.recv(100)
    print(hstnme)
    sendhostnme(hstnme, c)
    if not hstnme:
        break
c.close()                # Close the connection
 

