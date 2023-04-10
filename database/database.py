import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)



cursor= mydb.cursor()


class Consulta():
    def identificador(self,**kwargs):
        consulta="SELECT id FROM muestras WHERE "
        i = 0
        for clave,valor in kwargs.items():
            if i==0:
                consulta += f"{clave}='{valor}'"
            else:
                consulta+= f" AND {clave}='{valor}'"
            i+=1
        try:
            cursor.execute(consulta)
            busqueda = cursor.fetchone()[0]
            cursor.execute("SELECT * FROM muestras WHERE id='{}'".format(busqueda))
            lista = cursor.fetchall()
            print(lista)
        except mysql.connector.Error as error:
            print("Ocurrió un error de MySQL: {}".format(error)) 
    




