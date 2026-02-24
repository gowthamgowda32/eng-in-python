#tuples
friends = ("gowtham", "darshan" , "yashas")
print(friends)


print(friends[0])

print(friends[1:3])

best_friend = ("sudeep")
print(f"{best_friend}   {friends[1]}")

best_friends = (friends + ("sudeep",))*2
print(best_friends)

#sets
my_set = {1, 2, 3, 4, 5,}
package = {"numpy", "pandas", "matplotlib"}
print(my_set)
print(package)
empty_set = type(set())
print(empty_set)
union_set = my_set | package
print(union_set)
package.add("seaborn")
print(package)
package.discard("gowtham")
print(package)

#dictionaries
my_dict = {
    "name": "gowtham",
    "age": 20,
    "city": "bangalore"
}
print(my_dict)
print(my_dict["age"])
print(my_dict["name"])

print(my_dict.get("darshan", "not found"))
print(my_dict.get("age", "not found"))
my_dict["my_friend_name"] ="darshan"
print(my_dict)
del my_dict["my_friend_name"]
print(my_dict)
#my_dict.clear()
#print(my_dict)

print(my_dict.keys())
print(my_dict.values())
my_new_friend = {"his_name":"darshan"}
my_dict.update(my_new_friend)
print(my_dict)
