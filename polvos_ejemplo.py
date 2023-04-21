#el entry point y mi funcion principal
import tkinter as tk
from usuariotk_paquete.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()       #creamos la ventana principal, mediante la clase tk que crea una interfaz
    root.title('Polvos')
    root.geometry("1280x720")

    #si quisieramos meter un logo:
    #root.iconbitmap('templates/logo.jpg') carpeta, nombre_archivo.jpg
    
    #si queremos cambiar el tamaño
    #root.resizable(0,0) booleanos que indican si se modifica en vertical o horizontal respectivamente

    barra_menu(root)

    #cuando hemos creado el paquete usuariotk_paquete lo llamamos para crear el Frame, tenemos que importarlo arriba
    app = Frame(root=root)

    app.mainloop()      #esto es para que se ejecute continuamente hasta que se cierre la ventana principal


if __name__=="__main__":
    main()

