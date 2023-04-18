import tkinter as tk
from tkinter import ttk, messagebox



def barra_menu(root):
    barra_menu=tk.Menu(root)  #creamos la barra de menu
    root.config(menu=barra_menu, width = 300, height = 300) #asi anclamos la barra a la raiz

    menu_inicio=tk.Menu(barra_menu,tearoff=0)                         #asi creamos las opciones en la barra de arriba,
    barra_menu.add_cascade(label='inicio',menu=menu_inicio)           # tearoff para borrar la linea que aparece encima  
    menu_inicio2 = tk.Menu(menu_inicio,tearoff=0)                     #creamos una opcion dentro de opcion, esto no tiene funcionalidad
    menu_inicio.add_cascade(label='inicio2',menu=menu_inicio2)        #lo que tiene funcionalidad son los comandos de dentro  
    menu_inicio3 = tk.Menu(menu_inicio,tearoff=0)   
    menu_inicio.add_cascade(label='inicio3',menu=menu_inicio3)
    #para crear un comando al pinchar aqui, la app va a hacer una cosa, en este caso destruir la raiz, es decir salir de la app.
    menu_inicio2.add_command(label='hacer una cosa', command=root.destroy)   


class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root,width=480,height=320)


        self.root=root             
        self.pack()
        self.config(bg='#ff9999') 
        
        #esto es lo que teniamos hecho en el modulo principal polvos(pero al separar los frames en otro paquete...): 
        #frame = tk.Frame(root) #creamos el lugar donde meteremos los cuadros de texto., botones, etc..
        #frame.pack()
        #frame.config(width=480, height=220, bg='#ff9999') #ancho, alto y color del fondo en rgb

        #para meter el label que hemos creado abajo en nuestro frame:
        self.busquedas()
        self.deshabilitar()
        self.tabla()

    def busquedas(self):
        self.label_nombre = tk.Label(self,text='nombre')        #asi se crea un cuadro de texto (LABEL)
        self.label_nombre.config(font=('Arial',12,'bold'))      #asi modificamos la fuente
        self.label_nombre.grid(row=0,column=0,padx=30,pady=20)  #asi situamos el cuadro en la columna y fila y con la separacion 

        self.nombre=tk.StringVar()  #creamos esto para asignar el texto del entry a una variable
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)          #asi creamos un cuadro donde insertar texto (ENTRY)
        self.entry_nombre.grid(row=0,column=1,padx=30,pady=20,columnspan=2)  #asi lo situamos igual que antes

        self.boton=tk.Button(self,text='boton',command=self.habilitar)       #asi creamos un boton (BUTTON)
        self.boton.config(width=10,fg='#DAD5D6',bg='#158645')               #htmlcolorcodes.com  enlace para conseguir colores en hexadecimal
        self.boton.grid(row=1,column=0,padx=30,pady=20)                      #asi lo situamos

        self.boton2=tk.Button(self,text='boton2',command=self.deshabilitar)                 #asi creamos un boton (BUTTON)
        self.boton2.config(width=10,fg='#DAD5D6',bg='#158645')   #htmlcolorcodes.com  enlace para conseguir colores en hexadecimal
        self.boton2.grid(row=1,column=1,padx=30,pady=20) 

        self.boton3=tk.Button(self,text='boton',command=self.guardar)      #asi creamos un boton (BUTTON)
        self.boton3.config(width=10,fg='#DAD5D6',bg='#158645')      #htmlcolorcodes.com  enlace para conseguir colores en hexadecimal
        self.boton3.grid(row=1,column=2,padx=30,pady=20) 

    def habilitar(self):
        self.nombre.set('')   #el metodo set pone un valor en el campo, en este caso un entry
        self.entry_nombre.config(state='normal')
    def deshabilitar(self):
        self.nombre.set('')   
        self.entry_nombre.config(state='disabled')
    def guardar(self):
        self.nombre.get()

    def tabla(self):     #para crear una tabla
        self.tabla = ttk.Treeview(self, columns=('Identificador', 'Numero', 'Tmic','Tmin'))
        self.tabla.grid(row=2,column=0,columnspan=5,sticky='nse')

        #si quiero poner una scrollbar
        self.scroll=ttk.Scrollbar(self,orient='vertical',command=self.tabla.yview)
        self.scroll.grid(row=2,column=5,sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set) #para que la tabla se mueva segun la barra

        #para colocar los titulos de las columnas:
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Identificador')
        self.tabla.heading('#2', text='Numero')
        self.tabla.heading('#3', text='Tmic')
        self.tabla.heading('#4', text='Tmin')
        self.tabla.insert('',0,text='id',values=('sad','27','340','440')) #para insertar un valor en la tabla

# para mostrar una ventana emergente con un mensaje
#from tkinter import messagebox
#try: 
#lo que sea
#messagebox.info

#para guardar los datos en la base de datos
#creo un metodo que meta un objeto en la base de datos, INSERT INTO...
#creo un metodo que cree ese objeto con los datos que he escrito en los entrys, 
#ej: self.nombre.get()




