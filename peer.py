
#import struct

#import time
#import traceback

import random
import os
import socket
import numpy as np
import threading
import selectors

import traceback

class peer:
    # Core functionality to be used by a peer in a our P2P network.

    def __init__(self, maxpeers, ns, serverport, serverhost = "127.0.0.1"):
        #initialze a peer
        self.maxpeers = int(maxpeers) #set to 3 but could be changed
        self.ns = ns #namesever with list of peer IDs and addresses
        self.myid = os.getpid()
        self.peers = {} #list of this peers peers

        #socket handling
        self.shutdown = False #to close loop
        self.serverport = int(serverport)
        self.serverhost = serverhost
        self.handlers = {}
        self.router = None

    def newserversock(self, port): 
    # create a streaming socket, bind to port, and listen on port then queue connection requests
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #using smaller IPv4 address
        sock.bind(('localhost', port)) #since we are communicating only on local machine
        sock.listen(5) #now we listen on our port for a request and queue up messages limited by 5
        return sock 
    
    def main_loop(self):
    #the workhouse of our socket 
        sock = self.newserversock(self.serverport) #make the server socket
        self.debug( 'Server has started: %s (%s:%d)' % ( self.myid, self.serverhost, self.serverport )) #so we know socket is running


        while not self.shutdown: #if shutdown == True the socket will close
            #error handling, socket will start but can be stopped by user using keyboard
            try:
                self.debug('Listening for connection requests')
                clientsock, clientaddr = sock.accept()
                clientsock.settimeout(None) #don't close until we are finished
                
                #each connection will be passed onto a seperete thread for handling
                t = threading.Thread (target = self.handlepeer, args = [clientsock])
                t.start() 
            except KeyboardInterrupt: 
                self.shutdown = True #will force loop to close
                continue
            except:
                if self.debug:
                    traceback.print.exec() #final exemption case dump messages to console
        self.debug("Closing main socket loop bye")
        sock.close()

    def start_connection(host, port, request):
        sel = selectors.DefaultSelector()
        addr = (host, port)
        print(f"Starting connection to {addr}")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        message = libclient.Message(sel, sock, addr, request)
        sel.register(sock, events, data=message)

    def handlepeer():
        #handles incoming peer connection and message exchange on seperate thread
        pass





    def setmyrole( self, assign_role = None ):
        #decide which product and role a peer is by random assignment

        if assign_role != None: #optional to assign roles to aid in testing
            self.myrole = assign_role
        else:
            self.myrole = random.choice(['buyer','fish_seller','boar_seller','salt_seller'])

    def lookup(self, buyerID, product_name, hopcount, searchPath):
        hopcount = self.maxpeers - 1 #less than maximum distance between peers
        msg = np.array[buyerID, product_name]

        for i in hopcount:
            #send message to next peer and add id to search path
            if hopcount == 0:
                pass

    def repy(self, sellerID, replyPath):

        for i in replyPath:
            #send message to next peer
            replyPath = np.delet(replyPath, 0)
        pass
    def buy(self, peerID, path):
        peerID = np.random.choice(peerID)
        for i in path:
            #send msg
            if path[i] == peerID:
                pass
    def debug(self, message):
        # prints msg to console
        print(str(threading.currentThread().getName()), message )

        import socket


