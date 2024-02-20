#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi
import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123Asd-qwe",  # Cambia esto por tu contraseña
            database="ahorcado"
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error de conexión: {e}")
        return None

def cerrar(conexion):
    if conexion:
        conexion.close()

def obtener_palabras():
    conexion = conectar()
    
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT palabra FROM palabras")
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error al obtener palabras: {e}")
        finally:
            cerrar(conexion)

# Obtener el usuario desde la URL
form = cgi.FieldStorage()
usuario = form.getvalue('usuario')

print("""
<html>
<head>
    <title>Ahorcado - Palabras</title>
</head>
<body>
    <h1>Palabras del Ahorcado</h1>
""")

palabras = obtener_palabras()

if palabras:
    print("<ul>")
    for palabra in palabras:
        print(f"<li>{palabra['palabra']}</li>")
    print("</ul>")
else:
    print("<p>No hay palabras registradas.</p>")

# Mostrar el enlace con el usuario
if usuario:
    print(f"""
    <p><a href="menu.py?usuario={usuario}">Volver al Menú Principal</a></p>
    """)
else:
    print("<p><a href='index.py'>Volver al Menú Principal</a></p>")

print("""
</body>
</html>
""")
