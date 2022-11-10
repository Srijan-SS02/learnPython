class employee():
    def __init__(self,name) -> None:
        self.name=name

class bartender(employee):
    pass


class chef(employee):
    pass


bartender1=bartender(name="Harry")
print(bartender1.name)

chef1=chef(name="Hermionee")
print(chef1.name)
