def main():
    word = ""
    print("Program starting.")
    
    while True:
        print("\nOptions:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")
        choice = input("Your choice: ")
        if choice == "1":
            word = input("Insert word: ")
        elif choice == "2":
            if word:
                print(f'Current word - "{word}"')
            else:
                print("No word stored yet.")
        elif choice == "3":
            if word:
                print(f'Word reversed - "{word[::-1]}"')
            else:
                print("No word stored yet.")
        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option")
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
