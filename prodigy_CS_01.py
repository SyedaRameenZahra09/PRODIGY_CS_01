def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ('e', 'd'):
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue

        text = input("Enter the message: ")
        shift = int(input("Enter the shift value (a positive integer): "))

        if choice == 'e':
            encrypted_text = caesar_encrypt(text, shift)
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = caesar_decrypt(text, shift)
            print("Decrypted text:", decrypted_text)

        another = input("Do you want to perform another operation? (Y/N): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()

