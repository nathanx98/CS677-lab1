from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

class Peer:
    def __init__(self, name, addr, port) -> None:
        self.msg = []
        self.name = name #(this could be role?)
        # update proxy when connected to other server (neighbor)
        self.proxy = None
        self.server = SimpleXMLRPCServer((addr, port), allow_none=True)
        self.server.register_function(self.send, "send")
    
    # connect to another rpc server
    def connect(self, port):
        print(f"http://localhost:{port}")
        self.proxy = xmlrpc.client.ServerProxy(f"http://localhost:{port}")

    # send a message to proxy
    def send(self, message):
        self.msg.append(message)
        print(f"messgge from {message}")

    # lookup by the buyer, terminate when hopCount = 0
    def lookup(buyerId, product_name:str, hopCount:int, path: list):
        pass

    # reply message by the seller
    def reply(sellerId, path:list):
        pass

    # buyer picks one seller with {peerId} if multiple sellers respond
    def buy(peerId, path:list):
        pass



