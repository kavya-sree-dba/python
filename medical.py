
medicine = input("Enter medicine name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per strip: "))

total = quantity * price

print("Medicine Name:", medicine)
print("Quantity:", quantity)
print("Total Bill: ₹", total)