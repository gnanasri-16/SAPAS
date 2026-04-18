class Record:
    def __init__(self, student, subjects):
        self.student = student
        self.subjects = subjects

    #  Display full record
    def show(self):
        print("\n--- Student Details ---")
        print("ID:", self.student.student_id)
        print("Name:", self.student.student_name)
        print("Class:", self.student.student_class)
        print("Gender:", self.student.gender)

        print("\n--- Subjects ---")
        for sub in self.subjects:
            print(sub.name, "-", sub.marks)

    #  Calculate total marks
    def total(self):
        return sum(sub.marks for sub in self.subjects)

    #  Calculate average
    def average(self):
        if not self.subjects:
            return 0
        return self.total() / len(self.subjects)

    #  Find highest subject
    def highest(self):
        return max(self.subjects, key=lambda x: x.marks)

    #  Find lowest subject
    def lowest(self):
        return min(self.subjects, key=lambda x: x.marks)

    #  Check overall result
    def result(self):
        for sub in self.subjects:
            if sub.marks < 40:
                return "Fail"
        return "Pass"

