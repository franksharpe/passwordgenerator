# password generator

#gui 
import tkinter as tk

#import os 
import os

#random strings and int
import random

#get strings
import string

#message boxes
from tkinter import messagebox

#theme
import customtkinter

#error msg
import CTkMessagebox

#copy to clipboard

import pyperclip


#creates file if its not there already
def create_password_file():
    if not os.path.exists("password.txt"):
        # (w) means write and can overide files
        with open("password.txt", "w"):
            pass

#generates the password based on parameters

def generate_password():
    
    #length in interger
    length = int(length_entry.get())
    
    #uppercase
    uppercase = uppercase_var.get()
    
    #lowercase
    lowercase = lowercase_var.get()
    
    #digits
    digits = digits_var.get()
    
    #symbols
    symbols = symbols_var.get()
    
    #get characters

    characters = ''
    if uppercase:
        
        #if uppercase does all A-Z
        characters += string.ascii_uppercase
    if lowercase:
        
        #if lowercase does all a-z
        characters += string.ascii_lowercase
    if digits:
        
        #digits 1-9
        characters += string.digits
    if symbols:
        
        #all symbols such as @,* ect
        characters += string.punctuation

    #if non selected comes up with error message
    if not any((uppercase, lowercase, digits, symbols)):
        CTkMessagebox(title="Error", message="Please select at least one character type." ,icon="cancel")
        return

    #join randomly for the length selected
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.configure(text=password)

#save password to password.txt

def save_password():
    
    #create file if not there
    create_password_file()
    
    #get password
    password = password_label.cget("text")
    if password:
        directory = os.getcwd()
        file_path = os.path.join(directory, "password.txt")
        
        #(a) is append which means add password below
        with open(file_path, "a") as e:
            
            #writes password in 
            e.write(password + "\n")
            
            #success message
        CTkMessagebox(title="Success", message=f"Password saved to {file_path}",icon="check")
    else:
        
        #error message
        CTkMessagebox(title="Error", message="No password generated yet.",icon="cancel")
        
# Function to clear the contents of a file
def clear_file(filename):
    try:
        with open(filename, 'w'):  # Open the file in write mode 
            
            pass  # No need to write anything, the file will be overwritten
        
        print(f"File '{filename}' cleared successfully.")  # Print a message indicating success
        
    except Exception as e:
        print(f"Error clearing file '{filename}': {e}")  #Print any error that occurs

#display saved passwords 
def display_saved(event=None):
    
    #create file if not there
    create_password_file()
    
    #reads the file using (r)
    with open("password.txt", "r") as d:
        
        #reads the lines
        saved_passwords = d.readlines()
        
        #checks entered password and checks if in the file to access the rest
        saved_passwords = [password.strip() for password in saved_passwords]

    #success messsage displays passwords with options to clear
    response = messagebox.askyesno("Password Match", f"Saved passwords:\n\n\n{saved_passwords}\n\n\nWould you like to clear saved passwords?")
    
    #if yes it clears the file 
    if response:
        print("Yes clicked")
        filename = "password.txt"
        clear_file(filename)
        
    #if no it exits
    else:
        exit()

#gets password when inputed using the button if entered isnt used
def get_password():
    
    #get the input using .get()
    inputed = label.get()
    
    #prints what was entered into console 
    print("Entered:", inputed) 
    
    

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#root is the name
root = customtkinter.CTk()

#title of app 
root.title("Password Generator")

#size of screen
root.geometry("430x932")

#colour theme (green, darkblue, blue)
customtkinter.set_default_color_theme("blue")

#length off password

length_label = customtkinter.CTkLabel(master=root, text="Enter the length of the password:")
length_label.grid(row=0, column=0,padx=10, pady=5)

#password length entry box

length_entry = customtkinter.CTkEntry(master=root, placeholder_text="Password Length")
length_entry.grid(row=0, column=1, padx=10, pady=5)


#true or flase for option 

uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

#check boxes for true or false

uppercase_check = customtkinter.CTkCheckBox(master=root, text="Include uppercase letters?", variable=uppercase_var)
lowercase_check = customtkinter.CTkCheckBox(master=root, text="Include lowercase letters?", variable=lowercase_var)
digits_check = customtkinter.CTkCheckBox(master=root, text="Include digits?", variable=digits_var)
symbols_check = customtkinter.CTkCheckBox(master=root, text="Include symbols?", variable=symbols_var)

# size and placement

uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
lowercase_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
digits_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
symbols_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# generate button

generate_button = customtkinter.CTkButton(master=root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# password label about where will generate

password_label = customtkinter.CTkLabel(master=root, text="")
password_label.grid(row=6, column=0, columnspan=2, sticky="nsew", padx=(10, 0))  # Centered vertically and horizontally



def copy_to_clipboard():
    
    # Get the text to copy
    
    text_to_copy = password_label.cget("text")
    print(text_to_copy)
    
    # Copy the text to the clipboard
    
    pyperclip.copy(text_to_copy)
    
    # Show a message box to indicate success
    
    messagebox.showinfo("Copy to Clipboard", "Text copied to clipboard successfully!")
   
# Load the copy icon image with a transparent background

copy_icon = tk.PhotoImage(file="copy.png").subsample(2)  # Adjust subsample factor as needed


# Create a label widget for the button with a transparent background

copy_label = tk.Label(root, image=copy_icon, bg="#242424")
copy_label.grid(row=6, column=1, sticky="nsew", padx=(0, 10))  # Centered vertically and horizontally

# Bind the copy_to_clipboard function to the label
copy_label.bind("<Button-1>", copy_to_clipboard)



# save password button 

save_button = customtkinter.CTkButton(master=root, text="Save Password", command=save_password)
save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

#show button instead of hidden 

def show_button():
    
    #place holder text which shows when clicked and button for label
    label.configure(placeholder_text="Enter Password to View")
    label.grid()
    
    #text to show when clicked for labele
    labele.configure(text="Check" , width=5 , height=2)
    labele.grid()

#display button to show entery 

display_button = customtkinter.CTkButton(master=root, text="Display Passwords", command=show_button)
display_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

#displays when clicked uses entry to pop up passwords saved 

label = customtkinter.CTkEntry(master=root, placeholder_text="")
label.grid(row=9 , column=0, columnspan=2, padx=10, pady=5)
label.grid_remove()

#use enter to submit

label.bind("<Return>", get_password )

#shows a input button to take entry if cant use enter

labele = customtkinter.CTkButton(master=root, text="", command=get_password , width=0, height=0)
labele.grid(row=10, column=0, columnspan=2, padx=10, pady=5)
labele.grid_remove() 

root.mainloop()
