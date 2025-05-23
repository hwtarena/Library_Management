import tkinter as tk
from tkinter import font as tkFont # Import font module

def main():
    # Create the main application window
    root = tk.Tk()

    # Set the title of the window
    root.title("欢迎进入图书馆")

    # Set a reasonable initial size for the window
    root.geometry("400x300")

    # Define a prominent font for the title
    title_font = tkFont.Font(family="Arial", size=16, weight="bold")

    # Create the title label
    title_label = tk.Label(root, text="Welcome to the Library", font=title_font)

    # Pack the label at the top with some padding
    title_label.pack(pady=20)

    # Create a main content frame to hold forms and buttons
    main_content_frame = tk.Frame(root)
    main_content_frame.pack(pady=10, padx=10, fill="both", expand=True)

    # Create a frame for the login form (master is main_content_frame)
    login_frame = tk.Frame(main_content_frame)
    # login_frame is packed when made visible by toggle_form_action or initially

    # Username Label and Entry
    username_label = tk.Label(login_frame, text="Username:")
    username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w") # Align left
    username_entry = tk.Entry(login_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    # Password Label and Entry
    password_label = tk.Label(login_frame, text="Password:")
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w") # Align left
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a frame for the registration form (master is main_content_frame)
    registration_frame = tk.Frame(main_content_frame)
    # registration_frame is packed when made visible by toggle_form_action

    # Registration Form Elements
    reg_username_label = tk.Label(registration_frame, text="Username:")
    reg_username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    reg_username_entry = tk.Entry(registration_frame)
    reg_username_entry.grid(row=0, column=1, padx=5, pady=5)

    reg_password_label = tk.Label(registration_frame, text="Password:")
    reg_password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    reg_password_entry = tk.Entry(registration_frame, show="*")
    reg_password_entry.grid(row=1, column=1, padx=5, pady=5)

    confirm_password_label = tk.Label(registration_frame, text="Confirm Password:")
    confirm_password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    confirm_password_entry = tk.Entry(registration_frame, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=5, pady=5)

    email_label = tk.Label(registration_frame, text="Email:")
    email_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    email_entry = tk.Entry(registration_frame)
    email_entry.grid(row=3, column=1, padx=5, pady=5)

    # Hide the registration frame by default
    # registration_frame.pack_forget() # Will be managed by initial form setup in toggle_form_action logic

    # Updated submit_action function
    def submit_action():
        if current_form[0] == "login":
            # Get login form details
            login_user = username_entry.get()
            login_pass = password_entry.get()
            print(f"Login attempt: Username: {login_user}, Password: {login_pass}")
        elif current_form[0] == "register":
            # Get registration form details
            reg_user = reg_username_entry.get()
            reg_pass = reg_password_entry.get()
            reg_confirm_pass = confirm_password_entry.get()
            reg_email = email_entry.get()
            print(f"Registration attempt: Username: {reg_user}, Password: {reg_pass}, Confirm: {reg_confirm_pass}, Email: {reg_email}")
        # No other states expected for current_form[0] that would require an else here

    # Variable to keep track of the current form
    current_form = ["register"] # Start with "register" to force initial setup to "login"

    # Create the Submit button (master is main_content_frame)
    submit_button = tk.Button(main_content_frame, text="Login", command=submit_action)
    # submit_button is packed by toggle_form_action

    # Create the Toggle button (master is main_content_frame)
    toggle_button = tk.Button(main_content_frame, text="Switch to Register") # Command assigned later
    # toggle_button is packed by toggle_form_action

    # Function to toggle between login and registration forms
    def toggle_form_action():
        # Hide current form and buttons first
        login_frame.pack_forget()
        registration_frame.pack_forget()
        submit_button.pack_forget()
        toggle_button.pack_forget()

        if current_form[0] == "login":
            # Setup for registration form
            registration_frame.pack(pady=10) # Pack into main_content_frame
            submit_button.config(text="Register")
            toggle_button.config(text="Switch to Login")
            current_form[0] = "register"
        else: # current_form[0] is "register" or initial call
            # Setup for login form
            login_frame.pack(pady=10) # Pack into main_content_frame
            submit_button.config(text="Login")
            toggle_button.config(text="Switch to Register")
            current_form[0] = "login"

        # Repack buttons into main_content_frame
        submit_button.pack(pady=10)
        toggle_button.pack(pady=5)

    # Assign the command to the toggle button
    toggle_button.config(command=toggle_form_action)

    # Initially set up the login form view
    toggle_form_action() # Call once to set initial state (will switch from "register" to "login")

    # Keep the window open until it is manually closed
    root.mainloop()

if __name__ == "__main__":
    main()
