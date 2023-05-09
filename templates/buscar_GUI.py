import customtkinter as ctk #importamos tkinter
from tkinter import *
from tkinter import ttk,messagebox

class Buscar_Muestra():
    
    def __init__(self,view,root):
        self.root=root
        self.view=view

    def buscar_muestra(self):

        self.frame_filtros = ctk.CTkFrame(self.root,border_width=20)
        self.frame
