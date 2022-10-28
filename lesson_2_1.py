class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Person:
    def __init__(self, full_name, address):
        self.__full_name = full_name
        self.__address = address


class Animal:
    def __init__(self, age, name, address):
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Value for age attribute must be a positive number")
        else:
            self.__age = age
        self.__name = name
        if not isinstance(address, Address):
            raise ValueError("Value for address attribute must be an Address data type")
        else:
            self.__address = address
        self.__was_born()

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value for age attribute must be a positive number")
        else:
            self.__age = value

    def get_name(self):
        return self.__name

    def info(self):
        return f'Age: {self.__age} Name: {self.__name} Birth year: {self.calculate_birth_year()}\n' \
               f'Address: {self.__address.city}, {self.__address.street} {self.__address.number}'

    def calculate_birth_year(self):
        return 2022 - self.__age

    def __was_born(self):
        print(f'Animal {self.__name} was born. Heeeey')

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        if not isinstance(value, Address):
            raise ValueError("Value for address attribute must be an Address data type")
        else:
            self.__address = value

    def speak(self):
        #raise NotImplemented("Method speak must be implemented in all classes")
        pass


class Dog(Animal):
    def __init__(self, age, name, address, commands):
        super(Dog, self).__init__(age, name, address)
        self.__commands = commands

    @property
    def commands(self):
        print('Working getter of commands')
        return self.__commands

    @commands.setter
    def commands(self, value):
        print('Working setter of commands')
        self.__commands = value

    def info(self):
        return f'Commands: {self.__commands} ' + super().info()

    def speak(self):
        print("Gav Gav")


class Cat(Animal):
    def __init__(self, age, name, address):
        super(Cat, self).__init__(age, name, address)

    def speak(self):
        print("Myayu myayu")


class Fish(Animal):
    def __init__(self, age, name, address):
        super(Fish, self).__init__(age, name, address)


address = Address("Bishkek", "Chui", 221)
some_animal = Animal(2, "Barsik", address)
# some_animal.age = "Three"
some_animal.set_age(3)
print(some_animal.info())
snooppy_dog = Dog(1, "Snooppy", address, "Fight")
snooppy_dog.commands = "Fight, Sit"

# address_of_tom = Address("LA", "Walk Street", 77)
#    a          =   b
tom_cat = Cat(5, "Tom", Address("LA", "Walk Street", 77))
archi_cat = Cat(3, "Archi", address)
freddy_fish = Fish(16, "Freddy", Address("NY", "1st Avenue", 89))

animals_list = [snooppy_dog, tom_cat, freddy_fish, archi_cat]
for animal in animals_list:
    print(animal.info())
    animal.speak()