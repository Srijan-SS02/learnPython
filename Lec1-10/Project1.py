#Sell Coustomer areas Episode10 Project1

price_summer=2000          #per square unit
discount_percentage=25     #for winter
pay_percentage =100-discount_percentage

price_winter=(pay_percentage/100)*price_summer
 

name=str(input("Hello, what is yourn name: "))
width=float(input("Enter widht of your area: "))
height=float(input("Enter height of your area: "))

req_area_to_buy=width*height

price_total_summer=price_summer*req_area_to_buy
price_total_winter=price_winter*req_area_to_buy


print(f"""
Hello {name.title()}
If you want to sell in summer you can sell it for ${price_total_summer}.
But, if you want to sell in winter, there will be {discount_percentage}%
So the price will be ${price_total_winter}.
Thanks for visiting.
""")