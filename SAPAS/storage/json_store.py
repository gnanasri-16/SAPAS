import json


FILE_NAME = "data.json"

#  Save data to JSON
def save_json(data):
    try:
        # Convert objects to dictionary
        records = [vars(s) for s in data.values()]

        with open(FILE_NAME, "w") as f:
            json.dump(records, f, indent=4)

        print("Data saved successfully!")

    except Exception as e:
        print("Error saving data:", e)


# Load data from JSON
def load_json():
    new_data = {}

    try:
        with open(FILE_NAME, "r") as f:
            records = json.load(f)

            for d in records:
                student = Student(**d)
                new_data[d['student_id']] = student

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("File not found, starting fresh.")

    except json.JSONDecodeError:
        print("File is empty or corrupted.")

    except Exception as e:
        print("Error loading data:", e)

    return new_data


# Append single student (extra feature)
def append_json(student):
    try:
        data = load_json()
        data[student.student_id] = student
        save_json(data)
        print("Student appended!")

    except Exception as e:
        print("Error appending:", e)


#  Delete student from file
def delete_json(student_id):
    try:
        data = load_json()

        if student_id in data:
            del data[student_id]
            save_json(data)
            print("Deleted from file!")
        else:
            print("ID not found")

    except Exception as e:
        print("Error deleting:", e)