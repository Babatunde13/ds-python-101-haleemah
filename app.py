PI = 3.142

PI = 3.14 # This should not be allowed
print(PI)

name = "John" + ' Doe'
age = 23
height = 6.1
isMarried = False

with open("app.py") as f:
    print(f.read())

# Strings
name = "John Doe"
char = 'a'
numeric = "123"
print(type(name))
print(type(char))
print(type(numeric))
print(type(isMarried))
print(type(height))
print(type(age))
my = 1

with open("app.py") as f:
    print(f)

y = memoryview(b"Hello")
print(y)
print(y[1])

user1 = {
    "name": "John Doe",
    "age": 23,
    "height": 6.1,
    "isMarried": False
}

user2 = {
    "name": "John Doe",
    "age": 23,
    "height": 6.1,
    "isMarried": False
}

user_set = {
    "John Doe",
    23,
    6.1,
    False
}


print(user1)
print(user_set)

user_set.add(1)
user_set.add(1)
user_set.add(1)
print(user_set)

products = ["Laptop", "Desktop", "Mobile"]
users = set()
def sale(user, product, price):
    print("User: ", user + "is buying a " + product + " for " + str(price))
    if product not in products:
        print("Product not found")
        return

    print("Product found")
    users.add(user)
    print("User added to the list")
    products.remove(product)
    print("Product removed from the list")
    return


sale("John Doe", "Laptop", 1000)
sale("Jane Doe", "Laptop", 1000)
sale("John Doe", "Laptop", 1000)
sale("Janet Doe", "Desktop", 1000)
sale("John Doe", "Mobile", 1000)

print(products)
print(users)

# unique_users = set(users)
# print(unique_users)


print(user1 == user2)