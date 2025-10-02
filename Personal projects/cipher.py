def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char  
    return result

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

message = input("Enter text: ")
shift = int(input("Enter shift number: "))

encrypted = encrypt_caesar(message, shift)
decrypted = decrypt_caesar(encrypted, shift)

print("Original:", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

