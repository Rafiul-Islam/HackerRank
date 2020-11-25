class Person:
    def __init__(self, initialAge):
        self.age = initialAge

    def amIOld(self):
        if self.__age < 13:
            print("You are young.")
        if self.__age >= 13 and self.__age < 18:
            print("You are a teenager.")
        elif self.__age >= 18:
            print("You are old.")

    def yearPasses(self):
        self.__age += 1
        return self.__age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            self.__age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.__age = value


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
