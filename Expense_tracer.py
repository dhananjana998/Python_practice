#simple expense tracker
from unicodedata import category


def show_menu():0
print("\n----------------------Expense Tracker----------------------\n")
print("1.Add Expense")
print("2.View Expenses")
print("3.Exit")

def add_expense():
    try:
        date=input("Enter Date(YYYY-MM--DD): ")
        category=input("Enter Category Name(eg:Food,Travel,etc:")
        amount=float(input("Enter amount:"))
        description=input("Enter Description:")

        with open("expenses.txt","a") as file:
            file.write(f"{date},{category},{amount},{description}\n")
        print("Expense added successfully!")
    except ValueError:
        print("pleace enter valid number for amount.")
    except Exception as e:
        print("Error:",e)

def view_expenses():
    try:
        with open("expenses.txt","r") as file:
            print("\n-----All Expenses-----")
            for line in file:
                date,category,amount,description=line.strip().split(",")
                print(f"{date}|{category}|{amount}|{description}\n")
    except FileNotFoundError:
        print("No expenses file")


#main program

while True:
    show_menu()
    choice=input("Enter Your Choice:(1-3)  \t")

    if choice=="1":
        add_expense()
    elif choice=="2":
        view_expenses()
    elif choice=="3":
        print("Thank you for using the Expense Tracker.")
        break
    else:
        print(" Invalid choice! Please enter 1, 2, or 3.")




"""output:

C:\Users\User\Desktop\SE_Skill\PythonProject9\.venv\Scripts\python.exe C:\Users\User\Desktop\SE_Skill\PythonProject9\Expense_tracer.py 

----------------------Expense Tracker----------------------

1.Add Expense
2.View Expenses
3.Exit
Enter Your Choice:(1-3)  	1
Enter Date(YYYY-MM--DD): 2025-11-04
Enter Category Name(eg:Food,Travel,etc:food
Enter amount:4000
Enter Description:for pizza
Expense added successfully!
Enter Your Choice:(1-3)  	2

-----All Expenses-----
2025-11-04|food|4000.0|for pizza

Enter Your Choice:(1-3)  	



"""