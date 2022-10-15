import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
import sys
import threading

proxy = xmlrpc.client.ServerProxy("http://localhost:6789")


def func():
    print("test!")


def send():
    proxy.updateCache('hello')


server = SimpleXMLRPCServer(("localhost", 6790), allow_none=True)
server.register_function(func, "func")
t1 = threading.Thread(target=server.serve_forever)
t2 = threading.Thread(target=send)

t1.start()
t2.start()