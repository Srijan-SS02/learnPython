class Item():
    after_discount=0.8

    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity= quantity

    def apply_discount(self):
        return self.price* self.after_discount


item1 =Item(name='Shirt', price=10, quantity=50)
print(f'The price of {item1.name} after discount is {item1.apply_discount()}')
item2 =Item(name='Pants', price=20, quantity=100)
print(f'The price of {item2.name} after discount is {item2.apply_discount()}')


item1.after_discount=0.7
print(f'The price of {item1.name} after discount is {item1.apply_discount()}')
print(f'The price of {item2.name} after discount is {item2.apply_discount()}')







