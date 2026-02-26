no_of_cars_brands = 5
car_owners = ["gowtham", "mariswamy", "madeshwara", "shiva", "ganesha"]
brands = ["audi", "mercedez", "bmw", "volvo", "honda"]

for car_owner, brand in zip(car_owners, brands):
    hi = input(f" which branded {brands} do u want to know: ")
    if hi in brands :
        if car_owner == "gowtham":
            print(f"{car_owner} is the owner of a car but we will not disclose it")
            continue
        else:
            print(f"{car_owner} owns a {brand} branded car")
    if car_owner == "shiva":
        print(f"{car_owner} is the final boss , he has a {brand} branded car")
    else:
        print(f"{car_owner} owns a {brand} branded car")
if no_of_cars_brands > 0:
    print(f"we have {no_of_cars_brands} cars and brands in our list")
    a = input("enter the car brand you want to know the owner of: ")
    if a in brands:
        index = brands.index(a)
        if car_owners[index[0]] == "gowtham":
            print(f"{car_owners[index]} is the owner of but we can not disclose it")
        else:
             print(f"{car_owners[index]} is the owner of {a} branded car")
    else:
        print(f"sorry we dont have {a} in our list")
no_of_cars_brands -= 1
print(f"we have {no_of_cars_brands} cars and brands left in our list and they are {brands}")


    



    