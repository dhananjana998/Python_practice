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
        print("Preparing pizza dough, adding sauce and cheese.")

    def serve(self):
        print("Serving the pizza in a box.")


class Burger(FoodItem):
    def prepare(self):
        print("Grilling burger patty and adding toppings.")

    def serve(self):
        print("Serving the burger in a wrapper.")


class Pasta(FoodItem):
    def prepare(self):
        print("Boiling pasta and adding sauce.")

    def serve(self):
        print("Serving the pasta on a plate.")


# Abstract class for Payment
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# Subclasses for Payment Methods
class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing card payment of Rs{amount}.")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Accepting cash payment of Rs{amount}.")


# Main Program
def Practice_AbstractionMethod():
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
if __name__ == "__Practice_AbstractionMethod__":
    Practice_AbstractionMethod()
