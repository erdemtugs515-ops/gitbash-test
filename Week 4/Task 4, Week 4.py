print("Program starting. ")
print("")
wordcount= 0 
characount= 0
word = input("Insert word (Empty stops): ")
while word != "":
    wordcount+= 1
    characount+=len(word)
    word = str(input("Insert word (Empty stops): "))
print("")
print("You inserted: ")
print(f" {wordcount} words. ")
print(f" {characount} characters. ")

print("\nProgram Ending. ")