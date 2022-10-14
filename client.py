import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:6789")
num1 = 12
num2 = 31

result = proxy.testFunc(num1, num2)
print("Result is:", result)