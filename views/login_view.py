from templates.login_GUI import Login
from model.database_model import Database
#from database_buscar import Database

class Login_view():

    def __init__(self):
        self.login_gui = Login(self)
        self.root=self.login_gui.login()
        self.root.mainloop()
        

        #self.database = Database()
    
        
    def acceder(self,user, password):
        modelo= Database()
        acceso= modelo.controlAcceso(user,password)
        if acceso:
            self.login_gui.cerrar()
                        
        else:
            self.login_gui.denegar()
        
        