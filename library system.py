#store the library book's data in this list
# Store all books
library = [
    {"title": "Harry Potter", "author": "J.K. Rowling", "isbn": "9780439708180",
     "category": "Fiction", "copies": 10, "borrowed": 3, "location": "Shelf A1",
     "borrowed_by": ["Ram", "Sita", "Gita"], "borrow_dates": ["2025-11-05", "2025-11-08", "2025-11-10"]}
]

# add the new book to  the System
def add_book():
    print("\n" + "-" * 50 + "ADD NEW BOOK"  + "-" * 50)

    title = input("Enter Book Title    : ").strip()
    if not title :
        print(" Title cannot be empty")
        return

    author = input("Enter Book Author   : ").strip()
    if not author:
        print(" Author cannot be empty")
        return

    isbn = input("Enter Book ISBN     : ").strip()

    #check the ISBN already add or not
    for book in library:
        if book["isbn"] == isbn:
            print(" This ISBN already exists!")
            return

    if not isbn:
        print("ISBN cannot be empty!")
        return

    category = input("Enter Book Category : ").strip()
    location = input("Enter Book Location : ").strip()

    #   copies must be more than 1
    while True:
            copies = int(input("Copies   : ").strip())
            if copies < 1:
                print("Copies must be at least 1!")
                continue

            break

    # Add the book to library
    library.append({
        "title": title,
        "author": author,
        "isbn": isbn,
        "category": category if category else "Uncategorized",
        "copies": copies,
        "borrowed": 0,
        "location": location if location else "General Shelf"
    })

    print(f"\n Book '{title}' added successfully! ({copies} copies)")

# SEARCH BOOK

def search_book():
    if not library:
        print("\n This book not in RNCOE Library")
        return

    print("\n" + "-" * 50 + "SEARCH BOOK "+ "-" * 50  )
    criteria = input("Enter to search the book ( title/author/ISBN ): ").strip().lower()

    if not  criteria:
        print(" Search cannot be empty!")
        return


    print("\n" + "-" * 50+" SEARCH RESULTS:" + "-" * 50)


    for book in library:
        if ( criteria in book["title"].lower() or  criteria in book["author"].lower() or criteria == book["isbn"]):
            available = book["copies"] - book["borrowed"]
            print(f"Title    : {book['title']}")
            print(f"Author   : {book['author']}")
            print(f"ISBN     : {book['isbn']}")
            print(f"Category : {book['category']}")
            print(f"Location : {book['location']}")
            print(f"Available: {available}/{book['copies']}")


    else:
        print(" No matching book found.")



 # BORROW BOOK (USER TYPES DATE)
def borrow_book():
    print("\n" + "-" * 50 + " BORROW BOOK " + "-" * 50)
    isbn = input("Enter ISBN to borrow: ").strip()
    name = input("Enter your name     : ").strip()

    # USER TYPES DATE MANUALLY
    while True:
        date = input("Enter issue date (YYYY-MM-DD): ").strip()
        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            if date[0:4].isdigit() and date[5:7].isdigit() and date[8:10].isdigit():
                break
            else:
                print("Date must have numbers only!")
        else:
            print("Use format: YYYY-MM-DD (example: 2025-11-12)")

    for book in library:
        if book["isbn"] == isbn:
            if book["borrowed"] < book["copies"]:
                book["borrowed"] += 1
                book["borrowed_by"].append(name)
                book["borrow_dates"].append(date)
                print(f"\nSUCCESS! '{book['title']}' borrowed by {name}")
                print(f"Issue Date : {date}")
                print(f"Return by  : (14 days after {date})")
                print(f"Available now: {book['copies'] - book['borrowed']}/{book['copies']}\n")
            else:
                print("\nSORRY! All copies are borrowed.\n")
            return
    print("\nBook not found!\n")


# ---------------- RETURN BOOK ----------------
def return_book():
    print("\n" + "-" * 50 + " RETURN BOOK " + "-" * 50)
    isbn = input("Enter ISBN to return: ").strip()

    for book in library:
        if book["isbn"] == isbn and book["borrowed"] > 0:
            book["borrowed"] -= 1
            returned_by = book["borrowed_by"].pop()
            returned_on = book["borrow_dates"].pop()
            print(f"\nThank you {returned_by}! '{book['title']}' returned.")
            print(f"Borrowed on: {returned_on}")
            print(f"Available now: {book['copies'] - book['borrowed']}/{book['copies']}\n")
            return
    print("\nNo record found or book not borrowed!\n")

#summary report
report_month = ""
report_printed_month = None


def monthly_report():
    global report_month

    while True:
        month = input("\nEnter month for report (YYYY-MM): ").strip()
        if len(month) == 7 and month[4] == "-" and month[0:4].isdigit() and month[5:7].isdigit():
            break
        else:
            print("Enter correct format: YYYY-MM (example: 2025-11)")

    # SEARCH USER INPUT DATE TO MOUNTH NUMBER
    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    month_num = int(month[5:7])
    month_name = month_names[month_num]

    print("\n" + "-" * 180)
    print("   RUWANPURA NATIONAL COLLEGE OF EDUCATION - MONTHLY LIBRARY REPORT".center(100))
    print(f"   {month_name} {month[0:4]} - DATABASE SUMMARY".center(100))
    print("=" * 100)

    print(f"{'No':<4} {'TITLE':<35} {'AUTHOR':<18} {'TOTAL':<6} {'BORROWED':<8} {'AVAILABLE':<10} {'STATUS'}")
    print("-" * 100)

    total_copies = 0
    total_borrowed = 0

    for i in range(len(library)):
        book = library[i]
        avail = book["copies"] - book["borrowed"]
        status = "AVAILABLE" if avail > 0 else "ALL BORROWED"
        total_copies += book["copies"]
        total_borrowed += book["borrowed"]

        print(f"{i + 1:<4} {book['title'][:34]:<35} {book['author'][:17]:<18} "
              f"{book['copies']:<6} {book['borrowed']:<8} {avail:<10} {status}")

    report_month = month  # Save this month


#main user interface
while True:
    # name of system
    print("\n"+"-"*180)
    print("RUWANPURA NATIONAl COLLADGE OF EDUCATION".center(100))
    print("\n" + "-" * 180)

    # main menu
    #print("\t1.Add new book\n"+"\t2.Search Book\n"+"+"\t3. Borrow Book (Enter Date)"+)

    print("\t1. Add New Book")
    print("\t2. Search Book")
    print("\t3. Borrow Book (Enter Date)")
    print("\t4. Return Book")
    print("\t5. Monthly Report (Enter Month)")
    print("\t6. Exit")
    print("=" * 100)

    #get the  user needs in this system
    choice=int(input("Enter your choice(As 1 to 6 number):"))
   # check the user choice and call the function to user need
    if choice ==1:
        add_book()
    elif choice ==2:
        search_book()
    elif choice == 3:
        borrow_book()
    elif choice == 4:
        return_book()
    elif choice == 5:
        monthly_report()
    elif choice == 6:
        print("\n" + "=" * 100)
        print(" THANK YOU FOR USING RUWANPURA NATIONAL COLLEGE LIBRARY SYSTEM ".center(100))

        print("-" * 100)
        break
    else:
        print("Invalid choice! Enter 1–6 only.")



