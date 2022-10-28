class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu
    @cpu.setter
    def cpu(self, value):
             self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def __str__(self):
        return f'cpu: {self.__cpu} memory: {self.__memory}'

    def __gt__(self, other):
        return self.__memory > other.cpu

    def __lt__(self, other):
        return self.__memory < other.cpu


    def make_computations(self):
        print(f'{self.__cpu}  += {self.__memory} = {self.__cpu + self.memory}')
class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def __str__(self):
        return f'Name: {self.sim_cards_list} '

    def call(self, sim_card_number, call_to_number):

        self.sim_card_number = sim_card_number
        self.call_to_number = call_to_number


        print(f"идёт звонок на номер: {self.sim_card_number} с сим-карты: {self.call_to_number}")

class SmartPhone(Computer, Phone):

    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def __str__(self):
        return f'CPU: {self.cpu} memory: {self.memory} sim_cards_name: {self.sim_cards_list}'

    def use_gps(self, location):
        print(f'you are in {location}')

mac_computer = Computer(218, 512)
print(mac_computer)
mac_computer.make_computations()
print(Computer.mro())

some_phone = Phone("beeline")
print(some_phone)
some_phone.call(996777998811, "O!")
print(Phone.mro())

sumsung_smartphone = SmartPhone("Exynos 7", 256, "O!")
print(sumsung_smartphone)
sumsung_smartphone.use_gps("osh")

apple_smartphone = SmartPhone("Apple A4", 512, "MegaCome")
print(apple_smartphone)
apple_smartphone.use_gps("Batken")
print(SmartPhone.mro())



