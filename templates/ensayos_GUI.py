import customtkinter as ctk #importamos tkinter
from tkinter import *
from tkinter import ttk,messagebox

class MenuEnsayos():
    
    def __init__(self,view,root):
        self.root=root
        self.view=view

        #------titulo-------
        #titulo=Label(self.root,text="ENSAYOS",font=("cooper black",30,"bold"),border_color="#2C82F8",fg="white")
        #titulo.place(x=0,y=0,width=1280)
        #titulo.pack(expand=True,fill=BOTH)
        
        #-----Menu---------
        barra_menu=Menu(root)
        self.root.config(menu=barra_menu, width = 300, height = 300) 
        Inicio=Menu(barra_menu,tearoff=0)                         #asi creamos las opciones en la barra de arriba,
        barra_menu.add_command(label='INICIO',command=self.reinicio)
        
        
        

    def inicio(self):

        self.frame_inicio=ctk.CTkFrame(self.root,border_width=30)
        
        #-----botones-----------
        self.frame_botones=ctk.CTkFrame(self.frame_inicio,border_width=30,width=1280) 
       

        self.frame_botones.pack(expand=True,fill=BOTH)
        self.boton_buscar=ctk.CTkButton(self.frame_botones,text='Buscar Muestra',font=('cooper black',25,'bold'),command=self.buscar_muestra,corner_radius=50)       
        self.boton_buscar.configure(width=20,border_color='#2C82F8',cursor="hand2")                
        self.boton_buscar.pack(fill=BOTH,expand=True,side=LEFT,ipady=60)
                            

        self.boton_insertar=ctk.CTkButton(self.frame_botones,text='Nueva Muestra',font=('cooper black',25,'bold'),command=self.nueva_muestra,corner_radius=50)                 
        self.boton_insertar.configure(width=20,border_color='#2C82F8',cursor="hand2")   
        self.boton_insertar.pack(fill=BOTH,expand=True,side=RIGHT,ipady=60)     
        

        #------tabla--------
        
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('cooper black', 16,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        self.frame_tabla=ctk.CTkFrame(self.frame_inicio,border_width=100)
        self.frame_tabla.pack(expand=True,fill=BOTH)
        self.scrolly=ctk.CTkScrollbar(self.frame_tabla,orientation='vertical')
        self.scrolly.pack(side=RIGHT,fill="y")
        self.scrollx=ctk.CTkScrollbar(self.frame_tabla,orientation='horizontal')
        self.scrollx.pack(side=BOTTOM,fill="x")
        self.tabla=ttk.Treeview(self.frame_tabla,columns=("Identificador","Numero","tminube","tmicapa","LIE","EMI","EXPLO","Hum","Granulo","TAI","N1","N2","N4","Pmax","dp/dt","kmax","TG/DSC","CLO","O1","REC","TEV"),
                           yscrollcommand=self.scrolly.set,show='headings',style='mystyle.Treeview',xscrollcommand=self.scrollx.set)
        #tabla.place(x=0,y=240,relwidth=1,relheight=1)
        self.scrolly.configure(command=self.tabla.yview)
        self.scrollx.configure(command=self.tabla.xview)
        self.tabla.tag_configure('Treeview',font=('Montserrat,12'))
        for n in ["Identificador","Numero","tminube","tmicapa","LIE","EMI","EXPLO","Hum","Granulo","TAI","N1","N2","N4","Pmax","dp/dt","kmax","TG/DSC","CLO","O1","REC","TEV"]:
            self.tabla.heading(n,text=n)
            self.tabla.column(n,width=180)
        #tabla.grid(row=1,column=0,sticky='nsew')
        self.tabla.pack(expand=True,fill=BOTH,padx=5,pady=5)
        self.frame_inicio.pack(expand=True,fill=BOTH)
        
        #style=ttk.Style('Treeview',background=)
        """for i in range(2):
            n=self.tabla.insert(parent="",text=i,index=1,values=('','','hola',i))
            self.tabla.set(n,"LIE","pene")"""
        #for i in range(20):
            #self.tabla.insert(parent="",index=1,values=('adios','que','tal'))

        self.frames=[self.frame_botones,self.frame_inicio,self.frame_tabla]

        
    
    def reinicio(self):
        self.ocultar()
        self.inicio()
            
        
    def buscar_muestra(self):
        self.ocultar()
        

    def nueva_muestra(self):
        self.ocultar()

    def ocultar(self):
        for frame in self.frames:
            frame.pack_forget()
            
    def insertar_tabla(self,ids,identificadores,numeros,resultados):

        for i,valor in enumerate(ids):
            item = self.tabla.insert(parent="",text=valor,index=1,values=(identificadores[i],numeros[i]))
            for clave,valor in resultados[i].items():
                self.tabla.set(item,clave,valor)

        
        



