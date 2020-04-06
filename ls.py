import socket
import array
import sys
import select


#read in ports/hostnames
lslistenport = sys.argv[1]
ts1hostname = sys.argv[2]
ts1listenport = sys.argv[3]
ts2hostname = sys.argv[4]
ts2listenport = sys.argv[5]





def sendhostnme(hstnme, clientsckt):
#connect to ts1 and ts2
    ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ts1.connect(ts1hostname, ts1listenport)
    ts2.connect(ts2hostname, ts2listenport)

    ts1.send(hstnme)
    ts2.send(hstnme)

    ts1.settimeout(5000)
    ts2.settimeout(5000)


    data = [ ts1.recv(1024),
    ts2.recv(1024)]




#send hstnme to both ts1 and ts2

#get response 
    #if(time > 5000ms):
        #send error string
    #else:
        #send received string






messages = [ 'This is the message. ',
             'It will be sent ',
             'in parts.',
             ]
server_address = ('localhost', 10000)

# Create a TCP/IP socket
socks = [ socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          socket.socket(socket.AF_INET, socket.SOCK_STREAM),
          ]

# Connect the socket to the port where the server is listening
print >>sys.stderr, 'connecting to %s port %s' % server_address
for s in socks:
    s.connect(server_address)



for message in messages:

    # Send messages on both sockets
    for s in socks:
        print >>sys.stderr, '%s: sending "%s"' % (s.getsockname(), message)
        s.send(message)

    # Read responses on both sockets
    for s in socks:
        data = s.recv(1024)
        print >>sys.stderr, '%s: received "%s"' % (s.getsockname(), data)
        if not data:
            print >>sys.stderr, 'closing socket', s.getsockname()
            s.close()







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
 

