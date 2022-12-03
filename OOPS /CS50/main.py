class Student:                                #Class is student
    def __init__(self, name, house, patronus):  #init method
        self.name = name                        #these are instance variables  
        self.house =house
        self.patronus=patronus

    def __str__(self):
        return (f"{self.name} from {self.house}  patronus : {self.patronus}" )


    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"    

            case "Otter":
                return "🦦"

            case "Jack":
                return "🐶"

            case _:
                return "⚔️"            
def main():
    student = get_student()
    print("Expecto petronoum!")
    print (student.charm())




def get_student():

    name = input("Name: ")             #name, house and patronus are attributes of a class 
    house= input("house: ")
    patronus = input("patronus: ")
    student = Student(name, house, patronus)    #student is the object/Instance here of class Student 
    return student 

    
if __name__ == "__main__":
    main()