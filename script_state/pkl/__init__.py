import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import pickle

# File paths
STATE_FILE = "script_state.pkl"

# Helper Functions
def validate_input(input_text):
    """ Validates user input. """
    # Example validation: input should not be empty
    return input_text.strip() != ""

def save_state(state):
    """ Saves the script's state to a file. """
    with open(STATE_FILE, "wb") as file:
        pickle.dump(state, file)

def load_state():
    """ Loads the script's state from a file. """
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "rb") as file:
            return pickle.load(file)
    return None

# Command Functions
def execute_command(command):
    """ Executes a given command. """
    try:
        if command == "save":
            user_input = simpledialog.askstring("Input", "Enter state to save:")
            if validate_input(user_input):
                save_state(user_input)
                messagebox.showinfo("Success", "State saved successfully.")
            else:
                messagebox.showwarning("Warning", "Invalid input.")
        elif command == "load":
            state = load_state()
            if state:
                messagebox.showinfo("Loaded State", f"State: {state}")
            else:
                messagebox.showwarning("Warning", "No state found.")
        else:
            messagebox.showinfo("Command", f"Executing command: {command}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
def setup_gui():
    window = tk.Tk()
    window.title("Script Interface")

    save_btn = tk.Button(window, text="Save State", command=lambda: execute_command("save"))
    save_btn.pack()

    load_btn = tk.Button(window, text="Load State", command=lambda: execute_command("load"))
    load_btn.pack()

    # Additional buttons and functionalities can be added here

    return window

# Main Function
def main():
    window = setup_gui()
    window.mainloop()

if __name__ == "__main__":
    main()
