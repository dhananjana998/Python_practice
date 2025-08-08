from abc import ABC, abstractmethod

# Abstract class for Food Item
class FoodItem(ABC):
    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass


# Subclasses for Food Items
class Pizza(FoodItem):
    def prepare(self):
        print("Prepared pizza")

    def serve(self):
        print("Serving the pizza")


class Burger(FoodItem):
    def prepare(self):
        print("Prepared burger")

    def serve(self):
        print("Serving the burger")


class Pasta(FoodItem):
    def prepare(self):
        print("Prepared pasta")

    def serve(self):
        print("Serving the pasta")


# Abstract class for Payment
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Subclasses for Payment Methods
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing card payment of Rs {amount}.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Accepting cash payment of Rs {amount}.")


# Main Program
def main():
    print("Select a food item:")
    print("1. Pizza")
    print("2. Burger")
    print("3. Pasta")

    food_choice = input("Enter choice (1-3): ")

    # Dictionary for food items and prices
    food_map = {
        "1": (Pizza(), 1200),
        "2": (Burger(), 800),
        "3": (Pasta(), 1000)
    }

    if food_choice in food_map:
        food, price = food_map[food_choice]
    else:
        print("Invalid choice!")
        return

    food.prepare()
    food.serve()

    print("\nSelect payment method:")
    print("1. Card")
    print("2. Cash")

    payment_choice = input("Enter choice (1-2): ")

    # Dictionary for payment methods
    payment_map = {
        "1": CardPayment(),
        "2": CashPayment()
    }

    if payment_choice in payment_map:
        payment = payment_map[payment_choice]
    else:
        print("Invalid payment method!")
        return

    payment.pay(price)


# Run the program
if __name__ == "__main__":
    main()
"""
Output:

Select a food item:
1. Pizza
2. Burger
3. Pasta
Enter choice (1-3): 1
Prepared pizza
Serving the pizza

Select payment method:
1. Card
2. Cash
Enter choice (1-2): 2
Accepting cash payment of Rs 1200.

Process finished with exit code 0
"""
