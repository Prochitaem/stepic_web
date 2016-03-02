import socket, sys
from thread import *

host = '127.0.0.1' ## 172.17.1.39
port = 2222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Starting server...'
try:
    s.bind((host,port))
except socket.error as err:
    print 'Server returned error: Code'+ str(err[0])+' description: ' +str(err[1])
    sys.exit()
print 'Server started!'
s.listen(10)
def clientthread(conn):
    print 'Start recieving data...'
    while True:
        data = conn.recv(1024)
        reply = data
        if reply == 'close':
            print 'Bye-Bye...'
            conn.close()
            break
        if not data:
            break
        conn.sendall(reply)
    conn.close()
while 1:
    conn, addr = s.accept()
    print 'Established conn: ' + str(addr[0])+':' + str(addr[1])
    start_new_thread(clientthread ,(conn,))
    ##start_new_thread(clientthread(conn))
s.close()