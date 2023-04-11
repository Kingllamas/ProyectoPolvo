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
        consulta="SELECT id FROM muestras WHERE "
        i = 0
        claves = ', '.join([clave for clave in kwargs if clave not in ('identificador', 'numero')])
        print(claves)
        for clave,valor in kwargs.items():
            if clave in ('identificador','numero','expediente','material','peso','id_procedencia','fecha_recepcion','fecha_fin','id_empresa'):
                nombre_tabla = 'muestras'
            elif clave == 'empresa':
                nombre_tabla = 'empresas'
            elif clave in ('ensayo','normativa','procedimiento','id_equipo1','id_equipo2','id_equipo3','id_equipo4','id_equipo5'):
                nombre_tabla = 'ensayos'
            elif clave == 'procedencia':
                nombre_tabla = 'procedencias'
            
            if i==0:
                consulta += f"{clave}='{valor}'"
            else:
                consulta += f" AND {clave}='{valor}'"
            i+=1
        try:
            cursor.execute(consulta)
            busqueda = cursor.fetchone()[0]
            cursor.execute(f"SELECT identificador, numero, {claves} FROM {nombre_tabla} WHERE id='{busqueda}'")
            lista = cursor.fetchall()
            print(lista)
        except mysql.connector.Error as error:
            print("Ocurrió un error de MySQL: {}".format(error)) 
    def all(self):
        cursor.execute("SELECT * FROM muestras ORDER BY fecha_fin DESC")
        lista = cursor.fetchall()
        
        
                           
        

        


    




