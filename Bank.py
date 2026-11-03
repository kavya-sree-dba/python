class Bank:

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    # PIN Verification
    def verify_pin(self):
        entered_pin = int(input("Enter your PIN: "))

        if entered_pin == self.pin:
            print("PIN Verified Successfully!")
            return True
        else:
            print("Invalid PIN!")
            return False

    # Deposit Money
    def deposit(self):
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
            print("Current Balance:", self.balance)
        else:
            print("Please enter a valid amount.")

    # Withdraw Money
    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Please enter a valid amount.")

        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", self.balance)

        else:
            print("Insufficient Balance!")

    # Check Balance
    def check_balance(self):
        print("Account Holder:", self.name)
        print("Available Balance:", self.balance)


# Creating Object
account = Bank("Kavya", 1234, 5000)

# PIN Verification
if account.verify_pin():

    while True:

        print("\n----- BANK MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            account.deposit()

        elif choice == 2:
            account.withdraw()

        elif choice == 3:
            account.check_balance()

        elif choice == 4:
            print("Thank you for using our bank!")
            break

        else:
            print("Invalid Choice!")