from Crypto.Util.number import *
from math import gcd

n =  81120097948660064963760363050224942579193189658348303705417893337169638307930351045249862762611157186996852696621784130049967859671648623160495105395190069314659009235762286765210860898811784296123193952250059910523047202326030491416120053059504011321595408304983860432724425092826960453007550936094304250963
c1 =  45542186634979818062894508292378753199478347063475697933499959697412788876807522856025815165018689983246356097240196880132597170468962860463199963360111660016494444108422393986533159592722480873081672381024281364897042977740113819516183806738336958274218078682579800284758665877467676683984973821673759803463
c2 =  6259323892279367679323225674356195466045260619714530100569015926670850676458507016827519096626664770457854380432846957698467052357514606396208880352441451
e =  65537


p = gcd((c1-c2)%n, n)
q = n // p

phi = (p-1) * (q-1)
d = pow(e, -1, phi)

flag = pow(c1, d, n)
print(long_to_bytes(flag).decode())

