ip=['192.168.10.1','192.168.10.20','192.168.10.100','192.168.10.9','192.168.10.5']

def func(x):
      b=x.split('.')
      return int(b[-1])

ip.sort(key=func)
print(ip)
