balance = 5000
choice = 0

while choice != 3:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 3:
        print("Thank you for using ATM")

    else:
        print("Invalid choice!")