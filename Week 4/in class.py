num1 = int(input("Insert a number: "))

flag = False
if num1 == 0 or 1:
    print(f"{num1} is not a prime number")
elif num1 > 1:
    for i in range(2, num1):
        if (num1 % i) == 0:
            flag = True
            break
    if flag:
        print(f"{num1} Is not a prime number. ")
    else:
        print(f"{num1} is a prime number. ")