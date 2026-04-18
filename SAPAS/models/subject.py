class Subject:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

    #  Display subject details
    def show(self):
        print("Subject:", self.student_name, "| Marks:", self.marks)

    #  Check pass/fail
    def is_pass(self):
        return self.marks >= 40

    # Get grade
    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"