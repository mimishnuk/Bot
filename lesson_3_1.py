class MusicPlayable:
    # def __init__(self):
    #     pass

    def play_music(self, song_name):
        print(f"Now is playing {song_name}")


class SmartPhone(MusicPlayable):
    pass


class Car(MusicPlayable):
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    def drive(self):
        print(f'{self.__model} is driving')

    def __str__(self):
        return f'Model: {self.__model} Year: {self.__year}'

    def __gt__(self, other):
        return self.year > other.year

    def __lt__(self, other):
        return self.year < other.year


class FuelCar(Car):
    __total_fuel_amount = 1000

    def __init__(self, model, year, fuel_bank):
        Car.__init__(self, model, year)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank
        # FuelCar.__total_fuel_amount = FuelCar.__total_fuel_amount - self.__fuel_bank

    @staticmethod
    def get_fuel_type():
        return "AI - 95"

    @classmethod
    def show_total_fuel_amount(cls):
        print(f"Remains {cls.__total_fuel_amount}")

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    @fuel_bank.setter
    def fuel_bank(self, value):
        self.__fuel_bank = value

    def drive(self):
        print(f'{self.model} is driving by using fuel')

    def __str__(self):
        return Car.__str__(self) + f' Fuel bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.fuel_bank + other.fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        Car.__init__(self, model, year)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'{self.model} is driving by using elecricity')

    def __str__(self):
        return Car.__str__(self) + f' Battery: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, fuel_bank, battery):
        FuelCar.__init__(self, model, year, fuel_bank)
        ElectricCar.__init__(self, model, year, battery)

    # def drive(self):
    #     print(f'{self.model} is driving by using elecricity or fuel')

    def __str__(self):
        return FuelCar.__str__(self) + f" Battery: {self.battery}"


some_car = Car("Toyota Camry", 2010)
print(some_car)

fuel_car = FuelCar("Honda Civic", 2017, 55)
print(fuel_car)

electric_car = ElectricCar("Tesla Model X", 2021, 25000)
print(electric_car)

hybrid_car = HybridCar("Toyota Prius", 2008, 45, 20000)
print(hybrid_car)
hybrid_car.drive()
print(HybridCar.mro())

number_1 = 8
number_2 = 5
print(number_1 > number_2)

print(fuel_car > hybrid_car)
print(fuel_car + hybrid_car)

# FuelCar.__total_fuel_amount = 500
FuelCar.show_total_fuel_amount()
print("Fuel type: " + FuelCar.get_fuel_type())