import tkinter as tk


def barra_menu(root):
    
class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=480,height=320)


        self.root=root             
        self.pack()
        self.config(bg='#ff9999') /'''width=480, height=220,'''
        

        #esto es lo que teniamos hecho en el modulo principal polvos(pero al separar los frames en otro paquete...): 
        #frame = tk.Frame(root) #creamos el lugar donde meteremos los cuadros de texto., botones, etc..
        #frame.pack()
        #frame.config(width=480, height=220, bg='#ff9999') #ancho, alto y color del fondo en rgb
