# == , <=, >= , !=  ,< ,>, in

from genericpath import exists
from operator import is_


water_price = 7
is_expensive = water_price >=5
print(is_expensive)

if is_expensive == True:    # 'not' can also be used 
    print("habibi")
else:
    print("no habibi")    

name="Srijan"
exists= 't' in name
print(exists)