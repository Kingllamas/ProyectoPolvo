from templates.login_GUI import Login

from model.database_model import Database


class Login_view():

    def __init__(self,root):
        self.login_gui = Login(self,root)
        self.login_gui.login()
                

        #self.database = Database()
    
        
    def acceder(self,user, password):

        modelo= Database()
        acceso= modelo.controlAcceso(user,password)

        if acceso:
            self.login_gui.cerrar()
            return True
                        
        else:
            self.login_gui.denegar()
        
    
