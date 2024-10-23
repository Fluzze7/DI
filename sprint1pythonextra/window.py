import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from PIL import Image
from pptia import IA
from data import *

def goto_lobby():
    game_frame.grid_forget()
    main.grid()

def close_app():
    messagebox.showinfo(title="Results",message=f"You won: {wins} over the course of: {wins+looses} games. Congratulations.")
    reset_values()
    main.quit()

def play_game():
    main.grid_forget()  # Hide main screen
    game_frame.grid(row=0, column=0, sticky="nsew")
    global username
    username = name_entry.get()
    if username == "":
        username = "NO NAME"
    user_label.configure(text=username)

def show_response(choice):
    global ia_score
    global user_score
    if ia_score < 3 and user_score < 3:
        ia_response = ia.answer()
        response_photo = Image.open(ia_response + ".png")
        response_image = ctk.CTkImage(light_image=response_photo, size=(tamx, tamy))
        response_label.configure(image=response_image, text="")
        add_point(ia_response, choice)

    if (ia_score == 3 or user_score == 3) and not play_again_button_exists:
        restart_game_button.pack()
    if ia_score == 3:
        global looses
        looses +=1
    elif user_score == 3:
        global wins
        wins +=1
def restart_game():
    global ia_score
    global user_score
    ia_score = 0
    user_score = 0
    exchange_status.configure(text="")
    restart_game_button.pack_forget()
    user_score_label.configure(text=f"Score: {user_score}")
    ia_score_label.configure(text=f"Score: {ia_score}")



def add_point(ia_response, user_response):
    global ia_score
    global user_score
    alter_user_tendencies(user_response)
    posible_combinations = {
        "rockrock": "Draw...",
        "rockpaper": "You win...",
        "rockscissors": "I win",
        "paperrock": "I win",
        "paperpaper": "Draw...",
        "paperscissors": "You win...",
        "scissorsrock": "You win...",
        "scissorspaper": "I win",
        "scissorsscissors": "Draw...",
    }
    response = posible_combinations[ia_response + user_response]
    exchange_status.configure(text=response)
    if response == "I win":
        ia_score+=1
    elif response == "You win...":
        user_score+=1
    user_score_label.configure(text=f"Score: {user_score}")
    ia_score_label.configure(text=f"Score: {ia_score}")
    if ia_score == 3 or user_score == 3:
        exchange_status.configure(text="THE WINNER OF THIS ROUND IS: " + winner())


def winner():
    return username if user_score > ia_score else "IA"

username="admin"
ia_score = 0
user_score = 0
play_again_button_exists = False

wins = 0
looses = 0
# Image sizes
tamx = 100
tamy = 100
ctk.set_appearance_mode("dark")
ia = IA()
reset_values()
# Root window
root = ctk.CTk()
root.title("Piedra Papel o Tijera CUSTOM")
root.geometry("700x600")
root.resizable(False,False)

# Configure root grid to allow expansion
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Create the main frame
main = ctk.CTkFrame(root)
main.grid()


# Main screen labels and input
main_label = ctk.CTkLabel(main, text="Welcome to rock, paper and scissors.", font=("Arial", 30, "bold"))
main_label.grid(row=0, column=0, pady=5, padx=10, columnspan=2)

under_main_label = ctk.CTkLabel(main, text="Please enter your username", font=("Arial", 15, "italic"))
under_main_label.grid(row=1, column=0, pady=5, columnspan=2)

name_entry = ctk.CTkEntry(main)
name_entry.grid(row=2, column=0, pady=5, columnspan=2)

# Play button
play_button = ctk.CTkButton(main, text="Play", command=play_game)
play_button.grid(row=4, column=0, pady=10, columnspan=2)


# Create a standard tk.Menu for the root window
main_menu = tk.Menu(root)
root.config(menu=main_menu)

# Add "Game" menu
game_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Game", menu=game_menu)
game_menu.add_command(label="Lobby", command=goto_lobby)

# Add "Options" menu
leave_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Options", menu=leave_menu)
leave_menu.add_command(label="Rate it", command=lambda: rate_app(username, "5"))
leave_menu.add_separator()
leave_menu.add_command(label="Leave game", command=close_app)

# Game frame (hidden until the game starts)
game_frame = ctk.CTkFrame(root)

# Configure game frame grid
game_frame.grid_rowconfigure(0, weight=1)  # Upper frame row
game_frame.grid_rowconfigure(1, weight=1)  # Bottom frame row
game_frame.grid_columnconfigure(0, weight=1)  # Allow left column to expand
game_frame.grid_columnconfigure(1, weight=1)  # Allow right column to expand

# Upper frame (main container for user info and options)
upper_frame = ctk.CTkFrame(game_frame, height=200)  # Set fixed height for upper frame
upper_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=0)
upper_frame.grid_propagate(False)  # Prevent resizing based on content

# Left frame for user info (top-left position)
user_frame = ctk.CTkFrame(upper_frame)
user_frame.grid(row=0, column=0, padx=20, pady=0, sticky="nw")

# IA frame (right of the response frame)
ia_frame = ctk.CTkFrame(game_frame)
ia_frame.grid(row=2, column=1, padx=20, pady=0, sticky="ne")  # Cambiado a la columna 1 para colocarlo a la derecha

# IA image
ia_photo = Image.open("ia.png")
ia_image = ctk.CTkImage(light_image=ia_photo, size=(70, 80))
ia_image_label = ctk.CTkLabel(ia_frame, image=ia_image, text="")
ia_image_label.grid(row=0, column=0, pady=5)

# IA label (name)
ia_label = ctk.CTkLabel(ia_frame, text="IA", font=("Arial", 15))
ia_label.grid(row=1, column=0, pady=5)

# IA score label
ia_score_label = ctk.CTkLabel(ia_frame, text=f"Score: {ia_score}", font=("Arial", 15))
ia_score_label.grid(row=2, column=0, pady=5)

# Response frame (now also contains the IA section)
response_frame = ctk.CTkFrame(game_frame, height=200)  # Match the height of upper frame
response_frame.grid(row=2, column=0, columnspan=1, sticky="nsew", padx=10, pady=0)  # Set columnspan to 1
response_frame.grid_propagate(False)  # Prevent resizing based on content

# Response label (centered in the response frame)
response_label = ctk.CTkLabel(response_frame, text="")
response_label.grid(row=0, column=0, pady=5)

# User image (left of the upper frame)
user_photo = Image.open("user.png")
user_image = ctk.CTkImage(light_image=user_photo, size=(70, 80))
user_image_label = ctk.CTkLabel(user_frame, image=user_image, text="")
user_image_label.grid(row=0, column=0, pady=5)

# User label (name)
user_label = ctk.CTkLabel(user_frame, text="", font=("Arial", 15))
user_label.grid(row=1, column=0, pady=5)

# User score label
user_score_label = ctk.CTkLabel(user_frame, text=f"Score: {user_score}", font=("Arial", 15))
user_score_label.grid(row=2, column=0, pady=5)

# Center frame for options (rock, paper, scissors)
options_frame = ctk.CTkFrame(upper_frame)
options_frame.grid(row=0, column=1, padx=50, pady=75, sticky="nsew")  # Changed to "nsew" for expansion

# Option images
rock_photo = Image.open("rock.png")
rock_image = ctk.CTkImage(light_image=rock_photo, size=(tamx, tamy))
paper_photo = Image.open("paper.png")
paper_image = ctk.CTkImage(light_image=paper_photo, size=(tamx, tamy))
scissors_photo = Image.open("scissors.png")
scissors_image = ctk.CTkImage(light_image=scissors_photo, size=(tamx, tamy))

rock_label = ctk.CTkLabel(options_frame, image=rock_image, text="")
paper_label = ctk.CTkLabel(options_frame, image=paper_image, text="")
scissors_label = ctk.CTkLabel(options_frame, image=scissors_image, text="")

# Arranging the options in a grid, centered
rock_label.grid(row=0, column=0, padx=20)
paper_label.grid(row=0, column=1, padx=20)
scissors_label.grid(row=0, column=2, padx=20)

# Bindings for user input
rock_label.bind("<Button-1>", lambda event: show_response("rock"))
paper_label.bind("<Button-1>", lambda event: show_response("paper"))
scissors_label.bind("<Button-1>", lambda event: show_response("scissors"))

# Create a frame for the status label
status_frame = ctk.CTkFrame(game_frame)
status_frame.grid(row=1, column=0, columnspan=2, pady=2)  # Adjusted to row 1

# Status label inside the new frame
exchange_status = ctk.CTkLabel(status_frame, text="")
exchange_status.pack(pady=2)  # Use pack for simple layout management

restart_game_button = ctk.CTkButton(status_frame, text="Play again", command=restart_game)


# Start the main loop
root.mainloop()