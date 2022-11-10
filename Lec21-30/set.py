# Sets are similar to lists but are printed in unordered way and also accepts no duplicate data 

setQ={'apple', 'banana', 'anyhting'}
print(setQ)


numA=[1,2,4,7,5]
numB=[4,5,1]

setA=set(numA)
setB=set(numB)
 
print(numA)
print(setA)

diff=setA.difference(setB)
print(diff) 
