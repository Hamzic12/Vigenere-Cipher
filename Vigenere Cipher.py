alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_index = dict(zip(alphabet, range(len(alphabet))))
index_letter = dict(zip(range(len(alphabet)), alphabet))

message = input("Enter your message: ")
key = input("Enter the key: ")

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
            i += 1
            encrypted_message += letter
    
    return encrypted_message

encrypt(message, key)