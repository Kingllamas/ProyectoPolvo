from tkinter import * #importamos tkinter
from tkinter import ttk,messagebox

class polvos:
    def __init__(self,root):
        self.root=root
        self.root.title("Polvos")
        self.root.geometry("1280x720+0+0") #tamaño+posicionX+posicionY

        #------titulo-------
        #titulo=Label(self.root,text="ENSAYOS",font=("times new roman",30,"bold"),bg="#2C82F8",fg="white",relief="ridge")
        #titulo.place(x=0,y=0,width=1280)
        #titulo.pack(expand=True,fill=BOTH)
        
        #-----Menu---------
        barra_menu=Menu()
        self.root.config(menu=barra_menu, width = 300, height = 300)
        Inicio=Menu(barra_menu,tearoff=0)                         #asi creamos las opciones en la barra de arriba,
        barra_menu.add_command(label='INICIO',command=self.reinicio)
        self.inicio()
        

    def inicio(self):
        #self.ocultar_framesinicio()
        #-----botones-----------
        self.frame_botones=Frame(self.root,bd=3,bg="#BAC2CC",width=1280,relief="ridge")
        #frame_botones.place(x=0,y=80)
        self.frame_botones.pack(expand=True,fill=BOTH)
        self.boton_buscar=Button(self.frame_botones,text='Buscar Muestra',font=('times new roman',20,'bold'),command=self.buscar_muestra)       
        self.boton_buscar.config(width=20,fg='#DAD5D6',bg='#2C82F8',cursor="hand2")               
        #boton_buscar.grid(row=1,column=0,padx=250) 
        self.boton_buscar.pack(fill=BOTH,expand=True,side=LEFT,padx=150,pady=60)
                            

        self.boton_insertar=Button(self.frame_botones,text='Nueva Muestra',font=('times new roman',20,'bold'),command=self.nueva_muestra)                 
        self.boton_insertar.config(width=20,fg='#DAD5D6',bg='#2C82F8',cursor="hand2")   
        #boton_insertar.grid(row=1,column=1,padx=237)
        self.boton_insertar.pack(fill=BOTH,expand=True,side=RIGHT,padx=150,pady=60)

        #-----frame principal---------
        """frame_principal=Frame(self.root,bd=3,bg="#BAC2CC",width=1280,relief="ridge")
        frame_principal.place(x=0,y=160)   
        frame_principal.pack(expand=True,fill=BOTH)
        frame_principal.columnconfigure(0, weight=1)"""
            
        
        

        #------tabla--------
        #pendientes=Label(frame_principal,text="TAREAS PENDIENTES",bg="blue",fg="white")
        #pendientes.grid(row=1)     
        self.tabla_frame=Frame(self.root)
        self.tabla_frame.pack(expand=True,fill=BOTH)
        self.scroll=Scrollbar(self.tabla_frame,orient='vertical')
        self.scroll.pack(side=RIGHT,fill="y")
        self.tabla=ttk.Treeview(self.tabla_frame,columns=("Identificador","Numero","Tmin","Tmic","LIE","EMI","EXPLO","Hum","Granulo"),
                           show='headings',yscrollcommand=self.scroll.set)
        #tabla.place(x=0,y=240,relwidth=1,relheight=1)
        self.scroll.configure(command=self.tabla.yview)
        for n in ["Identificador","Numero","Tmin","Tmic","LIE","EMI","EXPLO","Hum","Granulo"]:
            self.tabla.heading(n,text=n)
            self.tabla.column(n,width=120)
        #tabla.grid(row=1,column=0,sticky='nsew')
        self.tabla.pack(expand=True,fill=BOTH,padx=5,pady=5)
        self.frames_inicio=[self.frame_botones,self.tabla_frame]
        #style=ttk.Style('Treeview',background=)
        
    def ocultar(self):
        for frame in self.frames_inicio:
            frame.pack_forget()
    def reinicio(self):
        self.ocultar()
        self.inicio()
    
    def buscar_muestra(self):
        self.ocultar()
        self.frame_buscar=Frame(self.root)
        self.frame_buscar.pack(expand=True,fill=BOTH)
        
    def nueva_muestra(self):
        self.ocultar()
        
        
                
        



if __name__== "__main__":
    root=Tk()
    obj=polvos(root)
    root.mainloop()
