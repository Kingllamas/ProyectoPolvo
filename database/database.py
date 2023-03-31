import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)


cursor= mydb.cursor()
class Consulta():
    def identificador(self,identificador,numero):
        consulta=f"SELECT id FROM muestras WHERE identificador = '{identificador}' AND numero = '{numero}' "
        cursor.execute(consulta)
        busqueda = cursor.fetchone()[0]
        cursor.execute("SELECT * FROM muestras WHERE id='{}'".format(busqueda))
        lista = cursor.fetchall()
        print(lista) 




