import socket
import random
import threading
import sys

class sockPeer:

    def __init__(self, name, peerlist, maxpeers, host, serverport) -> None:
        self.name = name
        self.peerlist = peerlist
        self.maxpeers = maxpeers
        self.host = host
        self.serverport = serverport
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def closeSock(self):
        self.s.close()

    def startServer(self):
        t = threading.Thread(target=self.serverSock)
        t.start() 

    def startClient(self, conhost, conport):
        t = threading.Thread(target=self.ClientSock(conhost, conport))
        t.start()

    def serverSock(self, open=1):
        self.s.bind((self.host, self.serverport))
        self.s.listen()
        conn, addr = self.s.accept()
        print(f"Connected by {addr}")
        while open:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        
    def ClientSock(self, conhost, conport):
        self.s.connect((conhost, conport))
        self.s.sendall(b"Hello, world")
        data = self.s.recv(1024)
        self.s.close()
        print(f"Received {data!r}")

#-----------------------------------------------------------------
    def setmyrole( self, assign_role = None ):
        #decide which product and role a peer is by random assignment

        if assign_role != None: #optional to assign roles to aid in testing
            self.myrole = assign_role
        else:
            self.myrole = random.choice(['buyer','fish_seller','boar_seller','salt_seller'])

    
if __name__ == '__main__':
    p = sockPeer(sys.argv[0], "None", 3, sys.argv[1], sys.argv[2])
    p.setmyrole()

    if p.myrole == 'buyer':
        p.startServer
    else:
        pass

