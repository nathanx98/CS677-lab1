from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import random

class Peer(SimpleXMLRPCServer):
    #Peer class extends the capabilities of the simpleXMLRPCServer

    def __init__(self, name, addr, port) -> None:
        super().__init__((addr, port), allow_none=True)
        self.msg = []
        self.name = name #(this could be role?)
        
        # update proxy when connected to other server (neighbor)
        self.proxy = None
        #self.server = SimpleXMLRPCServer((addr, port), allow_none=True)
        self.register_function(self.send, "send")
    
    def serve_forever(self):
    #modifies the server forever function in simplXMLRPCServer to handle requests forever
    #until told to quit
        self.quit = 0
        while not self.quit:
            self.handle_request()

    
    def startServer(self):
        threading.Thread(target=self.serve_forever).start()
    
    # connect to another rpc server
    def connect(self, port):
        print(f"http://localhost:{port}")
        self.proxy = xmlrpc.client.ServerProxy(f"http://localhost:{port}")

    # send a message to proxy
    def send(self, message):
        self.msg.append(message)
        print(f"messgge from {message}")


#-----------------------------------------------------------------
    def setmyrole( self, assign_role = None ):
        #decide which product and role a peer is by random assignment

        if assign_role != None: #optional to assign roles to aid in testing
            self.myrole = assign_role
        else:
            self.myrole = random.choice(['buyer','fish_seller','boar_seller','salt_seller'])

    # lookup by the buyer, terminate when hopCount = 0
    def lookup(self, buyerId, product_name:str, hopCount:int, path: list):
        pass

    # reply message by the seller
    def reply(self, sellerId, path:list):
        pass

    # buyer picks one seller with {peerId} if multiple sellers respond
    def buy(self, peerId, path:list):
        pass

