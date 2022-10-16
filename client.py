import xmlrpc.client
import sys

proxy = xmlrpc.client.ServerProxy("http://localhost:6789")


def func():
    print("test!")


def send():
    proxy.updateCache('hello')

result = proxy.testFunc(num1, num2)
print("Result is:", result)

print(sys.argv)
proxy.updateCache(f'message is: {sys.argv[1]}')

t1.start()
t2.start()