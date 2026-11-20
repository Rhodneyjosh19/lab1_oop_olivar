class Car:
    wheels = 4

    def __init__(self, brand, model, year, mileage=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, km):
        if km < 0:
            print("Error: distance cannot be negative.")
        else:
            self.mileage += km

    def age(self, current_year):
        return current_year - self.year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model} – {self.mileage} km"


car1 = Car("Dodge", "Charger", 2023)
car2 = Car("Nissan", "Skyline", 2002)

car1.drive(100)
car1.drive(50)
car1.drive(-20)

car2.drive(200)
car2.drive(75)
car2.drive(25)

print(car1)
print(car2)
print("Age of car1:", car1.age(2026), "years")
print("Age of car2:", car2.age(2026), "years")