# student class
class Student:

    # class variables
    subjects_taken = 0
    total_marks = 0
    
    def __init__(self, name: str, marks: list, email: str):

        self.name = name
        self.marks = marks
        self.email = email

        # class variables can be accessed by using self or class name

        self.subjects_taken = len(self.marks)               # updates subjects taken for the particular object
        # Student.subjects_taken = len(self.marks)          # updates subjects taken for each of the objects

    def calc_avg(self):

        for mark in self.marks:
            self.total_marks += mark

        return self.total_marks / self.subjects_taken


stud1 = Student('shubham', [1,2,3,5], 'email@shubham.com')
stud2 = Student('shubh', [1,2,3,4,5], 'email2@shubham.com')
stud3 = Student('zxcv', [1,2,3,4,5,6,8,0], 'ertyu@shubham.com')

# print(stud1.name)
# print(stud1.subjects_taken)

avg_marks = stud3.calc_avg()
print(avg_marks)



