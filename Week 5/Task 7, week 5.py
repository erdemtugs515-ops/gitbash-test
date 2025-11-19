def main():
    print("Program starting.")

    words = []

    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    if word_count > 0:
        avg_length = char_count / word_count
    else:
        avg_length = 0
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print(f"- {avg_length:.2f} Average word length")
    print("Program ending.")
    
main()