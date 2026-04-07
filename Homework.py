class BMW:
    def fueltype(self):
        print("BMW uses petrol")
    def maxspeed(self):
        print("BMW max speed is 240")

class Ferrari:
    def fueltype(self):
        print("Ferrari uses premium gas")
    def maxspeed(self):
        print("Ferrari max speed is 340")

car1 = BMW()
car2 = Ferrari()

for car in (car1, car2):
    car.fueltype()
    car.maxspeed()
    print("-" * 20)