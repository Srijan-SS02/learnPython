monthly_salary=int(input("Enter your salary"))
age= int (input("Enter your age "))

if age <=24:
    bonus=  500
    monthly_salary+=bonus

else:
    bonus=1000
    monthly_salary+=bonus


print(monthly_salary )


