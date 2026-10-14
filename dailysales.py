
total = 0

for i in range(1, 3):
    bill = float(input("Enter customer bill: "))
    total = total + bill

average = total / 5

print("Total Sales: ₹", total)
print("Average Bill: ₹", average)