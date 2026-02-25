
#snacks available
snacks_available = 10
money = 5

while snacks_available>0 :
    print(f"snack available: {snacks_available} and money: {money}")
    buy = input("do u want to purchase snacks (yes/no): ")
    if buy == "yes":
        snacks_available -= 1
        
        print("snacks purchased")
    else:
        print("visit again soon")

#bus ticket booking
print("welcome to ksrtc bus ticket booking")
seats_available = 5
print(f"seats available: {seats_available}")
while seats_available > 0:
    name = input("enter ur name: ")
    seats_available -= 1
    place = input("enter your destination: ")
    print(f"congratulations {name} your ticket to {place} is booked")
    print(f"seats available: {seats_available}")
    if seats_available == 0:
        print("sorry, all seats are booked")

#chips
chips_count = int(input("enter the number of chips you want to buy: "))
rupees = chips_count * 5
while chips_count >= 1:
    print(f"the amount u have to pay is:{rupees} rupees")
    break
if rupees > 100:
    print("you are eligible for a discount of 10%")
    discount = rupees * 0.1
    final_amount = rupees - discount
    print(f"the final amount to be paid is: {final_amount} rupees")
else:
    print("you are not eligible for a discount")


     
  



