class Person:
    def __init__(self, fullname,  age: int, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'My name is {self.fullname} I am  {self.age} years old  {self.is_married}')


class Students(Person):

    def __init__(self, fullname,  age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def avarage(self):
        print(f'avarage marks:{round(sum(self.marks.values()) / len(self.marks), 1)}')


class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def sum_salary(self):
        if self.experience > 3:
             new_salary = round(self.salary + ((self.salary / 100 * 5) * (self.experience - 3)))
             print(new_salary)


student = Students("Kim Jennie", 20, "single", {
    "bio": 5,
    "phy": 4,
    "geo": 3})
print(f'Fullname: {student.fullname} Age: {student.age} Is_married: {student.is_married}'
       f' \n got {student.marks} points')



def create_students():
    student1 = Students("Sezim Aszkarbekova", 18, "no", {
        "bio": 5,
        "phy": 4,
        "geo": 3})
    student2 = Students("Temir Musa", 17, "yes", {
        "bio": 5,
        "phy": 4,
        "geo": 5})
    student3 = Students("Aladin Djin", 19, "no", {
        "bio": 5,
        "phy": 4,
        "geo": 5})
    result = [student1, student2, student3]

    return result


data = create_students()

for i in data:
    i.introduce_myself()
    print(i.marks)
    i.avarage()


sezim = Students("ahbhhh", 24, "no", {
    'bio': 5,
    'goe': 3,
    'qwerty': 4
})
sezim.avarage()
sezim = Teacher("Azamat Bek", 35, "yes", 5)
sezim.sum_salary()


girl_person = Person("Kim Jennie", 20, "single")
print(girl_person)
print(f'Fullname: {girl_person.fullname} Age: {girl_person.age} Is_married: {girl_person.marмried}')