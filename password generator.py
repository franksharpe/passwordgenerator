# password random generator which allows you to save it

#gui
import tkinter as tk
from tkinter import messagebox, simpledialog
from ttkthemes import ThemedStyle
#operating system
import os
#randomize strings
import random
#strings
import string
from tkinter import *
#theme
import customtkinter
#messagebox
import CTkMessagebox



# Function to create the password file if it doesn't exist
def create_password_file():
    if not os.path.exists("password.txt"):
        # Create the file if it doesn't exist
        with open("password.txt", "w"):
            pass  # Do nothing, file is created

# Function to generate a password based on user input
def generate_password():
    #options
    
    #length
    length = int(length_entry.get())
    #uppercase
    uppercase = uppercase_var.get()
    #lowercase
    lowercase = lowercase_var.get()
    #digits
    digits = digits_var.get()
    #symbols
    symbols = symbols_var.get()

    
    characters = ''
    if uppercase:
        #all A-Z
        characters += string.ascii_uppercase
    if lowercase:
        #all a-z
        characters += string.ascii_lowercase
    if digits:
        #all 1-9
        characters += string.digits
    if symbols:
        #all symbols
        characters += string.punctuation

    #if not selected any error message
    if not any((uppercase, lowercase, digits, symbols)):
        CTkMessagebox("Error", "Please select at least one character type.")
        return

    #join them randomly to create the password
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.configure(text=password)

# Function to save the generated password to a file
def save_password():
    # Create the password file if it doesn't exist
    create_password_file()
    
    password = password_label.cget("text")

    # Check if there is a password generated
    if password:
        # Get the current working directory
        directory = os.getcwd()
        # Construct the full path to the password file
        file_path = os.path.join(directory, "password.txt")
        
        # Open the file in append mode and write the password
        with open(file_path, "a") as e:
            # Add a newline character after each password to separate them
            e.write(password + "\n")
        
        # Display a success message with the file path
        CTkMessagebox.CTkMessagebox(title="Success", message=f"Password saved to {file_path}")
    else:
        # If no password is generated, display an error message
        CTkMessagebox.CTkMessagebox(title="Error", message="No password generated yet.", icon="cancel")
        
# Function to clear the contents of a file
def clear_file(filename):
    try:
        with open(filename, 'w'):  # Open the file in write mode (truncate)
            pass  # No need to write anything, the file will be truncated to zero length
        print(f"File '{filename}' cleared successfully.")  # Debugging: Print a message indicating success
    except Exception as e:
        print(f"Error clearing file '{filename}': {e}")  # Debugging: Print any error that occurs

def get_password():
    # Input the password from the entry box
    inputed = label.get()
    print("Entered:", inputed) 
    
def display_saved(event=None):
    create_password_file()

    def get_password():
        # Input the password from the entry box
        inputed = label.get()
        print("Entered:", inputed) 

    # Open and read the password file
    with open("password.txt", "r") as d:
        saved_passwords = d.readlines()
        # Remove whitespace characters 
        saved_passwords = [password.strip() for password in saved_passwords]

    # Display a message box with options
    response = messagebox.askyesno("Password Match", f"Saved passwords:\n\n\n{saved_passwords}\n\n\nWould you like to clear saved passwords?")

    # Check user response
    if response:
        print("Yes clicked")
        filename = "password.txt"
        clear_file(filename)
    else:
        exit()
# Main function to create and configure the GUI


    #global the function able to access
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, password_label , label , labele

    #root is the name of app
    root = customtkinter.CTk()
    #title 
    root.title("Password Generator")
    #size
    root.geometry("430x932")
    #colour theme either can have green , dark blue , blue .jason files can change it 
    customtkinter.set_default_color_theme("blue")
    
  
   # root.grid_rowconfigure(0, weight=1)
    #root.grid_columnconfigure(0, weight=1)   
    
    # create CTk scrollbar
    #ctk_textbox_scrollbar = customtkinter.CTkScrollbar(root)
    #ctk_textbox_scrollbar.grid(row=1, column=5, sticky="ns")

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
    
    #uses function to display the password once clicked will show button below
    def show_button():
        label.configure(placeholder_text="Enter Password to View")
        label.grid()
        labele.configure(text="Get Input")
        labele.grid()
        
    #Button to display saved passwords
    display_button = customtkinter.CTkButton(master=root, text="Display Passwords", command=show_button)
    display_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    
    # Create entry box when clicked 
    label = customtkinter.CTkEntry(master=root, placeholder_text="")
    print("Entered:", display_saved)
    label.grid(row=9 , column=0, columnspan=2, padx=10, pady=5)
    label.grid_remove()  # Hide the label initially
    
    # Bind the <Return> event to the on_enter function
    label.bind("<Return>", display_saved )
    
    # Create a button to retrieve the entered text
    labele = customtkinter.CTkButton(master= root, text="", command=get_password)
    labele.grid(row=10, column=1, padx=10, pady=5)
    labele.grid_remove() 

    
        
    #class ToplevelWindow(customtkinter.CTkToplevel):
     #   def __init__(self, *args, **kwargs):
      #      super().__init__(*args, **kwargs)
       #     self.geometry("400x300")

     #       self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
      #      self.label.pack(padx=20, pady=20)
            
       # def open_toplevel(self):
        #    if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
         #       self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
          #  else:
           #     self.toplevel_window.focus()  # if window exists focus it
            
    
    #loops thr app keeps it open 
    root.mainloop()

