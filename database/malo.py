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
        identificador=''
        numero = ''
        for clave,valor in kwargs.items():
            if clave in ['identificador','numero','expediente','material','peso','fecha_recepcion','fecha_fin']:
                nombre_tabla = 'muestras'
                cursor.execute(f"SELECT id FROM {nombre_tabla} WHERE {clave}='{valor}'")
                idm = cursor.fetchall()
                idm = [n[0] for n in idm]
                val = []
                for n in idm:
                    cursor.execute(f"SELECT {clave} FROM {nombre_tabla} WHERE id = '{n}'")  
                    val.append(cursor.fetchone()[0])
                
            elif clave == 'empresa':
                nombre_tabla = 'empresas'
                cursor.execute(f"SELECT id FROM {nombre_tabla} WHERE {clave}='{valor}'")
                idempresa = [n[0] for n in cursor.fetchall()]
                cursor.execute(f"SELECT id FROM muestras WHERE id_empresa = '{idempresa}'")
                idm = [n[0] for n in cursor.fetchall()]
                for n in idm:
                    cursor.execute(f"SELECT identificador,numero FROM muestras WHERE id = '{n}'")
                    iden_num = [n[0] for n in cursor.fetchall()]
                    iden_num = {iden_num[0]:iden_num[1]}
                    
            elif clave in ['ensayo','normativa','procedimiento']:
                nombre_tabla = 'ensayos'
            elif clave == 'procedencia':
                nombre_tabla = 'procedencias'
            elif clave in ['fecha','temperatura','humedad','resultado','realizado']:
                nombre_tabla = 'resultados'
                cursor.execute(f"SELECT id FROM {nombre_tabla} WHERE {clave}='{valor}'")
                id=cursor.fetchone()[0] 
                cursor.execute(f"SELECT {clave} FROM {nombre_tabla} WHERE id = '{id}'")  
                val = cursor.fetchone()[0]
                cursor.execute(f"SELECT muestras.id FROM muestras INNER JOIN resultados ON muestras.id=resultados.id_muestras WHERE resultados.id_ensayos = {id}")
                idm = cursor.fetchone()[0]
            elif clave == 'equipo':
                nombre_tabla = 'equipos'
            else:
                return('No existe esta columna')
            cursor.execute(f"SELECT identificador,numero FROM muestras WHERE id='{idm}'")
            
        
            
            cursor.execute(f"SELECT id FROM {nombre_tabla} WHERE {clave}='{valor}'")
            id=cursor.fetchone()[0] 
            cursor.execute(f"SELECT {clave} FROM {nombre_tabla} WHERE id = '{id}'")  
            a = cursor.fetchone()[0]
            cursor.execute(f"SELECT muestras.id FROM muestras INNER JOIN resultados ON muestras.id=resultados.id_muestras WHERE resultados.id_ensayos = {id}")

            
            consulta="SELECT id FROM muestras WHERE "
            claves = ', '.join([clave for clave in kwargs if clave not in ('identificador', 'numero')]) 
            print(claves)
            
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
        
        

        
        
                           
        

        


    




