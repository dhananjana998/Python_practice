def calculator():
    print("-" * 50)
    print("\t SIMPLE CALCULATOR")
    print("-" * 50)

    while True:
        try:
            num_one = float(input("\nEnter the first number: "))
            num_two = float(input("Enter the second number: "))
        except ValueError:
            print("❌ Please enter valid numbers!")
            continue

        print("\nSelect operator:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("❌ Please enter a valid choice number!")
            continue

        if choice == 1:
            answer = num_one + num_two
            print(f"Result: {num_one} + {num_two} = {answer}")

        elif choice == 2:
            answer = num_one - num_two
            print(f"Result: {num_one} - {num_two} = {answer}")

        elif choice == 3:
            answer = num_one * num_two
            print(f" Result: {num_one} × {num_two} = {answer}")

        elif choice == 4:
            try:
                answer = num_one / num_two
                print(f" Result: {num_one} ÷ {num_two} = {answer}")
            except ZeroDivisionError:
                print(" You can’t divide by zero!")

        elif choice == 5:
            print(" Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    calculator()
