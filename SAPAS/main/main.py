import pandas as pd
import numpy as np
import json
import csv
import matplotlib as mp

data = {}
class Student:
    def __init__(self, student_id, student_name, student_class, gender, marks):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = student_class
        self.gender = gender
        self.marks = marks




# ADD STUDENT
def add():
    try:
        student_id = input("Enter ID: ").strip()

        if not  student_id:
            print(" ID cannot be empty")
            return

        if  student_id in data:
            print(" ID already exists!")
            return

        student_name = input("Enter Name: ")
        student_class = input("Enter Class: ").strip()
        gender = input("Enter Gender: ").strip()

        marks = int(input("Enter Marks: "))


        data[ student_id] = Student( student_id,  student_name, student_class, gender, marks)
        print(" Student Added!")

    except ValueError as e:
        print(" Error:", e)


#  DISPLAY ALL
def display():
    if not data:
        print(" No records found")
        return

    print("\n--- Student Records ---")
    for s in data.values():
        print(f"ID:{s.student_id} | Name:{s.student_name} | Class:{s.student_class} | Gender:{s.gender} | Marks:{s.marks}")


#  SEARCH
def search():
    student_id = input("Enter ID to search: ").strip()

    if student_id in data:
        s = data[student_id]
        print(f"Found -> ID:{s.student_id}, Name:{s.student_name}, Class:{s.student_class}, Gender:{s.gender}, Marks:{s.marks}")
    else:
        print(" Student not found")


#  DELETE
def delete():
    student_id = input("Enter ID to delete: ").strip()

    if student_id in data:
        del data[student_id]
        print("Student deleted")
    else:
        print(" Student not found")


#  GRADE
def grade():
    student_id = input("Enter ID: ").strip()

    if student_id not in data:
        print(" Student not found")
        return

    marks= data[student_id].marks

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f" Grade of {data[student_id].name}: {grade}")


# 🔹 LOAD DATA SAFELY
def load_data():
    loaded = load_json()
    if loaded:
        data.update(loaded)
        print(" Data Loaded Successfully")
    else:
        print(" No data loaded")


#  SHOW TOPPER SAFELY
def show_topper():
    if not data:
        print(" No data available")
        return

    t = topper(data)
    print(f" Topper -> {t.student_name} ({t.marks})")


#  TOTAL
def show_total():
    if not data:
        print("No data")
        return
    print(" Total Marks:", total(data))


#  AVERAGE
def show_average():
    if not data:
        print("️ No data")
        return
    print("Average Marks:", round(average(data), 2))


# 🔹 MENU
def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Total Marks")
        print("6. Average Marks")
        print("7. Topper")
        print("8. Grade")
        print("9. Save to JSON")
        print("10. Load from JSON")
        print("11. Save to CSV")
        print("12. Show Graph")
        print("13. Exit")

        ch = input("Enter choice: ").strip()

        if ch == '1':
            add()
        elif ch == '2':
            display()
        elif ch == '3':
            search()
        elif ch == '4':
            delete()
        elif ch == '5':
            show_total()
        elif ch == '6':
            show_average()
        elif ch == '7':
            show_topper()
        elif ch == '8':
            grade()
        elif ch == '9':
            save_json(data)
            print(" Saved to JSON")
        elif ch == '10':
            load_data()
        elif ch == '11':
            save_csv(data)
            print(" Saved to CSV")
        elif ch == '12':
            show_graph(data)
        elif ch == '13':
            print("Exiting program...")
            break
        else:
            print("Invalid choice")


# 🔹 RUN PROGRAM
if __name__ == "__main__":
    menu()