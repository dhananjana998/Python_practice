"""Student Record Manager
Concepts: open(), read(), write(), append()
"""

def add_student():
    """Add the student record to the file"""
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    marks = input("Enter student marks: ")
    # Open file in append mode to add data
    with open("students.txt", "a") as f:
        f.write(f"{name},{age},{marks}\n")
    print("\n Student record added successfully!\n")


def view_students():
    """View all student records"""
    try:
        with open("students.txt", "r") as f:
            print("\n--- All Student Records ---")
            data = f.read()
            if data == "":
                print("No records found!\n")
            else:
                print(data)
    except FileNotFoundError:
        print("\n File not found! No records exist yet.\n")


def search_student():
    """Search for a student by name"""
    search = input("Enter student name to search: ")
    found = False
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, age, marks = line.strip().split(",")
                if name.lower() == search.lower():
                    print(f"\n Found Record:")
                    print(f"Name: {name}, Age: {age}, Marks: {marks}\n")
                    found = True
                    break
        if not found:
            print("\n Student not found!\n")
    except FileNotFoundError:
        print("\n File not found! No records exist yet.\n")


# -------------- Main Menu --------------
while True:
    print("====== Student Record Manager ======")
    print("1. Add Student Record")
    print("2. View All Records")
    print("3. Search Student by Name")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-4.\n")


"""output :C:\Users\User\Desktop\SE_Skill\PythonProject9\.venv\Scripts\python.exe C:\Users\User\Desktop\SE_Skill\PythonProject9\Recordbook.py 
====== Student Record Manager ======
1. Add Student Record
2. View All Records
3. Search Student by Name
4. Exit
Enter your choice (1-4): 1
Enter student name: sachini
Enter student age: 23
Enter student marks: 78

 Student record added successfully!

====== Student Record Manager ======
1. Add Student Record
2. View All Records
3. Search Student by Name
4. Exit
Enter your choice (1-4): 1
Enter student name: prasad
Enter student age: 24
Enter student marks: 85

 Student record added successfully!

====== Student Record Manager ======
1. Add Student Record
2. View All Records
3. Search Student by Name
4. Exit
Enter your choice (1-4): 2

--- All Student Records ---
sachini,23,78
prasad,24,85

====== Student Record Manager ======
1. Add Student Record
2. View All Records
3. Search Student by Name
4. Exit
Enter your choice (1-4): 3
Enter student name to search: prasad

 Found Record:
Name: prasad, Age: 24, Marks: 85

====== Student Record Manager ======
1. Add Student Record
2. View All Records
3. Search Student by Name
4. Exit
Enter your choice (1-4): """