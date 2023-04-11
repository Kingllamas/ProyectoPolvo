import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)


cursor= mydb.cursor()

# si quieres eliminar una tabla usa el codigo de debajo
#cursor.execute("DROP TABLE empresa")



cursor.execute('''CREATE TABLE IF NOT EXISTS procedencias (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               procedencia VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS empresas (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               empresa VARCHAR(50),
               subsidiaria VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS equipos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               equipo VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS muestras (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               identificador VARCHAR(50),
               numero VARCHAR(50),
               expediente VARCHAR(50),
               material VARCHAR(50),
               peso VARCHAR(50),
               id_procedencia VARCHAR(50),
               FOREIGN KEY(id_procedencia) REFERENCES procedencias(id),
               fecha_recepcion VARCHAR(50),
               fecha_fin VARCHAR(50),
               id_empresa VARCHAR(50),
               FOREIGN KEY(id_empresa) REFERENCES empresa(id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS ensayos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               ensayo VARCHAR(50),
               normativa VARCHAR(50),
               procedimiento VARCHAR(50),
               id_equipo1 VARCHAR(50),
               FOREIGN KEY(id_equipo1) REFERENCES equipos(id),
               id_equipo2 VARCHAR(50),
               FOREIGN KEY(id_equipo2) REFERENCES equipos(id),
               id_equipo3 VARCHAR(50),
               FOREIGN KEY(id_equipo3) REFERENCES equipos(id),
               id_equipo4 VARCHAR(50),
               FOREIGN KEY(id_equipo4) REFERENCES equipos(id),
               id_equipo5 VARCHAR(50),
               FOREIGN KEY(id_equipo5) REFERENCES equipos(id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS resultados (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_muestras VARCHAR(50),
               FOREIGN KEY(id_muestras) REFERENCES muestras(id),
               id_ensayos VARCHAR(50),
               FOREIGN KEY(id_ensayos) REFERENCES ensayos(id),
               fecha VARCHAR(50),
               humedad VARCHAR(50),
               temperatura VARCHAR(50),
               resultado VARCHAR(50)
               realizado VARCHAR(50))''')   
cursor.execute('''CREATE TABLE IF NOT EXISTS tmicapa_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               temperatura VARCHAR(50),
               temperatura_de_plato VARCHAR(50),
               temperatura_maxima VARCHAR(50),
               resultado_ignicion VARCHAR(50),
               tiempo VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tminube_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               temperatura VARCHAR(50),
               peso VARCHAR(50),
               presion VARCHAR(50),
               resultado VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS emi_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               concentracion VARCHAR(50),
               energia VARCHAR(50),
               retardo VARCHAR(50),
               resultado VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS severidad_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               concentracion VARCHAR(50),
               pm_serie1 VARCHAR(50),
               pm_serie2 VARCHAR(50),
               pm_serie3 VARCHAR(50),
               dpdt_serie1 VARCHAR(50),
               dpdt_serie2 VARCHAR(50),
               dpdt_serie3 VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS rec_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               tension VARCHAR(50),
               duracion VARCHAR(50),
               resistencia VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tev_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               temperatura_referencia VARCHAR(50),
               temperatura_ensayo VARCHAR(50),
               temperatura_maxima VARCHAR(50),
               vapores_visibles VARCHAR(50),
               inflama VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS clo_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               concentracion_polvo VARCHAR(50),
               concentracion_oxigeno VARCHAR(50),
               peso_equivalente VARCHAR(50),
               pm VARCHAR(50),
               dpdt VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS onu_n1_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               numero_prueba VARCHAR(50),
               t3 VARCHAR(50),
               rebasa VARCHAR(50)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS onu_n2_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               numero_prueba VARCHAR(50),
               inflamacion VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS onu_n4_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               temperatura_estufa VARCHAR(50),
               celda VARCHAR(50),
               temperatura_maxima VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS onu_o1_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               mezcla VARCHAR(50),
               t1 VARCHAR(50),
               t2 VARCHAR(50),
               t3 VARCHAR(50),
               t4 VARCHAR(50),
               t5 VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS humedad_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               humedad VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS secado_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               secado VARCHAR(50),
               estufa VARCHAR(50),
               tiempo VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tamizado_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               tamizado VARCHAR(50),
               equipo VARCHAR(50),
               codigo VARCHAR(50),
               tamaño VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS molienda_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               molienda VARCHAR(50),
               equipo VARCHAR(50),
               tiempo VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS lie_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               concentracion VARCHAR(50),
               peso_equivalente VARCHAR(50),
               pex VARCHAR(50),
               pm VARCHAR(50),
               dpdt VARCHAR(50),
               observaciones VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS clase_combustion_datos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_resultados VARCHAR(50),
               FOREIGN KEY(id_resultados) REFERENCES resultados(id),
               hilera_polvo VARCHAR(50),
               tiempo VARCHAR(50))''')





#cursor.execute('INSERT INTO empresa (empresa) VALUES ("urike")')
#cursor.execute("SELECT id FROM empresa WHERE empresa = 'urike'")
#pene= cursor.fetchone()[0]
#cursor.execute(f'INSERT INTO muestras (identificador, numero, expediente, material, peso, fecha_recepcion, id_empresa) VALUES ("URK", "1" , "23,141 Q ", "granalla", "3", "2022-03-21", {pene})')

#cursor.execute('INSERT INTO procedencias (procedencia) VALUES ("barcelona")')
#cursor.execute('INSERT INTO procedencias (procedencia) VALUES ("galicia")')
#cursor.execute('INSERT INTO resultados (id_muestras,id_ensayos,fecha,humedad,temperatura,resultado) VALUES ("1","1","10/4/2023","11%","24","340º")')
#cursor.execute('INSERT INTO resultados (id_muestras,id_ensayos,fecha,humedad,temperatura,resultado) VALUES ("2","1","11/4/2023","12%","25","380º")')
#cursor.execute('INSERT INTO resultados (id_muestras,id_ensayos,fecha,humedad,temperatura,resultado) VALUES ("3","1","12/4/2023","13%","23","440º")')
#cursor.execute('INSERT INTO resultados (id_muestras,id_ensayos,fecha,humedad,temperatura,resultado) VALUES ("4","1","13/4/2023","14%","26","480º")')
#cursor.execute('INSERT INTO tmicapa_datos (id_resultados,temperatura,temperatura_de_plato,temperatura_maxima,resultado_ignicion,tiempo,observaciones) VALUES ("1","20","120", "60", "si","30","ninguna")')
#cursor.execute('INSERT INTO tmicapa_datos (id_resultados,temperatura,temperatura_de_plato,temperatura_maxima,resultado_ignicion,tiempo,observaciones) VALUES ("2","21","200", "70", "no","20","alguna")')
#cursor.execute('INSERT INTO tmicapa_datos (id_resultados,temperatura,temperatura_de_plato,temperatura_maxima,resultado_ignicion,tiempo,observaciones) VALUES ("3","22","300", "80", "si","30","una")')
#cursor.execute('INSERT INTO tmicapa_datos (id_resultados,temperatura,temperatura_de_plato,temperatura_maxima,resultado_ignicion,tiempo,observaciones) VALUES ("4","23","400", "90", "no","40","niuna")')
#cursor.execute('INSERT INTO ensayos (ensayo, normativa, procedimiento) VALUES ("tmicapa","UNE-EN ISO/IEC 80079-20-2:2016","POENS 551")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("2","2","<500")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("4","2","330")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("2","3","S/V")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("3","3","1")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("4","3","350")') 

#cursor.execute('UPDATE muestras SET id_procedencia = "1" WHERE id = 1')
#cursor.execute('UPDATE muestras SET id_procedencia = "1" WHERE id = 2')
#cursor.execute('UPDATE muestras SET id_procedencia = "2" WHERE id = 3') 


cursor.execute("SELECT id FROM muestras WHERE identificador = 'sad' AND numero = '27'")
busqueda= cursor.fetchone()[0]
cursor.execute("SELECT procedencias.procedencia FROM muestras JOIN procedencias ON muestras.id_procedencia=procedencias.id WHERE muestras.id= '{}'".format(busqueda))
procedenciasad = cursor.fetchone()[0]
print(procedenciasad)


cursor.execute("SELECT id FROM muestras WHERE identificador = 'sad' AND numero = '26'")
busqueda= cursor.fetchone()[0]
cursor.execute("SELECT id FROM ensayos WHERE ensayo = 'tmicapa'")
busqueda2 = cursor.fetchone()[0]
cursor.execute(f"SELECT id FROM resultados WHERE id_muestras = '{busqueda}' AND  id_ensayos = '{busqueda2}'")
busqueda3= cursor.fetchone()[0]
cursor.execute(f"SELECT * FROM tmicapa_datos WHERE id_resultados='{busqueda3}'")
output=cursor.fetchall()
print(output)

#cursor.execute("SELECT resultados.valor FROM muestras JOIN resultados ON muestras.id=resultados.id_muestras WHERE muestras.id=3 AND resultados.id_ensayos=3")
#emi= cursor.fetchone()[0] 
#print(emi)
#cursor.execute("SELECT resultados.valor FROM muestras JOIN resultados ON muestras.id=resultados.id_muestras WHERE muestras.id=1")


#cursor.execute("SELECT * FROM muestras WHERE id='{}'".format(busqueda2))
#todo= cursor.fetchall()
#print(todo)



cursor.close()
mydb.close()

#Sacar la procedencia de sad-27, el valor de emi de urk-1 y todos los ensayos de sad-26, con unidades.