"""
Server side: open a socket on a port, listen for a message from a client, and 
send an echo reply; this version uses the standard library module socketserver to
do its work; socketserver provides TCPServer, ThreadingTCPServer, ForkingTCPServer,
UDP variants of these, and more, and routes each client connect request to a new 
instance of a passed-in request handler object's handle method; socketserver also
supports Unix domain sockets, but only on Unixen; see the Python library manual.
"""

import socketserver, time               # get socket server, handler objects
myHost = '127.0.0.1'                    # server machine, '' means local host
myPort = 50007
test = ''
first = 'hold/ \n' 
second = 'SPRADES 10 \n'
third = 'SPRADES A \n'
fourth = '/hold \n'
holdsmsg = 'hold/ \n' 
holdsmsg += 'SPRADES 10 \n'
holdsmsg += 'SPRADES A \n'
holdsmsg += '/hold \n'
test = 'inquire/ \n'
test += 'pid jetton money bet blind \n'
test += 'pid jetton money bet blind \n'
test += 'pid jetton money bet call \n'
test += 'pid jetton money bet fold \n'
test += 'pid jetton money bet fold \n'
test += 'pid jetton money bet call \n' 
test += 'total pot num \n'
test += '/inquire \n'                              # listen on a non-reserved port number
def now():
    return time.ctime(time.time())

class MyClientHandler(socketserver.BaseRequestHandler):
    def handle(self):                           # on each client connect
        print(self.client_address, now())       # show this client's address
        time.sleep(5)                           # simulate a blocking activity
        while True:                             # self.request is client socket
            data = self.request.recv(1024)      # read, write a client socket
            if not data: break
            print(data.decode())
            reply = 'Echo=>%s at %s' % (data, now())
            #self.request.send(reply.encode())
            self.request.send(first.encode())
            self.request.send(second.encode())
            self.request.send(third.encode())
            self.request.send(fourth.encode())
            #self.request.send(test.encode())
        self.request.close()

# make a threaded server, listen/handle clients forever
myaddr = (myHost, myPort)
server = socketserver.ThreadingTCPServer(myaddr, MyClientHandler)
server.serve_forever()
