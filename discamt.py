
medicine = input("Enter medicine name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per strip: "))

total = quantity * price

if total > 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print("Original Amount: ₹", total)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_amount)