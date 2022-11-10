class employee():
    def __init__(self,name, salary) -> None:
        self.name=name
        self.salary=salary

class bartender(employee):
    def __init__(self, name ) -> None:
        super().__init__(name, salary='3000')


class chef(employee):
    pass


bartender1=bartender(name="Harry")
bartender2=bartender(name="Ron")
print(bartender1.name)
print(bartender2.name , "\n")
print(bartender1.salary)

chef1=chef(name="Hermionee", salary=25000)
print(chef1.name)

