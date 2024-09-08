from Crypto.Util.number import bytes_to_long, getPrime
#from secret import flag

import sys
import socket
import threading
import socketserver
import signal

host, port = '0.0.0.0', 5000
BUFF_SIZE = 2048
flag = b'FPTUHacking{Y0u_kn0w_t0_CR34t3_y0ur_0wn_k3y!!!}'

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def generation(self):
        p, q = getPrime(512), getPrime(512)
        n = p * q
        e = 65537

        msg = bytes_to_long(flag)

        assert n > msg
        ct = pow(msg,e,n)

        phi = (p-1) * (q-1)
        d = pow(e,-1,phi)

        self.request.sendall(b'Do you want to try your own key? [ y/n ] : ) ')
        yn = (self.request.recv(BUFF_SIZE).strip())
        if yn.decode() == 'y':

            self.request.sendall(b'\nSure, here are your keys \n')
            self.request.sendall(b'\ne = ' + str(e).encode())
            self.request.sendall(b'\nn = ' + str(n).encode())
            self.request.sendall(b'\nx = ' + str(p % (n // 2)).encode())

            self.request.sendall(b'\nEnter your key :  \n')
            user_d = int((self.request.recv(BUFF_SIZE).strip()).decode())
            if user_d != d:
                if pow(ct,user_d,n) == pow(ct,d,n):
                    self.request.sendall(flag)
                else:
                    self.request.sendall(b'Better luck next time !!')
                    exit(0)
            else:
                self.request.sendall(b"Sorry you can't use my key, or maybe our keys were similar this time, try again !!")
                exit(0)
        else:
            self.request.sendall(b'See you next time')
            exit(0)
    
    def handle(self):
        self.request.settimeout(30)     
        self.generation()

def main():
    server = ThreadedTCPServer((host, port), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    server_thread.join()

if __name__=='__main__':
    main()
