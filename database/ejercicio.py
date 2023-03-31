import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)


cursor= mydb.cursor()

#cursor.execute("DROP TABLE muestras")



cursor.execute('''CREATE TABLE IF NOT EXISTS procedencias (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               procedencia VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS empresa (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               empresa VARCHAR(50))''')
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
               id_empresa INT,
               FOREIGN KEY(id_empresa) REFERENCES empresa(id))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS ensayos (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               ensayos VARCHAR(50),
               unidad VARCHAR(50))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS resultados (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               id_ensayos VARCHAR(50),
               FOREIGN KEY(id_ensayos) REFERENCES ensayos(id),
               id_muestras VARCHAR(50),
               FOREIGN KEY(id_muestras) REFERENCES muestras(id),
               valor VARCHAR(50))''')




#cursor.execute('INSERT INTO empresa (empresa) VALUES ("urike")')
#cursor.execute("SELECT id FROM empresa WHERE empresa = 'urike'")
#pene= cursor.fetchone()[0]
#cursor.execute(f'INSERT INTO muestras (identificador, numero, expediente, material, peso, fecha_recepcion, id_empresa) VALUES ("URK", "1" , "23,141 Q ", "granalla", "3", "2022-03-21", {pene})')

#cursor.execute('INSERT INTO procedencias (procedencia) VALUES ("barcelona")')
#cursor.execute('INSERT INTO procedencias (procedencia) VALUES ("galicia")')
#cursor.execute('INSERT INTO ensayos (ensayos,unidad) VALUES ("humedad","%")')
#cursor.execute('INSERT INTO ensayos (ensayos,unidad) VALUES ("granulometría","micra")')
#cursor.execute('INSERT INTO ensayos (ensayos,unidad) VALUES ("emi","j")')
#cursor.execute('INSERT INTO ensayos (ensayos,unidad) VALUES ("tmic","k")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("1","1","2")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("2","1","S/V")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("3","1","25")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("4","1","340")')
#cursor.execute('INSERT INTO resultados (id_ensayos, id_muestras, valor) VALUES ("1","2","0.5")')
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


cursor.execute("SELECT id FROM muestras WHERE identificador = 'sad' AND numero = '27'")
busqueda= cursor.fetchone()[0]
cursor.execute("SELECT resultados.valor FROM muestras JOIN resultados ON muestras.id=resultados.id_muestras WHERE muestras.id=3 AND resultados.id_ensayos=3")
emi= cursor.fetchone()[0] 
print(emi)
#cursor.execute("SELECT resultados.valor FROM muestras JOIN resultados ON muestras.id=resultados.id_muestras WHERE muestras.id=1")
cursor.execute("SELECT id FROM muestras WHERE identificador = 'sad' AND numero = '27'")
busqueda2 = cursor.fetchone()[0]
cursor.execute("SELECT * FROM muestras WHERE id='{}'".format(busqueda2))
todo= cursor.fetchall()
print(todo)



cursor.close()
mydb.close()

#Sacar la procedencia de sad-27, el valor de emi de urk-1 y todos los ensayos de sad-26, con unidades.