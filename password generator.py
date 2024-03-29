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
    
    global length
    
    #length in interger
    length = int(length_entry.get())
    

    
    # Check if the length exceeds 20 characters or is less than 1
    if length > 20 or length < 1:
        return
     
     
    # Update the columnspan of the Generate Password button based on the length
    password_label.grid_configure(columnspan=2 if length <= 9 else 1)
    
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
    
    


#app main page




#root is the name

root = customtkinter.CTk()

#title of app 
root.title("Password Generator")

# Create a Label widget for the heading
heading_label = tk.Label(root, text="Swiftly create a safe, \nunpredictable passphrase using \n my tool below", font=("Helvetica", 13))

# Place the Label widget using the grid layout manager
heading_label.grid(row=1, column=0 ,columnspan=3, padx=10, pady=10)



#size of screen
root.geometry("390x500")

#colour theme (green, darkblue, blue)
customtkinter.set_default_color_theme("blue")

#length off password

length_label = customtkinter.CTkLabel(master=root, text="Enter the length of the password:")
length_label.grid(row=3, column=1,padx=10, pady=5)

#password length entry box

length_entry = customtkinter.CTkEntry(master=root, placeholder_text="Password Length")
length_entry.grid(row=3, column=2, padx=10, pady=5)


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

uppercase_check.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
lowercase_check.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
digits_check.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
symbols_check.grid(row=8, column=0, columnspan=2, padx=10, pady=5)



# Generate button

generate_button = customtkinter.CTkButton(master=root, text="Generate Password", command=generate_password)
generate_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)


# password label about where will generate

password_label = customtkinter.CTkLabel(master=root, text="")
password_label.grid(row=10, column=0, columnspan=2, sticky="nsew", padx=(10, 0))  # Centered vertically and horizontally

# Function to hide the temporary message
def hide_temp_message():
    temp_message_label.config(text="")
    temp_message_label.place_forget()

# Function to display a temporary message
def display_temp_message(message, duration=2000):
    temp_message_label.config(text="Text Copied Successfully")
    temp_message_label.place(relx=0.5, rely=0.9, anchor="center")  # Place label at the bottom
    root.after(duration, hide_temp_message)

# Create a label widget for displaying temporary messages
temp_message_label = tk.Label(root, text="", bg="white", padx=10, pady=5 , width=420)

def copy_to_clipboard():
    global temp_message_label 
    print("text copy clicked!")
    
    # Get the text to copy
    text_to_copy = password_label.cget("text")
    print(text_to_copy)
    
    # Copy the text to the clipboard
    pyperclip.copy(text_to_copy)
    
    # Show a message box to indicate success
    display_temp_message("Password copied to clipboard")

# Load the copy icon image with a transparent background
copy_icon = tk.PhotoImage(file="copy.png").subsample(1)  

# Create a label widget for the button with a transparent background
copy_label = tk.Label(root, image=copy_icon, bg="#242424")

# Configure the label to adjust image size and reduce padding
copy_label.config(image=copy_icon, bg="#242424", padx=5, pady=5)  

# Pack or grid the label widget as desired
copy_label.grid(row=10, column=1, sticky="nsew", padx=(0, 10)) 

copy_label.bind("<Button-1>", lambda event: (copy_to_clipboard(), display_temp_message("Password copied to clipboard")))






# save password button 

save_button = customtkinter.CTkButton(master=root, text="Save Password", command=save_password)
save_button.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

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
display_button.grid(row=12, column=0, columnspan=2, padx=10, pady=5)

#displays when clicked uses entry to pop up passwords saved 

label = customtkinter.CTkEntry(master=root, placeholder_text="")
label.grid(row=13 , column=0, columnspan=2, padx=10, pady=5)
label.grid_remove()

#use enter to submit

label.bind("<Return>", get_password )

#shows a input button to take entry if cant use enter

labele = customtkinter.CTkButton(master=root, text="", command=get_password , width=0, height=0)
labele.grid(row=14, column=0, columnspan=2, padx=10, pady=5)
labele.grid_remove() 

root.mainloop()
