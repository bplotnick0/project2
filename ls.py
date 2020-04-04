import socket
import array
import sys


#read in ports/hostnames
lslistenport = sys.argv[1]
ts1hostname = sys.argv[2]
ts1listenport = sys.argv[3]
ts2hostname = sys.argv[4]
ts2listenport = sys.argv[5]





sendhostnme(hstnme, clientsckt):
#connect to ts1 and ts2
    #code

#send hstnme to both ts1 and ts2

#get response 
    #if(time > 5000ms):
        #send error string
    #else:
        #send received string








# connect to client
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
port = int(lslistenport)
print(port)
s.bind(('', port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


c, addr = s.accept()     # Establish connection with client.


print("connected")
while True:
    hstnme = c.recv(100)
    sendhostnme(hstnme, c)
    if not hstnme:
        break
c.close()                # Close the connection
 

