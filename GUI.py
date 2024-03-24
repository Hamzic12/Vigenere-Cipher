from tkinter import *
from VigenereCipher import *

window = Tk()
logo = PhotoImage(file='Logo/vigenere.png')
window.iconphoto(True, logo)
window.title("Vigenere Cipher")
window.geometry("500x450")
window.config(background="grey")

key_entry = Entry(window, font=(24))
key_entry.pack(side = TOP)
message_entry = Entry(window, font=(24))
message_entry.pack(side = TOP)

def user_input(operation):
   key_data = key_entry.get()
   message_data = message_entry.get()
   match operation:
        case "encrypt":
            encrypted = encrypt(key_data, message_data)
            print(encrypted)
        case "decrypt":
           decrypted = decrypt(key_data, message_data)
           print(decrypted)

encrypt_button = Button(window, command=lambda: user_input("encrypt"), text="Encrypt") 
decrypt_button = Button(window, command=lambda: user_input("decrypt"), text="Decrypt")

decrypt_button.pack(side = BOTTOM)
encrypt_button.pack(side = BOTTOM)


window.mainloop()
