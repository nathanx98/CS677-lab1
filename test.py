import peer
import threading

# start server 
p1 = peer.Peer('p1', "localhost", 8888)
# t = threading.Thread(target=p1.server.serve_forever)
# t.start()
p1.startServer()


p2 = peer.Peer('p2', "localhost", 4444)
# t = threading.Thread(target=p2.server.serve_forever)
# t.start()
p2.startServer()
p3 = peer.Peer("p3", "localhost", 5555)

# connect to port to send messages
p1.connect(4444)
p1.proxy.send(f"hello from {p1.name}")

p2.connect(8888)
p2.proxy.send(f"hello from {p2.name}")

p1.proxy.send("I'm good!")
print(p2.msg)

p3.connect(4444)
p3.proxy.send("hi from peer 3")
print(p2.msg)