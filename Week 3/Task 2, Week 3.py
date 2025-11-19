word1 = input("Insert a word: ")
character = input("Insert a character: ")

if character in word1:
    print('Word "' + word1 + '" contains character "' + character + '"')
else:
    print('Word "' + word1 + '" doesn\'t contain character "' + character + '"')

word2 = input("Insert another word: ")

if word1 < word2:
    print('The first word "' + word1 + '" is before the second word "' + word2 + '" alphabetically.')
elif word2 < word1:
    print('The second word "' + word2 + '" is before the first word "' + word1 + '" alphabetically.')
else:
    print('Both inserted words are the same alphabetically, "' + word1 + '"')
