variety = 5
dishes = ["biryani", "chicken curry", "upsaru", "milk", "laadu"]
friends = ["gowtham", "mariswamy", "madeshwara", "shiva", "ganesha"]

for dish, friend in zip(dishes, friends):
    if dish == "milk":
        print(f"{friend} is drinking {dish}")
    else:
        print(f"{friend} is eating {dish}")
if variety > 0:
    print(f"we still contain other varieties of dishes")
    a = input("enter the dish you want to eat: ")
    if a in dishes:
        print(f"enjoy your {a}")
        variety -= 1
        print(f"variety left: {variety}")
    else:
        print(f"sorry we dont have {a} in our menu")







   
  
