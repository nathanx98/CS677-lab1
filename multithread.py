import client
import server
import threading


def run():
    threads = []

    threads.append(
        threading.Thread(target=server.startServer),
        threading.Thread(target=client.clientFunc)
    )

    for thread in threads:
        thread.start()
    
    for thread in threads:
        thread.join()