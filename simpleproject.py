password = "1234"
balance = 5000

print("===== WELCOME TO SMART SYSTEM =====")

# LOGIN SYSTEM
while True:
    user_pass = input("Enter Password: ")

    if user_pass == password:
        print("Login Successful!")
        break
    else:
        print("Wrong Password! Try Again")

# MAIN MENU
while True:
    print("\n====== MAIN MENU ======")
    print("1. ATM System")
    print("2. Calculator")
    print("3. Multiplication Table")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # ATM SYSTEM
    if choice == 1:
        while True:
            print("\n--- ATM MENU ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Back to Main Menu")

            atm_choice = int(input("Enter your choice: "))

            if atm_choice == 1:
                print("Your Balance is:", balance)

            elif atm_choice == 2:
                amount = int(input("Enter deposit amount: "))
                balance = balance + amount
                print("Money Deposited Successfully")

            elif atm_choice == 3:
                amount = int(input("Enter withdrawal amount: "))

                if amount <= balance:
                    balance = balance - amount
                    print("Please collect your cash")
                else:
                    print("Insufficient Balance")

            elif atm_choice == 4:
                break

            else:
                print("Invalid Choice")

    # CALCULATOR
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        op = int(input("Choose operation: "))

        if op == 1:
            print("Result:", num1 + num2)

        elif op == 2:
            print("Result:", num1 - num2)

        elif op == 3:
            print("Result:", num1 * num2)

        elif op == 4:
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero")

        else:
            print("Invalid Operation")

    # MULTIPLICATION TABLE
    elif choice == 3:
        num = int(input("Enter number: "))

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    # EXIT
    elif choice == 4:
        print("Thank you for using the system 🙏")
        break

    else:
        print("Invalid Choice! Try again.")