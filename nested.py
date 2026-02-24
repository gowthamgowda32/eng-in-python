day = input("enter the day: ")
is_working_day = input("is it a working day? (yes/no): ")
is_it_raining = input("is it raining? (yes/no): ")
if is_working_day == "yes":
    if day in ["monday", "tuesday", "wenesday", "thursday", "friday"]:
        print(" im sorry i have to work")
elif is_working_day == "no":
       if is_it_raining == "yes":
           print("im sorry")
if is_it_raining == "no":
                         print("lets go out")
else:
    print("lets enjoy the day")


