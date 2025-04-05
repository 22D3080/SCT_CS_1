def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using Caesar cipher.
    
    :param text: The input string to encrypt or decrypt.
    :param shift: The number of positions to shift.
    :param mode: 'encrypt' to shift forward, 'decrypt' to shift backward.
    :return: Transformed text after applying the shift.
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char  # Preserve non-alphabet characters
    
    return result

def main():
    """Handles user input and calls the Caesar cipher function."""
    while True:
        mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
        if mode in ['encrypt', 'decrypt']:
            break
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")

    text = input("Enter the message: ")
    
    while True:
        try:
            shift = int(input("Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                break
            print("Shift value must be between 0 and 25.")
        except ValueError:
            print("Invalid shift value! Please enter an integer.")

    output = caesar_cipher(text, shift, mode)
    print(f"Result: {output}")

if __name__ == "__main__":
    main()