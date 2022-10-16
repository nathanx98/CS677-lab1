import peer
import threading

#Simple function to kill a server    
def kill(server):
    server.quit = 1
    return 1

# start server 
p1 = peer.Peer('p1', "localhost", 8890)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
p1.startServer()


p2 = peer.Peer('p2', "localhost", 4446)
# t = threading.Thread(target=p2.server.serve_forever)
# t.start()
p2.startServer()
p3 = peer.Peer("p3", "localhost", 5557)

# connect to port to send messages
p1.connect(4446)
p1.proxy.send(f"hello from {p1.name}")

p2.connect(8890)
p2.proxy.send(f"hello from {p2.name}")

p1.proxy.send("I'm good!")
print(p2.msg)

p3.connect(4446)
p3.proxy.send("hi from peer 3")
print(p2.msg)

kill(p1)
kill(p2)
kill(p3)

#-----------------------------------------------------------------
# adding bazaar functionality to peer class
# start server 
buyer = peer.Peer('buyer', "localhost", 8020)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
buyer.setmyrole('buyer')
print(buyer.myrole())
#buyer.startServer()

seller1 = peer.Peer('seller', "localhost", 8020)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
seller1.setmyrole()
print(seller1.myrole())
#seller1.startServer()