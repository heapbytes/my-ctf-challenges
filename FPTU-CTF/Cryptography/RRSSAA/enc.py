## Source code
from Crypto.Util.number import bytes_to_long, getPrime
from sympy import nextprime
from secret import flag

c1 = flag[:35].encode()
c2 = flag[35:].encode()

e = 65537

p1 = q1 = r1 = s1 = getPrime(512)
n1 = p1 * q1 * r1 * s1

msg1 = bytes_to_long(c1)
ct1 = pow(msg1, e, n1)

p2 = getPrime(1024)
q2 = nextprime(p2)
n2 = p2 * q2

msg2 = bytes_to_long(c2)
ct2 = pow(msg2, e, n2)


print(f'e = {e}')
print(f'n1 = {n1}')
print(f'ct1 = {ct1}')

print(f'n2 = {n2}')
print(f'ct2 = {ct2}')

