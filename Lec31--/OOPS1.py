# classes have two parameters field and method 
# This is field




class Person():
    pass


person1 =Person()

person1.name="Harry"
person1.age=20
person1.college="Hogwarts"

print(person1.name)
print(person1.age)
print(person1.college)

# This is method

class car():
    def car_name(self, name):
        print(name)


car2=car()
car2.car_name(name="Jim")



class Drinks():
    Pepsi="coldrink"
    coffee="hotdrink"


print(Drinks.Pepsi)    



#When you use __init__ function / using constructor for making function in class
class CAR():
    def __init__(self,name,hp) -> None:
        print(name,hp)


carX=CAR(name="Lamborghini", hp="750KWH")


class bike():
    def __init__(self,name,motor) -> None:
        self.Name=name
        self.motor=motor


bikeX=bike(name="BMW", motor="ABC")
print(bikeX.Name)
print(bikeX.motor)


