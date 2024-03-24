alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_index = dict(zip(alphabet, range(len(alphabet))))
index_letter = dict(zip(range(len(alphabet)), alphabet))

choice = input("Encrypt or decrypt a message: ")


def encrypt(message, key):
    #split into length of key
    split_message = [message[i: i + len(key)] for i in range(0, len(message), len (key))]
    encrypted_message = ""

    #split list
    for split in split_message:
        i = 0
        #split words
        for letter in split:
            number = (letter_index[letter] + letter_index[key[i]]) % 26 #mod 26 = length of alphabet
            letter = index_letter[number]
            encrypted_message += letter
            i += 1
    
    return encrypted_message

def decrypt(encrypted, key):
    split_message = [encrypted[i: i + len(key)] for i in range(0, len(encrypted), len (key))]
    decrypted_message = ""
    
    for split in split_message:
        i = 0
        for letter in split:
            number = (letter_index[letter] - letter_index[key[i]]) % 26 
            letter = index_letter[number]
            decrypted_message += letter
            i += 1
    
    return decrypted_message


def choose(choice):
    #if choice is not either encrypt or decrypt it will ask again until the right choice is written
    try:
        choice = choice.lower()
        if choice not in ["encrypt", "decrypt"]:
            raise ValueError("Invalid choice.")
        
        key = input("Enter the key: ")

        match choice:
            case "encrypt":
                message = input("Enter your message: ")
                print(encrypt(message, key))
            case "decrypt":
                encrypted_message = input("Enter your encrypted message: ")
                print(decrypt(encrypted_message, key))

    except ValueError:
        print(ValueError)
        choose(input("Try again. Enter encrypt or decrypt: "))

choose(choice)