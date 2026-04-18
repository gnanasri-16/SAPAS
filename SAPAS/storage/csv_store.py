import csv


FILE_NAME = "data.csv"

#  Save data to CSV
def save_csv(data):
    try:
        with open(FILE_NAME, "w", newline="") as f:
            w = csv.writer(f)

            # Header
            w.writerow(["ID", "Name", "Class", "Gender", "Marks"])

            # Data
            for s in data.values():
                w.writerow([s.student_id, s.student_name, s.student_class, s.gender, s.marks])

        print("Data saved to CSV!")

    except Exception as e:
        print("Error saving CSV:", e)


#  Load data from CSV
def load_csv():
    data = {}

    try:
        with open(FILE_NAME, "r") as f:
            r = csv.reader(f)
            next(r)

            for row in r:
                student_id, student_name, student_class, gender, marks = row
                data[student_id] = Student(student_id, student_name, student_class, gender, int(marks))

        print("Data loaded from CSV!")

    except FileNotFoundError:
        print("CSV file not found")

    except Exception as e:
        print("Error loading CSV:", e)

    return data


#  Append single record
def append_csv(student):
    try:
        with open(FILE_NAME, "a", newline="") as f:
            w = csv.writer(f)
            w.writerow([student.student_id, student.student_name, student.student_class, student.gender, student.marks])

        print("Student added to CSV!")

    except Exception as e:
        print("Error appending:", e)


#  Delete record from CSV
def delete_csv(student_id):
    try:
        data = load_csv()

        if student_id in data:
            del data[student_id]
            save_csv(data)
            print("Deleted from CSV!")
        else:
            print("ID not found")

    except Exception as e:
        print("Error deleting:", e)