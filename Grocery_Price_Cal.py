
def calculate_cost(price, quantity):
    total = price * quantity

    if quantity > 10:
        discount = total * 5 / 100
        total = total - discount

    return total


price = float(input("Enter item price: ₹"))
quantity = int(input("Enter quantity: "))

final_amount = calculate_cost(price, quantity)

print("Final Amount Payable: ₹", final_amount)
