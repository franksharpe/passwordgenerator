import tkinter as tk
import os
import random
import string
from tkinter import messagebox
import customtkinter
import CTkMessagebox

def create_password_file():
    if not os.path.exists("password.txt"):
        with open("password.txt", "w"):
            pass

def generate_password():
    length = int(length_entry.get())
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    digits = digits_var.get()
    symbols = symbols_var.get()

    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not any((uppercase, lowercase, digits, symbols)):
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.configure(text=password)

def save_password():
    create_password_file()
    password = password_label.cget("text")
    if password:
        directory = os.getcwd()
        file_path = os.path.join(directory, "password.txt")
        with open(file_path, "a") as e:
            e.write(password + "\n")
        messagebox.showinfo("Success", f"Password saved to {file_path}")
    else:
        messagebox.showerror("Error", "No password generated yet.")

def display_saved(event=None):
    create_password_file()
    with open("password.txt", "r") as d:
        saved_passwords = d.readlines()
        saved_passwords = [password.strip() for password in saved_passwords]

    response = messagebox.askyesno("Password Match", f"Saved passwords:\n\n\n{saved_passwords}\n\n\nWould you like to clear saved passwords?")
    if response:
        print("Yes clicked")
        filename = "password.txt"
        clear_file(filename)
    else:
        exit()

def get_password():
    inputed = label.get()
    print("Entered:", inputed) 

root = customtkinter.CTk()
root.title("Password Generator")
root.geometry("430x932")
customtkinter.set_default_color_theme("blue")

length_label = customtkinter.CTkLabel(master=root, text="Enter the length of the password:")
length_label.grid(row=0, column=0,padx=10, pady=5)

length_entry = customtkinter.CTkEntry(master=root, placeholder_text="Password Length")
length_entry.grid(row=0, column=1, padx=10, pady=5)

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

uppercase_check = customtkinter.CTkCheckBox(master=root, text="Include uppercase letters?", variable=uppercase_var)
lowercase_check = customtkinter.CTkCheckBox(master=root, text="Include lowercase letters?", variable=lowercase_var)
digits_check = customtkinter.CTkCheckBox(master=root, text="Include digits?", variable=digits_var)
symbols_check = customtkinter.CTkCheckBox(master=root, text="Include symbols?", variable=symbols_var)

uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
lowercase_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
digits_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
symbols_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

generate_button = customtkinter.CTkButton(master=root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

password_label = customtkinter.CTkLabel(master=root, text="Your generated password will appear here")
password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

save_button = customtkinter.CTkButton(master=root, text="Save Password", command=save_password)
save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

def show_button():
    label.configure(placeholder_text="Enter Password to View")
    label.grid()
    labele.configure(text="Get Input")
    labele.grid()

display_button = customtkinter.CTkButton(master=root, text="Display Passwords", command=show_button)
display_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

label = customtkinter.CTkEntry(master=root, placeholder_text="")
label.grid(row=9 , column=0, columnspan=2, padx=10, pady=5)
label.grid_remove()

label.bind("<Return>", display_saved )

labele = customtkinter.CTkButton(master=root, text="", command=get_password)
labele.grid(row=10, column=1, padx=10, pady=5)
labele.grid_remove() 

root.mainloop()
