from doctest import testfile
from xmlrpc.server import SimpleXMLRPCServer

class server:

    def __init__(self,host, port):
        self.host = host
        self.port = port

    def testFunc(num1, num2):
        return num1 + num2

    def startServer(self, func):
        func = self.testFunc
        server = SimpleXMLRPCServer((self.host, self.port))
        server.register_function(func, "testFunc")
        server.serve_forever()

if __name__ == '__main__':
    myserver = server("localhost", 6799)
    myserver.startServer