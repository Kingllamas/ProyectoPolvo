import customtkinter as ctk
from views.login_view import Login_view
import mysql.connector
import os
import ctypes

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)


cursor= mydb.cursor()
"""class Main():
    def __init__(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")
        root=ctk.CTk()
        rutaAbsoluta= os.path.abspath(__file__)
        user = ctypes.windll.user32
        user.SetProcessDPIAware()
        ancho_pantalla = user.GetSystemMetrics(0)
        alto_pantalla = user.GetSystemMetrics(1)
        root.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0") #tamaño+posicionX+posicionY
        root.title("POLVOS")"""



if __name__== "__main__":
    

    polvos= Login_view()
    
    
    
    #abrimos el login
    

    #le damos a entrar


    #inicio.pack_forget()
    #esnayos=Polvos(root)
    #esnayos.inicio()

    































