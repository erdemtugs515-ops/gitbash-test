def askname():
    name = input("Please enter your name: ")
    return name 

def greetUser(Pname):
    print(f"Hello {Pname}")
    return None

def main():
    print("Program starting")
    name = askname()
    greetUser(name)
    print("Program ending. ")
    return None
main()
