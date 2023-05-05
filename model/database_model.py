import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)


cursor= mydb.cursor()

estado = 0
seleccion = ""
filtros = ""

class Database():

    def controlAcceso(self, user, password):
        password= password
        cursor.execute(f"SELECT * FROM usuarios WHERE usuarios.nombre = '{user}' and usuarios.contraseña= '{password}'")
        lista = cursor.fetchall()
        return lista

    def ensayo(nombre,operador,valor):
        if estado==0:
            seleccion =  f"ensayos.{nombre}, resultados.resultado"
            filtros = f"{nombre} {operador} '{valor}' "
        else: 
            seleccion =  seleccion+ f"ensayos.{nombre}, resultados.resultado"
            filtros = seleccion + f"{nombre} {operador} '{valor}' "

    def numero(valor):
        if estado==0:
             seleccion =  "muestras.numero"
             filtros = f"numero = '{valor}' "
        else:
            seleccion = seleccion + "muestras.numero"
            filtros = filtros + f"numero = '{valor}' "  

    def identificador(valor):
        if estado==0:
             seleccion =  "muestras.identificador"
             filtros = f"identificador = '{valor}' "
        else:
            seleccion = seleccion + "muestras.identificador"
            filtros = filtros + f"identificador = '{valor}' "   

    def expediente(valor):
        if estado==0:
             seleccion =  "muestras.expediente"
             filtros = f"expediente = '{valor}' "
        else:
            seleccion = seleccion + "muestras.expediente"
            filtros = filtros + f"expediente = '{valor}' "   
    
    def peso(valor):
        if estado==0:
             seleccion =  "muestras.peso"
             filtros = f"peso = '{valor}' "
        else:
            seleccion = seleccion + "muestras.peso"
            filtros = filtros + f"peso = '{valor}' "  
    
    def material(valor):
        if estado==0:
             seleccion =  "muestras.material"
             filtros = f"material = '{valor}' "
        else:
            seleccion = seleccion + "muestras.material"
            filtros = filtros + f"material = '{valor}' "  
        
    def empresa(valor):
        if estado==0:
             seleccion =  "empresas.empresa"
             filtros = f"empresa = '{valor}' "
        else:
            seleccion = seleccion + "empresas.empresa"
            filtros = filtros + f"empresa = '{valor}' "
    def procedencia(valor):
        if estado==0:
             seleccion =  "procedencias.procedencia"
             filtros = f"procedencia = '{valor}' "
        else:
            seleccion = seleccion + "procedencias.procedencia"
            filtros = filtros + f"procedencia = '{valor}' "
    
    def fecha_recepcion(valor):
        if estado==0:
             seleccion =  "muestras.fecha_recepcion"
             filtros = f"fecha_recepcion = '{valor}' "
        else:
            seleccion = seleccion + "muestras.fecha_recepcion"
            filtros = filtros + f"fecha_recepcion = '{valor}' "  
    
    def fecha_fin(valor):
        if estado==0:
             seleccion =  "muestras.fecha_fin"
             filtros = f"fecha_fin = '{valor}' "
        else:
            seleccion = seleccion + "muestras.fecha_fin"
            filtros = filtros + f"fecha_fin = '{valor}' " 



    def resultado(valor):
        #Consulta
        pass
    
    def buscar(consulta):
        cursor.execute(f'''SELECT muestras.identificador, muestras.numero, {seleccion}
        FROM muestras 
        JOIN resultados ON resultados.id_muestras = muestras.id
        JOIN ensayos ON resultados.id_ensayos = ensayos.id
        JOIN empresas ON muestras.id_empresa = empresas.id
        JOIN procedencias ON muestras.id_procedencia = procedencias.id
        WHERE {filtros}''')
        pass
        #cursor.execute(consulta)

    









"""baseDatos= Database()

#Filtro | id | SAD 
consultaMuestra= baseDatos.muestra(filtro= "SAD")
# SAD | 26 | 23.189 Z
nfiltros= 3
nfiltro = 0

for i in  nfiltros:
    if (nfiltro >= nfiltros):
        nfiltro += 1"""




#filtro | resultado | tmic | >300


    



