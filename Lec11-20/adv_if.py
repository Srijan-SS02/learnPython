hungry= str(input("Hungry ?? y/n")).lower()
diet= str(input("diet ?? y/n")).lower()

is_hungry= hungry=='y'
is_diet= diet=='y'

if( not is_hungry and not is_diet):
    print("Have a beer")

if( not is_hungry and is_diet):
    print("Have weed")

    