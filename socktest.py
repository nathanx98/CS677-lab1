from sockpeer import sockPeer
from multiprocessing import Process, current_process, active_children

#create peers
p1 = sockPeer('p1', None, 3, "127.0.0.1", 65010)
p2 = sockPeer('p1', None, 3, "127.0.0.1", 65435)

#start p1's server socket (listens for connections)
if __name__ == '__main__':
    #configure peer (child) process
    p = Process(target=p1.serverSock, args=())
    #start child process
    p.start()
    #check child id
    print(p.pid)
    #wait for child process to terminate
    p.join()


#p2 connects to p1 and sends data
#start p2's client socket
if __name__ == '__main__':
    #configure peer (child) process
    p = Process(target=p2.ClientSoc, args=("127.0.0.1", 65010))
    p.daemon = True
    #start child process
    p.start()
    #check child id
    print(p.pid)
    #wait for child process to terminate
    #p.join()

p1.closeSock()
p2.closeSock()
