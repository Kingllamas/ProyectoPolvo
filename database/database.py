import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="polvos"
)


cursor= mydb.cursor()

cursor.execute("DROP TABLE muestras")



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


cursor.execute("SELECT id FROM empresa WHERE empresa = 'sadim'")
pene= cursor.fetchone()[0]


cursor.execute(f'INSERT INTO muestras (identificador, numero, expediente, material, peso, fecha_recepcion, fecha_fin, id_empresa) VALUES ("sad", "27" , "23,658 Q ", "Polvo de lodo", "2", "2022-01-01", "2022-01-10",{pene})')
cursor.close()
mydb.close()
