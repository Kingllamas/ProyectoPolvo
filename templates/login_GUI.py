import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import ctypes

class Login():
    def __init__(self,view):
        self.view=view
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        self.root=ctk.CTk()
        self.rutaAbsoluta= os.path.abspath(__file__)
        user = ctypes.windll.user32
        user.SetProcessDPIAware()
        self.ancho_pantalla = user.GetSystemMetrics(0)
        self.alto_pantalla = user.GetSystemMetrics(1)
        self.root.geometry(f"{self.ancho_pantalla}x{self.alto_pantalla}+0+0") #tamaño+posicionX+posicionY
        self.root.title("POLVOS")    

 

    def login(self):  
            #Seleccionamos el fondo de la ventana
        imagent = ctk.CTkImage(light_image=Image.open(self.rutaAbsoluta + "\..\..\images\ondito.jpg"),size=(self.ancho_pantalla, self.alto_pantalla))
        self.fondo=ctk.CTkLabel(master=self.root,image=imagent,text='', fg_color= "transparent")
        self.fondo.pack()
 

            #Creamos el marco que contendrá el los inputs de acceso
        self.mAcceso=ctk.CTkFrame(master=self.fondo, width= 350, height= 400, fg_color= "white")
        self.mAcceso.place(relx=0.5,rely=0.5, anchor=tk.CENTER)
 

            #Acceso
        # Cargar la imagen y redimensionarla
        icono_principal=ctk.CTkImage(light_image=Image.open(self.rutaAbsoluta + "\..\..\images\Logo1.jpg"),size=(150, 150))
 

        # Crear un CTkLabel con la imagen

        lbl_iconoP = ctk.CTkLabel(master=self.mAcceso, image=icono_principal, text='')
        lbl_iconoP.place(relx= 0.5, y= 80, anchor= tk.CENTER)

        #Ponemos el título
        self.titulo_datos= ctk.CTkLabel(self.mAcceso,text= "ACCESO INFLAMABILIDAD LOM", font= ("Century Gothic",20), text_color="#06105b")
        self.titulo_datos.place(relx= 0.5, y= 190, anchor=tk.CENTER)

       
        #Input de usuario
        self.entry_usuario= ctk.CTkEntry(self.mAcceso,placeholder_text="Usuario", width=220)
        self.entry_usuario.place(relx= 0.5, y = 250, anchor= tk.CENTER)

 
        #input de contrseña
        self.entry_contraseña= ctk.CTkEntry(self.mAcceso, show="*",placeholder_text="Contraseña", width=220)
        self.entry_contraseña.place(relx= 0.5, y = 300, anchor= tk.CENTER)

 
        #entrar
        self.entrar = ctk.CTkButton(self.mAcceso, text= "Entrar", font= ("Calibri", 12), command= self.obtener_campos)
        self.entrar.place(relx= 0.5, y = 350, anchor= tk.CENTER)
 

        return(self.root)

       

    def obtener_campos(self):

        user = self.entry_usuario.get()

        password = self.entry_contraseña.get()

        self.view.acceder(user, password)
    


    def denegar(self):
            
            messagebox.showinfo("Acceso Denegado", "Usuario o contraseña incorrectos")
            self.entry_contraseña.delete(0,"end")

            
    def cerrar(self):
         
         self.mAcceso.pack_forget()
         self.fondo.pack_forget()
            



        


    





