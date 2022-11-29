class Item:
    def __init__(self, name:str, price:float, quantity=0):
        
        self.name=name
        self.price=price
        self.quantity=quantity
    #Run validation of recived arguments usinf ASSERT
        assert price>=0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!"   

    def calculate_total_price(self,x,y):
        return x * y  

        


item1=Item("Phone",100)
print(item1.name)
x=item1.calculate_total_price(item1.price , item1.quantity )
print (x)


item2= Item("Laptop",1000, 3)
print(item2.price)
y=item1.calculate_total_price(item2.price , item2.quantity)
print(y)


item3= Item("Heater",900, -3)
print(item3.price)
y=item3.calculate_total_price(item3.price , item3.quantity)
print(y)