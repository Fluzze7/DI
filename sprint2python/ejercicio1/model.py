import threading
from ast import Bytes
from io import BytesIO
import requests
from PIL import Image, ImageTk
import tkinter as tk

class NotasModel:
    def __init__(self):
        self.image_tk = None
    def add_note(self, listbox, text):
        listbox.insert(tk.END, text)

    def remove_note(self, listbox, selection):
        if selection:
            listbox.delete(selection)

    def get_note_list(self, listbox):
        notes_list = []
        for note in listbox.get(0, tk.END):
            notes_list.append(note)
        return notes_list

    def save_notes(self, listbox):
        with open("notas.txt", "w") as file:  # Usar 'with' para asegurar el cierre
            for note in listbox.get(0, tk.END):
                file.write(note + "\n")

    def load_notes(self, listbox):
        listbox.delete(0, tk.END)  # Limpiar la lista actual antes de cargar
        try:
            with open("notas.txt", "r") as file:
                for note in file:
                    listbox.insert(tk.END, note.strip())
        except FileNotFoundError:
            print("El archivo notas.txt no existe.")  # Mensaje de error para control interno

    def download_image(self, url, callback):
        try:
            response = requests.get(url)
            response.raise_for_status()

            image = Image.open(BytesIO(response.content))
            image = image.resize((200, 200), Image.Resampling.LANCZOS)

            self.image_tk = ImageTk.PhotoImage(image)
            callback(self.image_tk)  # Llama al callback aquí
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")

    def start_download(self, url, callback):
        thread = threading.Thread(target=self.download_image, args=(url, callback))
        thread.start()