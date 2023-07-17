from Crypto.Util.number import getPrime, bytes_to_long, GCD

flag = open('flag.txt', 'r').read()
flag = list(flag)

p = getPrime(96)
q = getPrime(96)

e = 65537
n = p * q
assert GCD(e,n) == 1

ct = []
for i in flag:
    ct.append( pow(  bytes_to_long(i.encode()),e,n) )

print(f'{ct = }')
print(f'{n = }')
print(f'{e = }')

