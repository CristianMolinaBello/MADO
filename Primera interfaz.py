import tkinter
import customtkinter
from PIL import Image

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.attributes("-fullscreen", True)
app.wm_attributes('-transparentcolor',app['bg'])
Width = app.winfo_screenwidth()
Height= app.winfo_screenheight()

def button_function():
    print(usuario.get())
    if usuario.get() == "maicol":
        print("si")
        if contra.get()== "1234":
            print("si")
            inicio.place_forget()
            usuarioLabel.place_forget()
            usuario.place_forget()
            contraseña.place_forget()
            Contraseñalabel.place_forget()
            button.place_forget()

            bienvenido = customtkinter.CTkLabel(app,text="Bienvenido Maicol", font=("Helvetica",80))
            bienvenido.place(relx=0.28, rely=0.4)



logo = customtkinter.CTkImage(light_image=Image.open("image\Fondo.png"),size=(Width,Height))

logolabel = customtkinter.CTkLabel(app, text="" , image=logo )
logolabel.place(relx=0, y=0)

inicio = customtkinter.CTkLabel(app,text="Iniciar sesión", font=("Helvetica",38), fg_color='transparent')

inicio.place(relx=0.42, y=200)

user = customtkinter.StringVar(app)
contra = customtkinter.StringVar(app)

usuarioLabel = customtkinter.CTkLabel(app,text="Usuario", font=("Helvetica",24))
usuarioLabel.place(relx=0.4, y=300)

usuario = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu usuario", corner_radius=50, textvariable=user)
usuario.place(relx=0.5, y=300)

Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )
Contraseñalabel.place(relx=0.4, y=400)

contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña", corner_radius=50,show="*",textvariable=contra )
contraseña.place(relx=0.5, y=400)

button = customtkinter.CTkButton(master = app, text="Ingresar", command=button_function)
button.place(relx=0.45, y=500)

app.mainloop()