from templates.ensayos_GUI import MenuEnsayos
from model.database_model import Database


class Ensayos_view():

    def __init__(self,root):

        self.ensayosview = MenuEnsayos(self,root)
        self.ensayosview.inicio()
        

    