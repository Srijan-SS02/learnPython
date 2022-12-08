import random 
class Hat:
    
    houses = ["Gryffindor", "Huffelpuf","Ravenclaw","Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



# hat = Hat()     NOT NEEDED NOW
Hat.sort("Harry") 