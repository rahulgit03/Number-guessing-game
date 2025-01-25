import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image

# Initialize Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate random number
number = random.randint(1, 5)

# Function to display GIF
def display_gif(gif_path):
    try:
        img = Image.open(gif_path)
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
    except Exception as e:
        print(f"Error loading image: {e}")

def check_guess():
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a number.")
        return

    if guess < number:
        display_gif("low.gif")
    elif guess > number:
        display_gif("high.gif")
    else:
        display_gif("correct.gif")
        messagebox.showinfo("Correct!", f"Correct! The number was {number}")
        root.quit()

# Create entry for user guess
entry = tk.Entry(root)
entry.pack()

# Create submit button
button = tk.Button(root, text="Submit", command=check_guess)
button.pack()

# Display panel for GIF
panel = tk.Label(root)
panel.pack()

# Run Tkinter loop
root.mainloop()
