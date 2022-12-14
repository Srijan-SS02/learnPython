class Student:                                #Class is student
    def __init__(self, name, house):  #init method
        
        self.name = name                        #these are instance variables  
        self.house =house
        # self.patronus=patronus

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


    # def charm(self):                                #Custom method
    #     match self.patronus:
    #         case "Stag":
    #             return "🦌"    

    #         case "Otter":
    #             return "🦦"

    #         case "Jack":
    #             return "🐶"

    #         case _:
    #             return "⚔️"            


def main():
    student = get_student()
    print(student)
    # student.house="lksjfslfj"
    # print("Expecto petronoum!")
    # print (student.charm())




def get_student():

    name = input("Name: ")             #name, house and patronus are attributes of a class 
    house= input("house: ")
    # patronus = input("patronus: ")
    student = Student(name, house)    #student is the object/Instance here of class Student 
    return student 

    
if __name__ == "__main__":
    main()