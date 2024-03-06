# random numbers and strings
import random
#access strings 
import string
# gui 
import tkinter as tk
#message box
from tkinter import messagebox
#string input from user for tinker
from tkinter import simpledialog
#import os 
import os

#if file is there do nothing if it isnt make it 
def create_password_file():
    if not os.path.exists("password.txt"):
        # Create the file if it doesn't exist
        with open("password.txt", "w") as f:
            pass  # Do nothing, file is created
        
  
# generate the password
def generate_password():
    
    #get length
    length = int(length_entry.get())
    #if selected uppercase
    uppercase = uppercase_var.get()
    #if selected lowercase
    lowercase = lowercase_var.get()
    #if selected digits
    digits = digits_var.get()
    #if selected symbols
    symbols = symbols_var.get()

    characters = ''
    if uppercase:
        #all characted A-Z uppercase
        characters += string.ascii_uppercase
    if lowercase:
        #all characters a-z lowercase
        characters += string.ascii_lowercase
    if digits:
        #all digits 1-9
        characters += string.digits
    if symbols:
        #all symbols
        characters += string.punctuation

    #have to select one
    if not any((uppercase, lowercase, digits, symbols)):
        messagebox.showerror("Error", "Please select at least one character type.")
        return
    
    #join characters randomly for lenght selected
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text=password)
    
def save_password():
    create_password_file()
    # Get the generated password from the password_label widget
    password = password_label.cget("text")
    
    # Check if a password has been generated
    if password:
        # If a password exists, open a text file named "password.txt" for writing
        with open("password.txt", "a") as f:
            # Write the generated password to the file
            f.write(password)
            # Display a success message box indicating that the password has been saved
            messagebox.showinfo("Success", "Password saved to password.txt")
    else:
        # If no password has been generated yet, display an error message box
        messagebox.showerror("Error", "No password generated yet.")
        
def display_saved():
    create_password_file()
    inputed = simpledialog.askstring("Input", "What is the saved password?")

    with open("password.txt", "r") as f:
        saved_passwords = f.read()
        if saved_passwords == inputed:
            # Display the contents of the file in a messagebox
            messagebox.showinfo("Saved Passwords", saved_passwords)
        else:
            #if password wrong
             messagebox.showerror("Wrong Password")


def main():
    global length_entry, uppercase_var, lowercase_var, digits_var, symbols_var, password_label
# root = main window
# tk = class
#uses tinker

    root = tk.Tk()
    
    #title
    
    root.title("Password Generator")
    
    #label displays it using tinker , root will display on main window
    
    length_label = tk.Label(root, text="Enter the length of the password:")

    #grid: This method is used to place the label within its parent widget (in this case, the main window root) 
    # using a grid layout manager. The grid layout manager organizes widgets in rows and columns.

    #row=0, column=0: These parameters specify the row and column indices where the label should be placed 
    # within the grid. In this example, the label is placed in the first row (index 0) and first column (index 0) of the grid.

    #padx=10, pady=5: These parameters specify the padding (in pixels) to be added horizontally (padx) and 
    # vertically (pady) around the label. This adds some space between the label and other widgets in the grid layout.

    length_label.grid(row=0, column=0, padx=10, pady=5)
    length_entry = tk.Entry(root)
    length_entry.grid(row=0, column=1, padx=10, pady=5)
    
    # Create and place checkbuttons for selecting whether to include uppercase letters, lowercase letters, digits, and symbols
    
    uppercase_var = tk.BooleanVar()
    uppercase_check = tk.Checkbutton(root, text="Include uppercase letters?", variable=uppercase_var)
    uppercase_check.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    lowercase_var = tk.BooleanVar()
    lowercase_check = tk.Checkbutton(root, text="Include lowercase letters?", variable=lowercase_var)
    lowercase_check.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    digits_var = tk.BooleanVar()
    digits_check = tk.Checkbutton(root, text="Include digits?", variable=digits_var)
    digits_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    symbols_var = tk.BooleanVar()
    symbols_check = tk.Checkbutton(root, text="Include symbols?", variable=symbols_var)
    symbols_check.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    
    # Create and place a button for generating the password
    
    generate_button = tk.Button(root, text="Generate Password", command=generate_password)
    generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Create and place a label for displaying the generated password
    
    password_label = tk.Label(root, text="Your generated password will appear here", wraplength=200)
    password_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
    
    
    save_button = tk.Button(root, text="Save Password", command=save_password)
    save_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
    
    # Create a button to display saved passwords
    display_button = tk.Button(root, text="Display Passwords", command=display_saved)
    display_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
    
    # Start the Tkinter event loop
    
    root.mainloop()

# Check if the script is being run directly by the Python interpreter

if __name__ == "__main__":
    
    # If the script is being run directly, execute the following code
    
    main()  # Call the main function to start the Tkinter application
