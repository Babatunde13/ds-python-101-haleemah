
def greet(*names):
    for name in names:
        print(f'Hello {name}!')
    # return 'Hello ' + name + '!'

print("First call")
greet()
print("Second call")
greet('Mary', 'Jane')
print("Third call")
greet('Jack', 'Jill', 'Joe')
print("Fourth call")
greet('Jill', 'Joe', 'Jack', 'John')

def print_info(name, age = 18):
    print(f'{name} is {age} years old')

print_info('John', 30)

def print_info_1(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value}')

def print_info_2(kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value}')

print_info_1(name='John', age=30, address='123 Main St')
print_info_2({'name': 'John', 'age': 30, 'address': '123 Main St'})

print_info('John')

a  =[]
a.sort()

class User:
    ...

class Product:
    ...

class Cart:
    ...


def main():
    user = User()
    product = Product()
    cart = Cart()
    user.purchase(product, cart)
