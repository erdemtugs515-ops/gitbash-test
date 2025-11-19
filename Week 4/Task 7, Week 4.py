print("Program starting.\n")
print("Check multiplicative persistence.")

num = input("Insert an integer: ")
steps = 0
while len(num) > 1:
    digits = [int(d) for d in num]
    print(" * ".join(num), end=" = ")
    product = 1
    for d in digits:
        product *= d
    print(product)
    num = str(product)
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")
