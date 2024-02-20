#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi
import hashlib
import mysql.connector

form = cgi.FieldStorage()

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
        print("Error de conexión:", e)
        return None

def cerrar(conexion):
    if conexion:
        conexion.close()

def registrar_usuario(usuario, contrasena):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
            cursor.execute("INSERT INTO usuarios (usuario, contrasena_hash) VALUES (%s, %s)", (usuario, hashed_password))
            conexion.commit()
            print("""
            <html>
            <head>
                <title>Registro Exitoso</title>
            </head>
            <body>
                <h1>Registro Exitoso</h1>
                <p>¡Te has registrado exitosamente!</p>
                <p><a href="index.py">Iniciar Sesión</a></p>
            </body>
            </html>
            """)
        except mysql.connector.Error as e:
            print("""
            <html>
            <head>
                <title>Error de Registro</title>
            </head>
            <body>
                <h1>Error de Registro</h1>
                <p>El nombre de usuario ya está en uso. Por favor, elige otro.</p>
                <p><a href="registro.py">Volver al Registro</a></p>
            </body>
            </html>
            """)
        finally:
            cerrar(conexion)

# Verificar el formulario y realizar la lógica de registro
usuario = form.getvalue('usuario')
contrasena = form.getvalue('contrasena')

if usuario and contrasena:
    registrar_usuario(usuario, contrasena)
else:
    # Mostrar el formulario de registro si no se proporcionaron credenciales
    print("""
    <html>
    <head>
        <title>Ahorcado - Registro</title>
    </head>
    <body>
        <h1>Ahorcado - Registro</h1>
        <form action="registro.py" method="post">
            <label for="usuario">Nombre de Usuario:</label>
            <input type="text" id="usuario" name="usuario" required><br>
            <label for="contrasena">Contraseña:</label>
            <input type="password" id="contrasena" name="contrasena" required><br>
            <input type="submit" value="Registrarse">
        </form>
        <p>¿Ya tienes una cuenta? <a href="index.py">Inicia Sesión</a></p>
    </body>
    </html>
    """)
