from templates.ensayos_GUI import MenuEnsayos
from model.database_model import Database


class Ensayos_view():

    def __init__(self,root):

        self.ensayosview = MenuEnsayos(self,root)
        self.ensayosview.inicio()
        self.tareas_pendientes()
        
    def tareas_pendientes(self):
        modelo = Database()
        ids, identificadores, numeros, resultados = modelo.tareas_pendientes()
        self.ensayosview.insertar_tabla(ids,identificadores,numeros,resultados)


    