class ATM:
    def _init_(self, name, pin):
        self.name = name
        self.pinNo = pin
        self.balance = 0.0

    def deposit(self):
        pin = int(input("Please Enter pin number: \n"))
        if self.pinNo == pin:
            print("-------Deposit---------")
            amount = float(input("Please Enter Money for deposit: "))
            if amount > 0:  # Check for positive amount
                self.balance += amount
                print(f"Deposited in your account: ₹{amount}")
            else:
                print("Invalid amount! Please enter a positive value.")
        else:
            print("Invalid Pin Number!")

    def withdrawal(self):
        pin = int(input("Please Enter pin number: \n"))
        if self.pinNo == pin:
            print("--------Withdrawal--------")
            amount = float(input("Enter Amount: "))
            if amount > 0 and amount <= self.balance:  # Check for positive amount and sufficient balance
                self.balance -= amount
                print(f"Withdrew: ₹{amount}")
            else:
                if amount <= 0:
                    print("Invalid amount! Please enter a positive value.")
                else:
                    print("Insufficient balance!")
        else:
            print("Invalid Pin Number!")

    def show_balance(self):
        pin = int(input("Please Enter pin number: \n"))
        if self.pinNo == pin:
            print("--------Balance----------")
            print(f"In your account, the balance is: ₹{self.balance}")
        else:
            print("Invalid Pin Number!")

    def menu(self):
        while True:
            print("\nChoose an option:")
            print("1. Deposit")
            print("2. Withdrawal")
            print("3. Balance")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdrawal()
            elif choice == 3:
                self.show_balance()
            elif choice == 4:
                print("Exiting the menu. Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option.")

# Create an instance of the ATM class
a1 = ATM('Selvan', 1453)
a1.menu()