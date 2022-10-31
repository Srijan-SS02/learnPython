num=int(input("Enter any no."))
fact=1
if num<1:
    print("Num is to small")

elif num>10:
    print("factorial is to large")

else :
    while num>1:
        fact=fact*num
        num=num-1

    print(fact)    