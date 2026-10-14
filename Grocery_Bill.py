
total_bill = 0

for i in range(5):
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    amount = quantity * price
    total_bill += amount

    print(name, "Amount:", amount)

print("Total Bill Amount: ₹", total_bill)
