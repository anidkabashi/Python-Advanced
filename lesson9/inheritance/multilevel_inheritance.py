from PIL.Image import module


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.nodul = module
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Modul: {self.modul}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, make, modul, year, body_style):
        super().__init__(make,modul,year)
        self.body_style = body_style

class ElectricCar(Car):
    def __init__(self,make,modul, year, body_style, battery_capacity):
        super().__init__(make,module, year, body_style)
        self.battery_capacity= battery_capacity

    def charge(self):
        print("Charging the electric car")

tesla = ElectricCar("Tesla", "Cybertruck", "2023", "triangular", 122.4)
print("Battery Capacity", tesla.battery_capacity)
tesla.charge()