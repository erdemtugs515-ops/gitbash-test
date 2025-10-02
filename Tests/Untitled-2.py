print("starting program.")
print("Testing decision structures.")
Feed = input("insert an integer")
Value = int(Feed)

print("Options:")
print("1 - In one multi-branced decision")
print("2 - In multiple independent if statements")
print("0 - Exit")

Feed = input("Your choice: ")
Choice = int(Feed) 

if (Choice == 1):
    if (Value >= 400):
        print("Larger than 400")
    elif(Value >= 200):
        print("Larger than 200")
    elif(Value >= 100):
        print("Larger than 100")
elif (Choice == 2):
    print("Choice Two")
elif (Choice == 0):
    print("Ending program")
else:
    print("Unknown option")