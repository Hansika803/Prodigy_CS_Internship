def caesar_cipher(message, shift, mode='encrypt'):
    result = []
    
    # Ensure that the shift value is within the 0-25 range (valid Caesar Cipher shift)
    shift = shift % 26
    
    for char in message:
        # Handle spaces: No transformation needed for spaces
        if char == " ":
            result.append(char)
        elif char.isupper():  # Encrypt/Decrypt uppercase characters
            shifted_char = chr((ord(char) + (shift if mode == 'encrypt' else -shift) - 65) % 26 + 65)
            result.append(shifted_char)
        elif char.islower():  # Encrypt/Decrypt lowercase characters
            shifted_char = chr((ord(char) + (shift if mode == 'encrypt' else -shift) - 97) % 26 + 97)
            result.append(shifted_char)
        else:
            # Non-alphabetic characters are added without change
            result.append(char)
    
    # Convert the list of characters back into a string and return it
    return ''.join(result)


def main():
    # Get user input for the message and shift value
    message = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    # Perform encryption and decryption
    encrypted_message = caesar_cipher(message, shift, mode='encrypt')
    decrypted_message = caesar_cipher(encrypted_message, shift, mode='decrypt')
    
    # Display results
    print("\nEncrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)
    

if __name__ == "__main__":
    #Call the main function to execute the program
    main()