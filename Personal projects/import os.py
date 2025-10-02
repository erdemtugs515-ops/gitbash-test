
while True:
    answer = input("Did you drink beer? = ").strip().lower()  
    if answer == "yes":
        print("You can start coding now")
        break  
    elif answer == "no":
        print("Drink a beer and come back")
    elif:
        print("Please answer with 'yes' or 'no'")
break 
# Task 3
user = input("What is your name? ").strip()
print(f"Welcome {user}")

# Task 1
print("Hello Python")

# Task 2
name1 = "John"
name2 = "Dave"
print(f"{name1} is eating ice cream with {name2}")

# Task 2: 
num1 = input("Give me a number = ").strip()
num2 = input("Give me a second number = ").strip()
add = int(num1) + int(num2)
print(add)

# Task 4: 
num4 = 47
num5 = 102
_sum = num4 + num5                 
_diff = num4 - num5              
_product = _sum * _diff          

print(f"{num4} + {num5} = {_sum}")
print(f"{num4} - {num5} = {_diff}")
print(f"{_sum} * {_diff} = {_product}")
