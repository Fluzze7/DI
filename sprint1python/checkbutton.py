import tkinter as tk
def show_hobbies():
    hobby_list = {"musica": "Tu afición es la música",
             "deporte": "Tu afición es el deporte",
             "leer": "Tu afición es la lectura",
             "leerdeporte": "Tus aficiones son la lectura y el deporte",
             "leermusica": "Tus aficiones son la lectura y la musica",
             "musicadeporte": "Tus aficiones son la musica y el deporte",
             "leermusicadeporte": "Todas las aficiones van contigo"}
    hobbies = ""
    if reading.get():
       hobbies += "leer"

    if music.get():
        hobbies += "musica"

    if sports.get():
        hobbies += "deporte"
    label1.config(text=f"{hobby_list.get(hobbies)}")

root = tk.Tk()
root.title("Ejercicio4")
root.geometry("600x250")
reading = tk.IntVar()
sports = tk.IntVar()
music = tk.IntVar()
check_reading = tk.Checkbutton(root, text="leer", variable=reading,command=show_hobbies)
check_reading.pack(pady = 5)
check_sports = tk.Checkbutton(root, text="deporte", variable=sports,command=show_hobbies)
check_sports.pack(pady = 5)
check_music = tk.Checkbutton(root, text="musica", variable = music ,command=show_hobbies)
check_music.pack(pady = 5)
label1 = tk.Label(root)
label1.pack(pady = 5)
root.mainloop()