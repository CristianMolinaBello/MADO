import tkinter
import customtkinter
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw
import threading


import time

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.attributes("-fullscreen", True)



Width = app.winfo_screenwidth()
Height= app.winfo_screenheight()
bar = customtkinter.CTkProgressBar(master=app,orientation="horizontal", mode="indeterminate",indeterminate_speed=5,
                                   height=15, width=400, corner_radius= 50, border_width=2)


ImageHuellaCarga = customtkinter.CTkImage(light_image=Image.open("image\\HuellaCarga.png"),size=(150,150))
huellaCargalabel = customtkinter.CTkLabel(app, text="" , image=ImageHuellaCarga, height=50, width=50)
botonIniciar = customtkinter.CTkButton(master = app, text="Iniciar")

contador = 1 + 0

def entras():
    
    bar.stop()
    bar.place_forget()
    botonIniciar.place_forget()
    huellaCargalabel.place_forget()

    if(contador == 2):
        alerta = customtkinter.CTkToplevel()

        boto = customtkinter.CTkButton(master = alerta, text="Error en la huella",
                                                command= lambda: alerta.wm_forget)
        boto.pack(pady=10)
    else:
        Bienvenido()
            
    
t = threading.Timer(3, entras)


def validacion():
     if contra.get()== "1234":
          Bienvenido()

def Bienvenido():

    
    print("si")
    inicio.place_forget()
    contraseña.place_forget()
    Contraseñalabel.place_forget()
    button.place_forget()
    logolabel.place_forget()
    huellabutton.place_forget()

    bienvenido = customtkinter.CTkLabel(app,text="Bienvenido Maicol", font=("Helvetica",80))
    bienvenido.place(relx=0.28, rely=0.4)


def inicioHuella():
    
    contraseña.place_forget()
    Contraseñalabel.place_forget()
    button.place_forget()
       
    bar.place(relx=0.36,rely=0.67)
    global botonIniciar
    botonIniciar._command = inicioProgreso
    if(contador == 1):
        
        botonIniciar.place(relx=0.45, y=710)
    else:
        print("Vamos")
        botonIniciar.place_forget()
        botonIniciar.destroy()
        botonIniciar = customtkinter.CTkButton(master = app, text="Intentar nuevamente",command = inicioProgreso)
        botonIniciar.place(relx=0.45, y=710)
   
    
   

    



def inicioProgreso():
    global contador
    contador = contador + 1
    t = threading.Timer(3, entras)
    bar.start()
    huellaCargalabel.place(relx=0.45, y=550)
    t.start()
    
    



inicio = customtkinter.CTkLabel(app,text="Navarrete", font=("Helvetica",38), fg_color='transparent')
inicio.place(relx=0.42, y=150)


ImageUser = customtkinter.CTkImage(light_image=Image.open("image\\Navarrete.png"),size=(300,300))
logolabel = customtkinter.CTkLabel(app, text="" , image=ImageUser, height=30, width=30)
logolabel.place(relx=0.4, y=200)

ImageHuella = customtkinter.CTkImage(light_image=Image.open("image\\Huella.png"),size=(50,50))
huellabutton = customtkinter.CTkButton(app, text="" , image=ImageHuella, height=30, width=30, command=inicioHuella)
huellabutton.place(relx=0.9, y=700)


user = customtkinter.StringVar(app)
contra = customtkinter.StringVar(app)


Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )
Contraseñalabel.place(relx=0.4, y=550)


contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña",corner_radius=50,show="*",textvariable=contra )
contraseña.place(relx=0.5, y=550)


button = customtkinter.CTkButton(master = app, text="Ingresar", command=validacion)
button.place(relx=0.45, y=600)


app.mainloop()