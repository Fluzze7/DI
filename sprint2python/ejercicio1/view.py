# view.py
import tkinter as tk


class View:
    def __init__(self, root):
        self.root = root
        self.root.title("First MVC app")

        self.main_frame = tk.Frame(self.root, bg="grey")
        self.main_frame.pack(fill="both", expand=True)

        self.title_label = tk.Label(self.main_frame, text="First app with MVC", font=("Arial", 20), bg="grey")
        self.title_label.pack(pady=5)

        self.note_listbox = tk.Listbox(self.main_frame, width=60)
        self.note_listbox.pack()

        self.notes_label = tk.Label(self.main_frame, text="Insert new notes on the entry below", font=("Arial", 15),
                                    bg="grey")
        self.notes_label.pack(pady=5)

        self.notes_entry = tk.Entry(self.main_frame, width=40)
        self.notes_entry.pack(pady=5)

        self.image_label = tk.Label(self.main_frame, text="")

        self.button_frame = tk.Frame(self.main_frame, bg="grey")
        self.button_frame.pack(pady=5, side="bottom")

        self.add_button = tk.Button(self.button_frame, text="Add a note to the list.")
        self.add_button.pack(side="left", padx=5)

        self.remove_button = tk.Button(self.button_frame, text="Remove a note from the list.")
        self.remove_button.pack(side="left", padx=5)

        self.load_notes_button = tk.Button(self.button_frame, text="Load notes from file.")
        self.load_notes_button.pack(side="left", padx=5)

        self.image_button = tk.Button(self.button_frame, text="Show image.")
        self.image_button.pack(side="left", padx=5)

        self.image_label = tk.Label(self.main_frame, text="", bg="grey")  # Label para mostrar la imagen
        self.image_label.pack()