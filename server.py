from doctest import testfile
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import multiprocessing


cache = []

def updateCache(elem):
	cache.append(elem)
	print("cache is: ", cache)
	return "message updated"


server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(updateCache, "updateCache")
# server.serve_forever()
p = multiprocessing.Process(target=server.serve_forever)
p.start()