def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old !")
    print()

happy_birthday("bro", 25)
happy_birthday("him", 30)
happy_birthday("her", 28)

def display_invoice(customer, amount):
    print(f"Customer: {customer}")
    print(f"Amount: ${amount:.2f}")
    print()

display_invoice("John Doe", 100.50)
display_invoice("Jane Smith", 75.25)

def add(x,y):
    z = x + y
    return z
def subtract(x,y):
    z = x - y
    return z
def multiply(x,y):
    z = x * y
    return z
def divide(x,y):
    if y != 0:
        z = x / y
        return z
    else:
        return "Error: Division by zero is not allowed."  

print (add(5, 3))
print (subtract(10, 4))
print (multiply(6, 7))
print (divide(12, 3))
print (divide(10, 0))

def create_name(first_name, last_name):
    first_name = first_name.strip().capitalize()
    last_name = last_name.strip().capitalize()
    full_name = first_name + " " + last_name
    return full_name
    

print (create_name("  john", "doe  "))