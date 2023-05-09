import customtkinter as ctk
from views.login_view import Login_view
from views.ensayos_view import Ensayos_view


import ctypes

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
root=ctk.CTk()
user = ctypes.windll.user32
user.SetProcessDPIAware()
ancho_pantalla = user.GetSystemMetrics(0)
alto_pantalla = user.GetSystemMetrics(1)
root.geometry(f"{ancho_pantalla}x{alto_pantalla}+0+0") #tamaño+posicionX+posicionY
root.title("POLVOS")




if __name__== "__main__":

    polvos= Login_view(root)
    if polvos.acceder:
        ensayos=Ensayos_view(root)
    else:
        pass
    root.mainloop()
    
    
    
    #abrimos el login
    

    #le damos a entrar


    #inicio.pack_forget()
    #esnayos=Polvos(root)
    #esnayos.inicio()

    































