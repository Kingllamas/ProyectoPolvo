import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import ctypes

class Login():
    def __init__(self,view):
        self.view=view
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.root=ctk.CTk()
        self.rutaAbsoluta= os.path.abspath(__file__)
        user = ctypes.windll.user32
        user.SetProcessDPIAware()
        self.ancho_pantalla = user.GetSystemMetrics(0)
        self.alto_pantalla = user.GetSystemMetrics(1) 
        self.root.geometry(f"{self.ancho_pantalla-400}x{self.alto_pantalla-200}+0+0") #tamaño+posicionX+posicionY
        self.root.title("POLVOS")
        

    def login(self):  
        imagen = Image.open(self.rutaAbsoluta + "\\..\\..\\images\\ondito.jpg")
        imagent= ImageTk.PhotoImage(imagen)
        
        self.fondo=ctk.CTkLabel(master=self.root,image=imagent,text='')
        
       
        """
        self.mAcceso=ctk.CTkFrame(master=fondo,corner_radius=20,fg_color='transparent',border_color="green") 
        self.mAcceso.place(relx=0.5,rely=0.5,anchor=tk.CENTER) 
        fondo.pack()

        return(self.root)"""  
        
        self.mAcceso=ctk.CTkFrame(master=self.fondo,corner_radius=15)
            #Marcos
        """self.marco_superior= ctk.CTkFrame(self.mAcceso,width= self.ancho_pantalla/4, height= self.alto_pantalla/4)
        self.marco_superior.pack()
        self.marco_central0= ctk.CTkFrame(self.mAcceso,width= self.ancho_pantalla/4, height= self.alto_pantalla/4, )
        self.marco_central0.pack()
        self.marco_central1= ctk.CTkFrame(self.mAcceso,width= self.ancho_pantalla/4, height= self.alto_pantalla/4)
        self.marco_central1.pack()
        self.marco_central2= ctk.CTkFrame(self.mAcceso,width= self.ancho_pantalla/4, height= self.alto_pantalla/4)
        self.marco_central2.pack()
        self.marco_inferior= ctk.CTkFrame(self.mAcceso,width= self.ancho_pantalla/4, height= self.alto_pantalla/4)
        self.marco_inferior.pack()"""
            #Crear imagen
        """self.logo= Image.open(self.rutaAbsoluta + "\..\..\images\Logo1.jpg")
        self.logo=self.logo.resize((int(self.alto_pantalla/4),int(self.alto_pantalla/4)), Image.ANTIALIAS)
        self.img= tk.PhotoImage(self.logo)
        pil_imagen =Image.open(self.img)
        imagen = ctk.CTkImage(light_image=self.logo, dark_image=self.logo)
        self.lbl_img= ctk.CTkLabel(self.mAcceso,image=imagen,text='') """
        #self.lbl_img.pack(anchor= 'center') 

            #self.Titulo
        self.titulo_datos= ctk.CTkLabel(self.mAcceso,text= "ACCESO INFLAMABILIDAD LOM", font= ("Calibri",20), fg_color= "#191970")
        #self.titulo_datos.grid(pady= 50, row=0,column=5,columnspan=1)
        self.titulo_datos.pack()

            #Variables

        self.usuario= tk.StringVar()
        self.contraseña = tk.StringVar()


            #Usuario
        icono_usuario= Image.open(self.rutaAbsoluta + "\..\..\images\Logo1.jpg")
        icono_usuario=icono_usuario.resize((int(self.alto_pantalla/25),int(self.alto_pantalla/25)), Image.ANTIALIAS)
        self.ico_usuario= ImageTk.PhotoImage(icono_usuario)
        self.lbl_usuario= ctk.CTkLabel(master=self.mAcceso,image=self.ico_usuario,text='')
        #self.lbl_usuario.grid(row=0, column = 0)
        self.lbl_usuario.pack()

        self.entry_usuario= ctk.CTkEntry(self.mAcceso, font=("Calibri",15),placeholder_text="Usuario")
        #self.entry_usuario.grid(row=0, column=1, pady= 20)
        self.entry_usuario.pack()
        
            #Contraseña
        self.icono_contraseña= Image.open(self.rutaAbsoluta + "\..\..\images\Logo1.jpg")
        self.icono_contraseña=self.icono_contraseña.resize((int(self.alto_pantalla/25),int(self.alto_pantalla/25)), Image.ANTIALIAS)
        self.ico_contraseña= ImageTk.PhotoImage(self.icono_contraseña)
        self.lbl_contraseña=ctk.CTkLabel(self.mAcceso,text='')
        #self.lbl_contraseña.grid(row=1, column=0)
        self.lbl_contraseña.pack()

        self.entry_contraseña= ctk.CTkEntry(self.mAcceso, font=("Calibri",15), show="*",placeholder_text="Contraseña")
        #self.entry_contraseña.grid(row=1,column = 1, pady= 10)
        self.entry_contraseña.pack()

            #Entrar
        self.entrar = ctk.CTkButton(self.mAcceso, text= "Entrar", font= ("Calibri", 12), fg_color= "#0C50AC", command=self.botonPresionado)
        self.entrar.pack(pady = 30)
        #self.titulo1= ctk.CTkLabel(self.mAcceso, font= ("Calibri",10))
        #self.titulo1.pack(pady=10)
        
        
        self.titulo= ctk.CTkLabel(self.mAcceso,text= "LABORATORIO OFICIAL J.M. MADARIAGA", font= ("Calibri",12), fg_color= "#191970")
        self.titulo.pack(pady=10)
        self.titulo= ctk.CTkLabel(self.mAcceso,text= "www.lom.upm.es", font= ("Calibri",12), fg_color= "#191970")
        self.titulo.pack(pady=10)

        self.mAcceso.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        self.fondo.pack()

        return(self.root)
        
    def obtener_campos(self):
        self.usuario = self.entry_usuario.get()
        self.contraseña = self.entry_contraseña.get()
        return self.usuario, self.contraseña
    def botonPresionado (self):
        return(self.usuario.get(),self.password.get())
        


    





