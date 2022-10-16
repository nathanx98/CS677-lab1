import peer
import os
import threading

# start server 
p1 = peer.Peer('p1', "localhost", 8890)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
p1.startServer()


p2 = peer.Peer('p2', "localhost", 4446)
# t = threading.Thread(target=p2.server.serve_forever)
# t.start()
p2.startServer()

# connect to port to send messages
p1.connect(4446)
p1.proxy.send(f"hello from {p1.name}")

p2.connect(8890)
p2.proxy.send(f"hello from {p2.name}")

p1.proxy.send("I'm good!")
print(p2.msg)

p3 = peer.Peer("p3", "localhost", 5557)
p3.connect(4446)
p3.proxy.send("hi from peer 3")
print(p2.msg)

#-----------------------------------------------------------------
# adding bazaar functionality to peer class
# start server 
buyer = peer.Peer('buyer', "localhost", 8002)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
buyer.setmyrole('buyer')
print(buyer.myrole)
#buyer.startServer()

seller1 = peer.Peer('seller', "localhost", 8003)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
seller1.setmyrole('salt_seller')
#seller1.startServer()

p1 = peer.Peer('p1', "localhost", 8006)
p2 = peer.Peer('p2', "localhost", 8007)
p2.startServer()
p2.setmyrole('seller')
p3 = peer.Peer('p2', "localhost", 8008)
p3.startServer()
p3.setmyrole('seller')
p4 = peer.Peer('p2', "localhost", 8009)
p4.startServer()
p4.setmyrole('seller')
p5 = peer.Peer('p2', "localhost", 8010)
p5.startServer()
p5.setmyrole('seller')
p6 = peer.Peer('p2', "localhost", 8011)
p6.startServer()
p6.setmyrole('seller')

peerlist = {'all':[p1.locate,p2.locate,p3.locate,p4.locate,p5.locate,p6.locate], 
            'p1':[p2.locate,p3.locate], 'p2':[p4.locate,p5.locate], 
            'p3':[p5.locate,p6.locate], 'p4':[p2.locate,p5.locate], 
            'p5':[p2.locate,p3.locate,p4.locate], 'p6':[p1.locate,p3.locate]}
#test case p1 is a buyer and everyone else is a seller
p1.setmyrole('buyer')
p1.mainloop(peerlist)
