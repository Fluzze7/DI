import customtkinter as ctk
def second_player_pick(choice):

root = ctk.CTk()
ctk.set_appearance_mode("dark")
root.title("ROCK, PAPER, SCISSORS")
root.geometry("800x600")
root.resizable(False,False)

mode_frame = ctk.CTkFrame(root)
game_frame = ctk.CTkFrame(root)
#página principal(seleccionar jugadores)
mode_frame.pack(fill="both",expand=True)
name_label=ctk.CTkLabel(mode_frame,text="Insert your username:", font=("Arial", 30, "bold"))
name_label.pack(pady = 5)
entry_name = ctk.CTkEntry(mode_frame)
entry_name.pack(pady=5)
second_player = ctk.CTkOptionMenu(mode_frame, values=["Player", "Machine"],command=second_player_pick)
second_player.pack()
root.mainloop()
