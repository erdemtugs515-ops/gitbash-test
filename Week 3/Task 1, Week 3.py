print("Program starting.")
print("Please input 2 integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

if int1 > int2:
    print("Integer 1 is greater.")
elif int1 == int2:
    print("Both integers are equal.")
else:
    print("Integer 2 is greater.")

print("Adding integers together")
sum_val = int1 + int2
print(f"{int1} + {int2} = {sum_val}")

print("Checking the parity of the sum...")
if sum_val % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")
