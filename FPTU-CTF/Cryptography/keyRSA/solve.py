from pwn import *
from Crypto.Util.number import inverse
from gmpy2 import lcm, iroot

#con = remote('127.0.0.1', 4444)
con = process('./enc.bin')
con.recvuntil(b'Press "y" for Yes and "n" for No (case sensisitive) : ')
con.sendline(b'y')

con.recvline()
con.recvline()

e = int(con.recvline()[4:-1])
n = int(con.recvline()[4:-1])
x = int(con.recvline()[4:-1])

p = x
q = n // p

d = inverse(e,lcm((p-1),(q-1)))

con.recvuntil(b'Enter your key : ')
con.sendline(str(d).encode())

con.interactive()



