def displayMenu()-> int:
    print("Options: ")
    print("1 - Insert word: ")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    return int(input("Your choice:"))

def main() -> None:
    print("Program starting.")
    Word = ""
    choice = -1 
    while choice != 0:
        choice = displayMenu()
        if choice == 1:
            Word = input("Insert word: ")
        elif choice == 2:
            print(f"Current word - {Word}")
        elif choice == 3:
            print(f"Word reverse - {Word[::-1]}")
    print("")
    print("Program ending.")
    return None