import tkinter as tk
from tkinter import messagebox, simpledialog , ttk 
import os
import random
import string
from tkinter import *
import CTkMessagebox
import customtkinter

# Function to create the password file if it doesn't exist
def create_password_file():
    if not os.path.exists("password.txt"):
        # Create the file if it doesn't exist
        with open("password.txt", "w"):
            pass  # Do nothing, file is created

# Function to generate a password based on user input
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
        CTkMessagebox("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.configure(text=password)

# Function to save the generated password to a file
def save_password():
    create_password_file()
    password = password_label.cget("text")
    
    if password:
        with open("password.txt", "a") as f:
            f.write(password)
        CTkMessagebox.CTkMessagebox(title="Success", message="Password saved")
    else:
        CTkMessagebox(title="Error", message="No password generated yet.", icon="cancel")
'''
# Function to display saved passwords
def display_saved():
    create_password_file()
    inputed = CTkMessagebox("Input", "What is the saved password?")
    with open("password.txt", "r") as f:
        saved_passwords = f.readlines()
        saved_passwords = [password.strip() for password in saved_passwords]
        if inputed in saved_passwords:
            CTkMessagebox(title="Password Match", message="Password matched with saved passwords." + save_password)
        else:
            CTkMessagebox(title="Password Mismatch", message="Password does not match any saved passwords.", icon="cancel")
'''
# Main function to create and configure the GUI
def main():
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, password_label

    root = customtkinter.CTk()
    root.title("Password Generator")
    root.geometry("370x550")
    customtkinter.set_default_color_theme("dark-blue")
    
    app = customtkinter.CTk()
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)   
    
    # create CTk scrollbar
    ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app)
    ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

    # Entry for password length
    length_label = customtkinter.CTkLabel(master=root, text="Enter the length of the password:")
    length_label.grid(row=0, column=0,padx=10, pady=5)
    
    length_entry = customtkinter.CTkEntry(master=root, placeholder_text="Password Length")
    length_entry.grid(row=0, column=1, padx=10, pady=5)
    
    # password types
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

    # Button to generate password
    generate_button = customtkinter.CTkButton(master=root, text="Generate Password", command=generate_password)
    generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Label to display generated password
    password_label = customtkinter.CTkLabel(master=root, text="Your generated password will appear here")
    password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    
    # Button to save password
    save_button = customtkinter.CTkButton(master=root, text="Save Password", command=save_password)
    save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    
    # Button to display saved passwords
    #display_button = customtkinter.CTkButton(master=root, text="Display Passwords", command=display_saved)
    #display_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()

# Check if the script is being run directly
if __name__ == "__main__":
    main()
