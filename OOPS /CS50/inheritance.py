class Wizard:
    def __init__(self,name):
        if not name :
            raise ValueError("Name Missing")

        self.name=name 
    ...

class Professor(Wizard):
    def __init__(self,subject,name):
        super().__init__(name)
        self.subject=subject


class Student(Wizard):
    def __init__(self, name,house):
         super().__init__(name)
         self.house=house



wizard=Wizard("Albus")
student=Student("Harry","Gryffindor")
professor=Professor("Severus","Deffence Against the Dark Magic")