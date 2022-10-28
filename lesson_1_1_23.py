class Transport:
    def __init__(self, the_model, the_color, the_year):
        self.model = the_model
        self.color = the_color
        self.year = the_year

    def change_color(self, new_color):
        self.color = new_color


class Car(Transport):
    # class attribute
    wheels = 4

    # constructor
    def __init__(self, the_model, the_color, the_year, penalties=0.0):
        # attributes / fields
        super().__init__(the_model, the_color, the_year)
        self.penalties = penalties

    # method
    def drive(self, city):
        print(f'Car {self.model} {self.color} is driving to {city}')


class Truck(Car):
    wheels = 10
    def __init__(self, the_model, the_color, the_year, penalties=0.0, load_capacity = 0.0):
        super().__init__(the_model, the_color, the_year, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, cargo_weight, perishable):
        if cargo_weight > self.load_capacity:
            print(f"Overweight, you can load up to {self.load_capacity}")
        else:
            print(f'Truck {self.model} was successfully loaded with {perishable}')

class Plane(Transport):
    def __init__(self, the_model, the_color, the_year):
        super().__init__(the_model, the_color, the_year)


print(f"We need {Car.wheels * 5000 * 10} soms")

bmw_car = Car("BMW X6", "Blue", 2020)
print(bmw_car)
print(f'Model: {bmw_car.model} Color: {bmw_car.color} Year: {bmw_car.year} '
      f'Penalties: {bmw_car.penalties} Number of wheels: {bmw_car.wheels}')

honda_car = Car(the_year=2009, the_model="Honda CR-V",
                the_color="Silver", penalties=900.0)
print(f'Model: {honda_car.model} Color: {honda_car.color} Year: {honda_car.year} '
      f'Penalties: {honda_car.penalties} Number of wheels: {honda_car.wheels}')
# honda_car.color = "Black"
honda_car.change_color("Black")
print(f'Model: {honda_car.model} Color: {honda_car.color} Year: {honda_car.year} '
      f'Penalties: {honda_car.penalties} Number of wheels: {honda_car.wheels}')
bmw_car.drive("Osh")
honda_car.drive("Bishkek")

Car.wheels = 5

kia_car = Car("Kia K5", "White", 2022)
print(f'Model: {kia_car.model} Color: {kia_car.color} Year: {kia_car.year} '
      f'Penalties: {kia_car.penalties} Number of wheels: {kia_car.wheels}')

airbus_plane = Plane("Airbus 320", "White", 2020)
print(f'Model: {airbus_plane.model} Color: {airbus_plane.color} Year: {airbus_plane.year}')
airbus_plane.change_color("Green")
print(f'Model: {airbus_plane.model} Color: {airbus_plane.color} Year: {airbus_plane.year}')

volvo_truck = Truck("Volvo 500", "Silver", 2000, 15000, 30000)

print(f'Model: {volvo_truck.model} Color: {volvo_truck.color} Year: {volvo_truck.year} '
      f'Penalties: {volvo_truck.penalties} Number of wheels: {volvo_truck.wheels} '
      f'Load capacity: {volvo_truck.load_capacity}')
volvo_truck.drive("LA")
volvo_truck.load_cargo(35000, "Fish")
volvo_truck.load_cargo(25000, "Fish")