#Aubre A. Anderson
#Vehicle Info
#This application will take your input and list out the vehicle details
#sept. 9, 2022
class Vehicle:
    def __init__(self, input, type):
        self.input = input
        self.type = type
vehicleType = str(input("Enter Vehicle Type: "))



class Automobile(Vehicle):
    def __init__(self, input, type, year, make, model, doors, roof):
        super().__init__(input, type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

year = str(input("Enter Year: "))
make = str(input("Enter Make: "))
model = str(input("Enter Model: "))
doors = str(input("Enter doors: "))
roof = str(input("Enter roof: "))

print("Type: " + vehicleType)
print("Year: " +year,"Make: " + make,"Model: " + model, "Doors: " +  doors, "Roof: " + roof, sep="\n")