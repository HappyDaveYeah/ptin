__author__ = 'dmicomrt'
import socket

HOST = ''                 # Symbolic name meaning the local host
PORT = 8088              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(2)


conn1, addr = s.accept()
print 'connected by ' , addr
conn2, addr = s.accept()
print 'connected by ' , addr

for i in range (10):
    print 'hello waiting'
    data = conn2.recv(1024)
    print 'hello sending'
    conn1.send('Hello')

conn1.close()
conn2.close()
