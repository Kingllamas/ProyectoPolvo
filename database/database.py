import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)



cursor= mydb.cursor()


class databases():
    def filter(self,**kwargs):
        cursor.execute("SHOW TABLES")
        tablas = cursor.fetchall()
        nombre_tabla=[]
        for tabla in tablas:
            nombre_tabla.append(tabla[0])
        print(nombre_tabla)
        consulta2="SELECT id FROM muestras WHERE "
        i = 0
        claves = ', '.join([clave for clave in kwargs if clave not in ('identificador', 'numero')])
        print(claves)
        for clave,valor in kwargs.items():
            if i==0:
                consulta2 += f"{clave}='{valor}'"
            else:
                consulta2 += f" AND {clave}='{valor}'"
            i+=1
        try:
            cursor.execute(consulta2)
            busqueda = cursor.fetchone()[0]
            cursor.execute(f"SELECT identificador, numero, {claves} FROM muestras WHERE id='{busqueda}'")
            lista = cursor.fetchall()
            print(lista)
        except mysql.connector.Error as error:
            print("Ocurrió un error de MySQL: {}".format(error)) 
    def all(self):
        cursor.execute("SELECT * FROM muestras ORDER BY fecha_fin DESC")
        lista = cursor.fetchall()
        
        
                           
        

        


    




