import customtkinter as ctk #importamos tkinter
from tkinter import *
from tkinter import ttk,messagebox

class Polvos:
    
    def __init__(self,root):
        self.root=root
        

        #------titulo-------
        #titulo=Label(self.root,text="ENSAYOS",font=("cooper black",30,"bold"),border_color="#2C82F8",fg="white")
        #titulo.place(x=0,y=0,width=1280)
        #titulo.pack(expand=True,fill=BOTH)
        
        #-----Menu---------
        barra_menu=Menu(root)
        self.root.config(menu=barra_menu, width = 300, height = 300) 
        Inicio=Menu(barra_menu,tearoff=0)                         #asi creamos las opciones en la barra de arriba,
        barra_menu.add_command(label='INICIO',command="")
        
        
        

    def inicio(self):
        self.frame_inicio=ctk.CTkFrame(self.root,border_width=30)
        #self.ocultar_framesinicio()
        #-----botones-----------
        self.frame_botones=ctk.CTkFrame(self.frame_inicio,border_width=30,width=1280) 
        #self.frame_botones.place(x=0,y=0) 

        self.frame_botones.pack(expand=True,fill=BOTH)
        self.boton_buscar=ctk.CTkButton(self.frame_botones,text='Buscar Muestra',font=('cooper black',25,'bold'),command="",corner_radius=50)       
        self.boton_buscar.configure(width=20,border_color='#2C82F8',cursor="hand2")               
        #boton_buscar.grid(row=1,column=0,padx=250) 
        self.boton_buscar.pack(fill=BOTH,expand=True,side=LEFT,ipady=60)
                            

        self.boton_insertar=ctk.CTkButton(self.frame_botones,text='Nueva Muestra',font=('cooper black',25,'bold'),command="",corner_radius=50)                 
        self.boton_insertar.configure(width=20,border_color='#2C82F8',cursor="hand2")   
        #boton_insertar.grid(row=1,column=1,padx=237)
        self.boton_insertar.pack(fill=BOTH,expand=True,side=RIGHT,ipady=60)

        #-----frame principal---------
        #"""frame_principal=Frame(self.root,border_width=2,border_color="#BAC2CC",width=1280)
        #frame_principal.place(x=0,y=160)   
        #frame_principal.pack(expand=True,fill=BOTH)
        #frame_principal.columnconfigure(0, weight=1)"""
            
        
        

        #------tabla--------
        #pendientes=Label(frame_principal,text="TAREAS PENDIENTES",border_color="blue",fg="white")
        #pendientes.grid(row=1)  
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('cooper black', 16,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
        self.frame_tabla=ctk.CTkFrame(self.frame_inicio,border_width=100)
        self.frame_tabla.pack(expand=True,fill=BOTH)
        self.scroll=ctk.CTkScrollbar(self.frame_tabla,orientation='vertical')
        self.scroll.pack(side=RIGHT,fill="y")
        self.tabla=ttk.Treeview(self.frame_tabla,columns=("Identificador","Numero","Tmin","Tmic","LIE","EMI","EXPLO","Hum","Granulo"),
                           yscrollcommand=self.scroll.set,style='mystyle.Treeview',show='headings')
        #tabla.place(x=0,y=240,relwidth=1,relheight=1)
        self.scroll.configure(command=self.tabla.yview)
        self.tabla.tag_configure('Treeview',font=('Montserrat,12'))
        for n in ["Identificador","Numero","Tmin","Tmic","LIE","EMI","EXPLO","Hum","Granulo"]:
            self.tabla.heading(n,text=n)
            self.tabla.column(n,width=120)
        #tabla.grid(row=1,column=0,sticky='nsew')
        self.tabla.pack(expand=True,fill=BOTH,padx=5,pady=5)
        self.frame_inicio.pack(expand=True,fill=BOTH)
        #style=ttk.Style('Treeview',background=)
        #for i in range(10):
            #self.tabla.insert(parent="",index=1,values=('hola','que','tal'))
        #for i in range(20):
            #self.tabla.insert(parent="",index=1,values=('adios','que','tal'))

        
    
    
        


if __name__== "__main__":
    print(__name__)
    root=ctk.CTk()
    obj=Polvos(root)
    root.mainloop()
