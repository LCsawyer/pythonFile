from urllib import urlopen

'''
import socket

s = socket.socket()

host = socket.gethostname()
#print host
port = 1234
s.bind((host,port))

s.listen(5)

while True:
	c , addr = s.accept()
	print 'Got connection from',addr
	c.send('thank you for connecting')
	print c.recv(1024)
	c.close()
'''

webp = urlopen('https://www.baidu.com')
txt = webp.read()
print txt
