# Number-guessing-game
generate complete details about this project to upload in my github and mentaion that its a simple guessing game but for output i used gif (memes of brahmanadham garu)
Got it! Here's a detailed description you can upload to your GitHub repository for your number guessing game project.

Number Guessing Game with GIFs
This is a simple number guessing game implemented in Python using the Tkinter library for the user interface and the Pillow (PIL) library for handling images. The game includes fun GIFs (memes of Brahmanandam Garu) to indicate whether the user's guess is too low, too high, or correct.

How It Works
Random Number Generation: The game generates a random number between 1 and 5.

User Input: The user inputs their guess through a graphical interface.

Feedback with GIFs: Based on the user's guess, the game displays a GIF:

A GIF for a low guess.

A GIF for a high guess.

A GIF for a correct guess.

End of Game: When the user guesses the correct number, they are informed via a popup message and the game ends.

Installation Instructions
Clone this repository to your local machine.

Ensure you have Python installed on your system. You can download it from python.org.

Install the required libraries:

sh
pip install pillow tkinter
Add the required GIFs to the same directory as the script:

low.gif (for low guesses)

high.gif (for high guesses)

correct.gif (for correct guesses)

Running the Game
Navigate to the directory where you cloned the repository.

Run the script using Python:

sh
python guessing_game.py
Code Details
Below is the code for the game:

python
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

# Function to display GIF
def display_gif(gif_path):
    try:
        img = Image.open(gif_path)
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
    except Exception as e:
        print(f"Error loading image: {e}")

# Initialize Tkinter window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate random number
number = random.randint(1, 5)

# Function to check user's guess
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
Notes
Ensure you have the proper GIFs named low.gif, high.gif, and correct.gif in the same directory as the script.

This project aims to provide a fun and interactive way to learn the basics of Python GUI programming and handling images.

Credits
Brahmanandam Garu for the hilarious memes that make this game more enjoyable!

Pillow Library for image handling.

Tkinter Library for the GUI framework.
