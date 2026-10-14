
total_bill = float(input("Enter total grocery bill: "))

if total_bill > 2000:
    discount = total_bill * 10 / 100
else:
    discount = 0

final_bill = total_bill - discount

print("Original Bill: ", total_bill)
print("Discount Amount: ", discount)
print("Final Bill: ", final_bill)
