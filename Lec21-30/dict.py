person= {
    "name": "Harry",
    "age": 20,
    "phone_number":1122334455,
    "height":128
}

print(person,"\n")
print(person.items(),"\n")
print(person.keys(),"\n")
print(person.values(),"\n")
print(person["name"],person["height"])


for key, values in person.items():
    print(f'The values of {key} is {values}')

print(person.get('age'))
print(person.get('age'))    

