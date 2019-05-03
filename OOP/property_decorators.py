# product class
class Person:

    def __init__(self, firstName: str, lastName: str, age: int):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    @property
    def email(self):
        return "{}.{}@email.com".format(self.firstName, self.lastName)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    @property
    def ageValue(self):
        return self.age

    def __repr__(self):
        return "Person({}, {}, {})".format(self.fullname, self.age, self.email)

    @ageValue.setter
    def ageValue(self, ageValue):
        self.age = ageValue

    
person1 = Person('shubham', 'pandey', 22)
print(person1)
print(person1.email)

person1.ageValue = 23
print(person1)