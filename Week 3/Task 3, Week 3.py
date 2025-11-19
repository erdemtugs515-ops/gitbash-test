name = input("Enter your name: ")

while True:
    
    print("\nMenu:")
    print("1. Print welcome message")
    print("2. Exit")
    choice = input("Your choice: ")
    if choice == "1":
        print(f"Welcome {name}!")
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Unknown option.")