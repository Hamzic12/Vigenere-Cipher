from tkinter import *
from VigenereCipher import *

def user_input(operation):
    key_data = key_entry.get()
    message_data = message_entry.get()
    if operation == "encrypt":
        encrypted = encrypt(key_data, message_data)
        encrypted_label.config(text="Encrypted message: " + encrypted)
        decrypted_label.grid_remove()
        encrypted_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    elif operation == "decrypt":
        decrypted = decrypt(key_data, message_data)
        decrypted_label.config(text="Decrypted message: " + decrypted)
        encrypted_label.grid_remove()
        decrypted_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

window = Tk()
window.title("Vigenere Cipher")
window.geometry("400x300")
window.config(bg="light grey")


top_padding = Frame(window, bg="light grey", height=20)
top_padding.pack(fill=X)

top_frame = Frame(window, bg="light grey")
top_frame.pack(pady=10)

key_label = Label(top_frame, text="Key:", font=("Arial", 12), bg="light grey")
key_label.grid(row=0, column=0, padx=5, pady=5)

key_entry = Entry(top_frame, font=("Arial", 12))
key_entry.grid(row=0, column=1, padx=5, pady=5)

message_label = Label(top_frame, text="Message:", font=("Arial", 12), bg="light grey")
message_label.grid(row=1, column=0, padx=5, pady=5)

message_entry = Entry(top_frame, font=("Arial", 12))
message_entry.grid(row=1, column=1, padx=5, pady=5)


middle_frame = Frame(window, bg="light grey")
middle_frame.pack(pady=10)


encrypted_label = Label(middle_frame, text="", font=("Arial", 12), bg="light grey")
decrypted_label = Label(middle_frame, text="", font=("Arial", 12), bg="light grey")

bottom_frame = Frame(window, bg="light grey")
bottom_frame.pack(pady=30)

encrypt_button = Button(bottom_frame, command=lambda: user_input("encrypt"), text="Encrypt", font=("Arial", 12)) 
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = Button(bottom_frame, command=lambda: user_input("decrypt"), text="Decrypt", font=("Arial", 12))
decrypt_button.grid(row=0, column=1, padx=10)

window.mainloop()
