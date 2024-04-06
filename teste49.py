import math 
import time
#print(math.ceil(3.2))
#print(math.floor(3.2))
#ven=[200,230,500]
#print(math.fsum(ven))
#print(math.sqrt(16))
#print(time.localtime())
hora=time.localtime().tm_hour
minuto=time.localtime().tm_min
print(str(hora)+':'+str(minuto))
