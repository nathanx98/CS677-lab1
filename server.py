from doctest import testfile
from xmlrpc.server import SimpleXMLRPCServer

def testFunc(num1, num2):
	return num1 + num2


cache = []
def updateCache(elem):
	cache.append(elem)
	print(cache)
	return "message updated"

server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(testFunc, "testFunc")
server.register_function(updateCache, "updateCache")
server.serve_forever()