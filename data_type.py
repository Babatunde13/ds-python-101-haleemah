name, age, height, isMarried = "Janet Doe", 24, 5.6, False

name == "John Doe"
name != "John Doe"
1 == 1
if (name == "John Doe" or age == 23 or height == 6.1):
    print("Hello John Doe")

not isMarried

user1 = {
    "name": "John Doe",
    "age": 23,
    "height": 6.1,
    "isMarried": False,
}

user2 = {
    "name": "John Doe",
    "age": 23,
    "height": 6.1,
    "isMarried": False
}

# create a deep copy of user1
user3 = user1.copy()
user3["name"] = "Jane Doe"

print(user1 == user2)
print(user1 is user2)
print(user1 is user3)
print(user1 == user3)

user3["name"] = "Jane Doe"
print(user1)
print(user2)
print(user3)
