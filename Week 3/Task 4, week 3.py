name = input("Enter your name: ")

while True:
    print("\nMenu:")
    print("1. Print welcome message")
    print("2. Print the name backwards")
    print("3. Print the first character")
    print("4. Show the amount of characters in the name")
    print("5. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        print("Welcome " + name + "!")

    elif choice == "2":
        backwards = ""
        for letter in name:
            backwards = letter + backwards
        print('Your name backwards is "' + backwards + '"')

    elif choice == "3":
        first_char = name[0]
        print('The first character in name "' + name + '" is "' + first_char + '"')

    elif choice == "4":
        length = len(name)
        print('There are ' + str(length) + ' characters in the name "' + name + '"')

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Unknown option.")
