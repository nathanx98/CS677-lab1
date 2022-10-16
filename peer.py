from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import threading
import random
import time

class Peer(): #Peer(SimpleXMLRPCServer):
    #Peer class extends the capabilities of the simpleXMLRPCServer

    def __init__(self, name, addr, serverport) -> None:
        #super().__init__((addr, serverport), allow_none=True)
        self.msg = []
        self.name = name #pid or tuple(host,port)?
        self.locate = [addr,serverport]
        self.myrole = None
        
        # update proxy when connected to other server (neighbor)
        self.proxy = None
        self.server = SimpleXMLRPCServer((addr, serverport), allow_none=True)
        self.server.register_function(self.send, "send")
        self.server.register_function(self.myrole, 'myrole')
        self.server.register_function(self.lookup, 'lookup')
        self.server.register_function(self.buy, 'buy')
        self.server.register_function(self.reply, 'reply')
    
    def startServer(self):
        #starts server runinng on a seperate thread to listen for messages
        threading.Thread(target=self.server.serve_forever).start()
    
    # connect to another rpc server
    def connect(self, port):
        print(f"http://localhost:{port}")
        self.proxy = xmlrpc.client.ServerProxy(f"http://localhost:{port}")

    # send a message to proxy
    def send(self, message):
        self.msg.append(message)
        print(f"messgge from {message}")

    def passMSG(self, destPort, message):
        self.connect(destPort)
        self.proxy(message)

#-----------------------------------------------------------------
    def setmyrole(self, assign_role = None ):
        #decide which product and role a peer is by random assignment

        if assign_role != None: #optional to assign roles to aid in testing
            self.myrole = assign_role
        else:
            self.myrole = random.choice(['buyer', 'seller'])

        if self.myrole =='seller':
            self.myproduct = random.choice(['salt', 'boar', 'fish'])#define what seller is selling
            self.inventory = 5 #initialize number of items to sell

    def changeInventory(self):
        self.inventory = self.inventory - 1 #decremente inventory as items are sold
        if self.inventory == 0: #once sold out of items pick new item to sell
            self.setmyrole('seller')

    # lookup by the buyer, terminate when hopCount = 0
    def lookup(self, product_name:str, hopCount:int, peerlist, searchpath):
        
        if hopCount == 0: #once hopcount reaches zero we stop the message
            pass

        myneighbors = peerlist[self.name]
        hopCount = hopCount -1 #decrement hopcount now that we made a hop

        if self.myrole == 'buyer': #if I'm a buyer just pass the message along
            searchpath.append(self.locate) #add my location to the path

            for n in range(len(myneighbors)):
                neighbor = myneighbors[n]
                self.connect(neighbor[1]) #establish connection to my neighbor
                self.proxy.lookup(product_name, hopCount, peerlist, searchpath) #invoke the lookup function on my neighbor with the new path
        
        elif self.product_name != product_name: #I'm a seller but not for that item
            searchpath = searchpath.append(self.locate) #add my location to the path

            for n in range(len(myneighbors)):
                neighbor = myneighbors[n]
                self.connect(neighbor[1]) #establish connection to my neighbor
                self.proxy.lookup(product_name, hopCount, peerlist, searchpath) #invoke the lookup function on my neighbor with the new path
        
        else: #I'm a seller for that item
            self.reply(self.name, searchpath)
        
    # reply message by the seller
    def reply(self, sellerId, replypath:list):
        
        #reduce path to what is remaining after this peer
        target_ibdex = replypath.index(self.locate)
        path = replypath[:target_ibdex+1]

        if len(path == 0):#we reached the buyer
            self.replyqueue[sellerId] = replypath #add to dictionary of replies
        
        else:
            #call method recusivly on next peer
            nextpeer = reversed(path)[0] 
            self.connect(nextpeer)
            self.proxy.reply(sellerId, replypath)


    # buyer picks one seller with {peerId} if multiple sellers respond
    def buy(self, buyerId, peerId, path:list):
        path = path.pop(0)

        if len(path) == 0: #we reached the seller
            self.changeInventory() #update inventory
            print(buyerId, " bought ", self.myproduct, " from ", self.name) 
        nextpeer = path[0] 
        self.connect(nextpeer)
        self.proxy.buy(buyerId, peerId, path)

#-----------------------------------------------------------------
    def mainloop(self, peerlist):
        self.startServer() #start server to listen for requests

        self.peerlist = peerlist
        myneighbors = peerlist[self.name]

        if self.myrole == None:
            self.setmyrole() #peer decides which role it will be in the bazaar
            print(self.name, "role in the bazaar is", self.myrole)

        if self.myrole == 'buyer':
            #sends out lookup request for a product
            product_id = random.choice(['fish', 'boar', 'salt'])
            self.replyqueue = {} #initialize a reply queue

            print(self.name, "is a buyer, looking for", product_id)
            #send on to my neighbors by calling the lookup function
            for n in range(len(myneighbors)):
                searchpath = list()
                self.lookup(product_id, 3, peerlist, searchpath)
            
            print(self.name, "is a buyer, waiting...")
            time.sleep(5)

            #now parse out our reply queue, select one seller and buy the item
            print(self.replyqueue.keys(), "replied to", self.name)
            sellerId, path = random.choice(list(self.replyqueue.items())) #randomly choice a seller
            self.buy(self.name, sellerId, path)

        else: #start server and wait for requests
            self.startServer()


