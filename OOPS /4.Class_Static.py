import csv
 
class Item:
    pay_rate= 0.8  #pay rate after 20 percent of discount  #attribute on class level 
    all=[]
    def __init__(self, name:str, price:float, quantity=0):

        #Assign to self object
        self.name=name               #attribute Instance level
        self.price=price
        self.quantity=quantity

        #Run validation of recived arguments usinf ASSERT
        assert price>=0, f"Price {price} is not greater than or equal to zero"
        assert quantity >=0, f"Quantity {quantity} is not greater than zero!"   

        Item.all.append(self)

    def calculate_total_price(self,x,y):
        return x * y  


    def apply_discount(self):
        self.price= self.price * self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )   


    def __repr__(self):
        return f"Item('{self.name}', '{self.price}','{self.quantity}')"   



Item.instantiate_from_csv()
print(Item.all)