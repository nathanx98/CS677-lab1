from doctest import testfile
from xmlrpc.server import SimpleXMLRPCServer

def testFunc(num1, num2):
	return num1 + num2

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(testFunc, "testFunc")
server.serve_forever()