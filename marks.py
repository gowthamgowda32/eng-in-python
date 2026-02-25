choice = "yes"

while choice == "yes":
    marks = int(input("Enter your marks: "))

    if marks >= 90:
        print("Grade: A+")
    elif marks >= 75:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 40:
        print("Grade: C")
    else:
        print("Grade: Fail")

    choice = input("Do you want to continue? (yes/no): ")