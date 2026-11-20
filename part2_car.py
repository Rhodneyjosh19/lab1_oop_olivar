class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car1 = Car("Dodge", "Charger -", 2023)
car2 = Car("Nissan", "Skyline -", 2002)
car3 = Car("Toyota", "Supra -", 2020)

for number, car in enumerate([car1, car2, car3], start=1):
    print(f"Car {number}: {car.brand} {car.model} {car.year}")

print("Wheels:", Car.wheels)

print("type(car1):", type(car1))
print("isinstance(car1, Car):", isinstance(car1, Car))