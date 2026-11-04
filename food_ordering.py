# Parent Class
class FoodItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "-", self.price)


# Child Class 1
class VegItem(FoodItem):

    def display(self):
        print(self.name, "- Rs.", self.price, "(Vegetarian)")


# Child Class 2
class NonVegItem(FoodItem):

    def display(self):
        print(self.name, "- Rs.", self.price, "(Non-Vegetarian)")


# Customer Class
class Customer:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.cart = []

    def add_to_cart(self, food, quantity):
        self.cart.append((food, quantity))
        print(food.name, "added to cart successfully!")


# Restaurant Class
class Restaurant:

    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def display_menu(self):
        print("\n-----", self.name, "MENU -----")

        for i, food in enumerate(self.menu, start=1):
            print(i, end=". ")
            food.display()


# Order Class
class Order:

    def __init__(self, customer):
        self.customer = customer
        self.__total = 0

    def calculate_total(self):

        self.__total = 0

        for food, quantity in self.customer.cart:
            self.__total += food.price * quantity

        return self.__total

    def apply_discount(self):

        total = self.calculate_total()

        if total >= 500:
            discount = total * 0.10
        elif total >= 300:
            discount = total * 0.05
        else:
            discount = 0

        return discount

    def generate_bill(self):

        print("\n========== ORDER SUMMARY ==========")
        print("Customer Name:", self.customer.name)
        print("Phone Number:", self.customer.phone)

        print("\nOrdered Items:")

        for food, quantity in self.customer.cart:
            print(food.name, "x", quantity,
                  "=", food.price * quantity)

        total = self.calculate_total()
        discount = self.apply_discount()
        final_amount = total - discount

        print("\nTotal Amount: Rs.", total)
        print("Discount: Rs.", discount)
        print("Final Bill: Rs.", final_amount)

        print("\nThank you for ordering!")


# Creating Restaurant Object
restaurant = Restaurant("Food Paradise")

# Adding Food Items
food1 = VegItem("Paneer Biryani", 200)
food2 = VegItem("Veg Fried Rice", 150)
food3 = NonVegItem("Chicken Biryani", 250)
food4 = NonVegItem("Chicken Fried Rice", 180)

restaurant.add_food(food1)
restaurant.add_food(food2)
restaurant.add_food(food3)
restaurant.add_food(food4)

# Display Menu
restaurant.display_menu()

# Creating Customer
customer = Customer("Kavya", "9876543210")

# Adding Items to Cart
customer.add_to_cart(food1, 2)
customer.add_to_cart(food3, 1)

# Creating Order
order = Order(customer)

# Generating Final Bill
order.generate_bill()