# employee class
class Employee:
    
    def __init__(self, firstName: str, lastName: str, salary: int):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def fullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def doubleSalary(self):
        self.salary = 2 * self.salary

emp1 = Employee('asdfg', 'asdfgh', 45000)
emp2 = Employee('zxcvb', 'hjkl', 55000)

# print(emp1.salary)
# print(emp2.salary)

# print(emp1.fullName())
# print(emp2.fullName())

# print(emp1.salary)
# emp1.doubleSalary()
# print(emp1.salary)

# class methods can be called directly passing objs as argumnet
Employee.doubleSalary(emp1)
print(emp1.salary)

print(Employee.fullName(emp2))