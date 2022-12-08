class Student:                                #Class is student
    def __init__(self, name, house):  #init method
        
        self.name = name                        #these are instance variables  
        self.house =house

    def __str__(self):
        return (f"{self.name} from {self.house}  " )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")

    @property
    def house(self):
        return self._house


    @house.setter
    def house(self, house):
            if house not in["Gryffindor", "Hufflepuff","Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")  

            self._house=house

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


    
if __name__ == "__main__":
    main()