
stock = 50

required = int(input("Enter required quantity: "))

if required <= 0:
    print("Enter a valid quantity")
elif required <= stock:
    print("Stock available")
    stock = stock - required
    print("Remaining stock:", stock)
else:
    print("Insufficient stock")