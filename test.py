from re import sub
import peer
import os
import subprocess
import time

# start server 
# p1 = peer.Peer('p1', 8891)
# # t = threading.Thread(target=p1.server.serve_forever)
# # t.start()
# p1.startServer()


# p2 = peer.Peer('p2',4447)
# # t = threading.Thread(target=p2.server.serve_forever)
# # t.start()
# p2.startServer()

# # connect to port to send messages
# p1.connect(4447)
# p1.proxy.send(f"hello from {p1.name}")


# p2.connect(8891)
# p2.proxy.send(f"hello from {p2.name}")

# p1.proxy.send("I'm good!")
# print(p2.msg)

# p3 = peer.Peer("p3", 5558)
# p3.connect(4447)
# p3.proxy.send("hi from peer 3")
# print(p2.msg)

#-----------------------------------------------------------------
# adding bazaar functionality to peer class
peerlist = {'all':[9001,9002,9003,9004,9005,9006], 
            'p1':[9002,9003], 'p2':[9004,9005], 
            'p3':[9005,9006], 'p4':[9002,9005], 
            'p5':[9002,9003,9004], 'p6':[9001,9003]}

subprocess.Popen(["python3", "peer.py", "p1", "9001", 'buyer'])
time.sleep(1)
subprocess.Popen(["python3", "peer.py", "p2", "9002", 'seller'])
time.sleep(1)
# subprocess.Popen(["python3", "peer.py", "p3", "9003"])
# time.sleep(1)
# subprocess.Popen(["python3", "peer.py", "p4", "9004"])
# time.sleep(1)
# subprocess.Popen(["python3", "peer.py", "p5", "9005"])
# time.sleep(1)
# subprocess.Popen(["python3", "peer.py", "p6", "9006"])
# time.sleep(1)









# # start server 
# buyer = peer.Peer('buyer', "localhost", 8002)
# # t = threading.Thread(target=p1.server.serve_forever)
# # t.start()
# buyer.setmyrole('buyer')
# print(buyer.myrole)
# #buyer.startServer()

# seller1 = peer.Peer('seller', "localhost", 8003)
# # t = threading.Thread(target=p1.server.serve_forever)
# # t.start()
# seller1.setmyrole('salt_seller')
# #seller1.startServer()

# p1 = peer.Peer('p1', "localhost", 8006)
# p1.startServer()
# p2 = peer.Peer('p2', "localhost", 8007)
# p2.startServer()
# p2.setmyrole('seller')
# p3 = peer.Peer('p2', "localhost", 8008)
# p3.startServer()
# p3.setmyrole('seller')
# p4 = peer.Peer('p2', "localhost", 8009)
# p4.startServer()
# p4.setmyrole('seller')
# p5 = peer.Peer('p2', "localhost", 8010)
# p5.startServer()
# p5.setmyrole('seller')
# p6 = peer.Peer('p2', "localhost", 8011)
# p6.startServer()
# p6.setmyrole('seller')

# peerlist = {'all':[p1.locate,p2.locate,p3.locate,p4.locate,p5.locate,p6.locate], 
#             'p1':[p2.locate,p3.locate], 'p2':[p4.locate,p5.locate], 
#             'p3':[p5.locate,p6.locate], 'p4':[p2.locate,p5.locate], 
#             'p5':[p2.locate,p3.locate,p4.locate], 'p6':[p1.locate,p3.locate]}
# #test case p1 is a buyer and everyone else is a seller
# p1.setmyrole('buyer')
# p1.connect(8007)
# p1.proxy.send(f"hello from {p1.name}")
# #p1.proxy.buy('p1', 'p2', [p1.locate])
# #p1.mainloop(peerlist)
