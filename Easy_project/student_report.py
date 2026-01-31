# students_data = {}
# while True:
#     
#     if choice == "1":
#         name = input("Enter student name: ")
#         roll_no = input("Enter student roll number")
#         marks_math = input("Enter math marks: ")
#         marks_english = input("Enter english marks: ")
#         marks_science = input("Enter science marks: ")
#         marks_geography = input("Enter geography marks: ")
#         students_data["name"] = name
#         students_data["roll_no"] = roll_no
#         students_data["marks_math"] = marks_math
#         students_data["marks_english"] = marks_english
#         students_data["marks_science"] = marks_science
#         students_data["marks_geography"] = marks_geography
#     elif choice == "2":
#         # for i, student in enumerate(students_data, start=1):
#         #     print(f"{i},{student}")
#         print(students_data)
    
#         break





# class Student():
#     def __init__(self,name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
    
#     def view(self):
#         print(f"{self.name} ")
    
#     def search():
#         pass
    
#     def update():
#         pass
#     def delete():
#         pass
    

# if choice == "1":
    
    
# student1 = Student("Kalam", "1", "98")  
# student1.view()
# # print(student1.name)

student_data = {}

def add_students():
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    marks = {}
    subjects = ["Hindi", "English", "Math"]
    for sub in subjects:
        marks[sub] = int(input(f"Enter marks for {sub}: "))
    students = {"name":name, "roll_no":roll_no, "marks":marks}
    student_data[roll_no] = students
    print(f"{name} has been added successfully.")
#viewing students
def view_students():
    print(student_data)
#search student by roll number
def search_student():
    roll_no = input("Enter roll number: ")
    if roll_no not in student_data:
        print("Does not exist in our database.")
    else:
        value = student_data[roll_no]
        print(value)
#updating details
def update_student():
    roll_no = input("Enter roll number to update details: ")
    if roll_no not in student_data:
        print("Does not exist in our database.")
    else:
    
        name = input("Enter name: ")
        marks = {}
        subjects = ["Hindi", "English", "Math"]
        for sub in subjects:
            marks[sub] = int(input(f"Enter marks for {sub}: "))
    
        students = {"name":name, "roll_no":roll_no, "marks":marks}

        student_data[roll_no] = students
        print("Details have been updated successfully.")
#deleting record
def delete_record():
    roll_no = input("Enter roll number to delete record: ")
    if roll_no not in student_data:
        print("Does not exist in our database")
    else:
        del student_data[roll_no]
        print("Deleted successfully.")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add new student(name,roll number,marks in subjects)")
    print("2. view all students")
    print("3. Search student by roll number")
    print("4. Update student details")
    print("5. Delete a student record")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_record()
    else:
        print("Invalid input")
        break