from peer import peer
from multiprocessing import Process, current_process, active_children
import os

#basic checks
test = peer( 3, "none" , 12345)
test.setmyrole()
print(test.myrole)
test2 = peer( 3, "none", 12346 )
test2.setmyrole()
print(test2.myrole)
test.setmyrole('fish_seller')
print(test.myrole)

mytestpeer = peer(3, 'none', 12345)
mytestpeer.newserversock(54321)
#mytestpeer.main_loop()


exec(open("server.py").read())
exec(open("client.py").read())











#now as a process
if __name__ == '__main__':
    #configure peer (child) process
    p = Process(target=peer, args=( 3, "none", 8080 ))
    #start child process
    p.start()
    #check child id
    print(p.pid)
    #wait for child process to terminate
    p.join()
    
print(current_process())

active = active_children()
print(active_children())
# terminate all active children
for child in active:
    child.terminate()
