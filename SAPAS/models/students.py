class Person:
    def __init__(self,student_id, student_name,  student_class, gender):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        self.gender = gender

class Student(Person):
    def __init__(self, student_id, student_name, student_class, gender, marks):
        super().__init__(student_id, student_name, student_class, gender)
        self.marks = marks