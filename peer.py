from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading

class Peer:
    def __init__(self, name, addr, port) -> None:
        self.msg = []
        self.name = name
        # use this to connect to user server
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


