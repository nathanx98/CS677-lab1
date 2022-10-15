import xmlrpc.client

class client:
    
    def __init__(self, proxyaddr):
        self.proxyaddr = proxyaddr
    
    def startProxy(self):
        proxy = xmlrpc.client.ServerProxy(self.proxyaddr)
        self.proxy = proxy

    def run(self, num1, num2):
        return self.proxy.testFunc(num1, num2)

if __name__ == '__main__':
    myclient = client("http://localhost:6799")
    myclient.startProxy()
    res = myclient.run(12, 31)
    print("Result is:", res)
