import tkinter as tk
from tkinter import messagebox
from warnings import catch_warnings

from PIL import Image
import view
import model

class Controller:
    def __init__(self, notas_model, vista):
        self.notas_model = notas_model
        self.vista = vista
        self.vista.main_frame.bind("<Button-1>",self.update_cords)
        # Asignar funciones del controlador a los botones de la vista
        self.vista.add_button.config(command=self.add_notes)
        self.vista.remove_button.config(command=self.rem_notes)
        self.vista.load_notes_button.config(command=self.load_notes)
        self.vista.image_button.config(command=self.show_img_from_url)

    def update_cords(self,event):
        xvalue = event.x
        yvalue = event.y
        self.vista.title_label.config(text=f"First app with MVC, cords = x = {xvalue},y = {yvalue}.")

    def add_notes(self):
        self.notas_model.add_note(self.vista.note_listbox,self.vista.notes_entry.get())

    def rem_notes(self):
        self.notas_model.remove_note(self.vista.note_listbox,self.vista.note_listbox.curselection())

    def save_notes(self):
        try:
            self.notas_model.save_notes(self.vista.note_listbox)
        except FileNotFoundError:
            messagebox.showinfo(title="Error managing file",message="Are you using it?")
        else:
            messagebox.showinfo(title="Save successful", message="Your notes are safe in the document notes.txt")

    def load_notes(self):
        try:
            self.notas_model.load_notes(self.vista.note_listbox)
        except FileNotFoundError:
            messagebox.showinfo(title="Error managing file", message="Are you using it?")
        else:
            messagebox.showinfo(title="Save successful", message="Your notes are loaded in the list")

    def show_img_from_url(self):
        url = "https://raw.githubusercontent.com/Fluzze7/DI/main/sprint1pythonextra/rock.png"
        self.notas_model.start_download(url, self.update_image)

    def update_image(self, image_tk):
        if image_tk:
            self.vista.image_label.config(image=image_tk)
            self.vista.image_label.image = image_tk  # Mantener una referencia
        else:
            self.vista.image_label.config(text="Error al descargar la imagen.")


