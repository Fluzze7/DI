import tkinter as tk
from users import *


def close_app():
    root.quit()

def show_register_frame():
    list_frame.forget()
    register_frame.pack(fill="both",expand=True)

def show_list_frame():
    for user in users:
        users_listbox.insert(tk.END, user.name)
    register_frame.forget()
    list_frame.pack(fill="both", expand=True)

def update_age(value):
    edad_label.config(text=f"Edad: {value}")

def register_user():
    user = User(name_entry.get(),edad_scale.get(),genre_var.get())
    users.append(user)


def on_select(event):
    widget = event.widget
    selected_index = widget.curselection()

    if selected_index:
        user_data_label.config(text=users[selected_index[0]].to_str())


if __name__ == '__main__':

    root = tk.Tk()
    root.title("Aplicación de registro de usuarios")
    root.geometry("800x500")
    users = [User("Jose",25,"masculino")]
    menu_principal = tk.Menu(root)
    root.config(menu=menu_principal)
    register_frame = tk.Frame(root)
    list_frame = tk.Frame(root)
    register_frame.pack(expand=True)
    menu_principal.add_cascade(label="Altas", command=show_register_frame)
    menu_principal.add_cascade(label="Registro", command=show_list_frame)
    menu_principal.add_cascade(label="Salir",command=close_app)

    register_label_title = tk.Label(register_frame,text="Registro de usuarios",font=("Arial",24,"bold"))
    register_label_title.pack(pady = 5)
    register_label_name = tk.Label(register_frame,text="Nombre")
    register_label_name.pack(pady = 5)
    name_entry = tk.Entry(register_frame,width=50)
    name_entry.pack(pady=5)
    edad_label = tk.Label(register_frame,text="Edad: 0")
    edad_label.pack(pady=5)
    edad_scale = tk.Scale(register_frame,from_=0,to=100,orient="horizontal",command=update_age,length=200)
    edad_scale.pack(pady = 5)
    register_radiobuton_frame = tk.Frame(register_frame)
    register_radiobuton_frame.pack(side="top")

    register_label_genre = tk.Label(register_radiobuton_frame,text="Genero",font=("Arial",20,"bold"))
    register_label_genre.pack(pady=5)
    genre_var = tk.StringVar()
    genre_var.set("otro")
    radio1 = tk.Radiobutton(register_radiobuton_frame, text="Masculino", variable=genre_var, value="masculino")
    radio1.pack(pady = 5)
    radio2 = tk.Radiobutton(register_radiobuton_frame, text="Femenino", variable=genre_var, value="femenino")
    radio2.pack(pady = 5)
    radio3 = tk.Radiobutton(register_radiobuton_frame, text="Otro", variable=genre_var, value="otro")
    radio3.pack(pady = 5)

    reg_user_button = tk.Button(register_frame,text="Registrar usuario", command=register_user)
    reg_user_button.pack(pady = 5)

    list_label = tk.Label(list_frame,text="Usuarios registrados.",font=("Times",24,"italic"))
    list_label.pack(pady =  5)
    users_listbox = tk.Listbox(list_frame,selectmode=tk.SINGLE,bg="grey")
    users_listbox.pack(pady = 5)
    users_listbox.bind("<<ListboxSelect>>", on_select)
    user_data_label = tk.Label(list_frame,text="")
    user_data_label.pack(pady = 5)
    root.mainloop()