from templates.login_GUI import Login
#from database_buscar import Database

class Login_view():

    def __init__(self):
        self.login_gui = Login(self)
        #self.database = Database()
        pass
        
    
    def acceder(self,usuario, contraseña):
        print(usuario,contraseña)

    def iniciar(self):
        root= self.login_gui.login()
        root.mainloop()

    
        