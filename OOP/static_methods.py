# person class

class Person:

    def __init__(self, age):
        self.age = age

    def check_age(self):
        self.age_group(self.age)

    @staticmethod
    def age_group(age):
        if age < 13:
            print('person is child')
        elif age > 45:
            print('person is old')
        else:
            print('person is adult')


# checking age of person object
person1 = Person(55)
person1.check_age()

# directly calling age_group function using class
Person.age_group(10)