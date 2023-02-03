import mysql.connector

con_bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ContraseñaSegura123+",
    database = "movies"
)

cursor_bd = con_bd.cursor()

cursor_bd.execute('SELECT * FROM tb_movie')

resultado = cursor_bd.fetchall()

print (resultado)

for x in resultado:
  print(x)