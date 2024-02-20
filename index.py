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

def verificar_contrasena(contrasena, contrasena_hash):
    hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
    return hashed_password == contrasena_hash

def iniciar_sesion(usuario, contrasena):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
            usuario_db = cursor.fetchone()
            if usuario_db and verificar_contrasena(contrasena, usuario_db['contrasena_hash']):
                return True
        except mysql.connector.Error as e:
            print("Error al iniciar sesión:", e)
        finally:
            cerrar(conexion)
    return False

def cerrar(conexion):
    if conexion:
        conexion.close()

# Verificar el formulario y realizar la lógica de inicio de sesión
usuario = form.getvalue('usuario')
contrasena = form.getvalue('contrasena')

if usuario and contrasena:
    if iniciar_sesion(usuario, contrasena):
        # Redirigir a la página del menú principal si el inicio de sesión es exitoso
        print(f"""
        <html>
        <head>
            <title>Redireccionando...</title>
            <meta http-equiv="refresh" content="0;url=menu.py?usuario={usuario}">
        </head>
        <body>
            <p>Redireccionando...</p>
        </body>
        </html>
        """)
    else:
        # Mostrar mensaje de error si las credenciales son incorrectas
        print("""
        <html>
        <head>
            <title>Ahorcado - Inicio de Sesión</title>
        </head>
        <body>
            <h1>Error de inicio de sesión. Nombre de usuario o contraseña incorrectos.</h1>
        </body>
        </html>
        """)
else:
    # Mostrar el formulario si no se proporcionaron credenciales
    print("""
    <html>
    <head>
        <title>Ahorcado - Inicio de Sesión</title>
    </head>
    <body>
        <h1>Ahorcado - Inicio de Sesión</h1>
        <form action="index.py" method="post">
            <label for="usuario">Nombre de Usuario:</label>
            <input type="text" id="usuario" name="usuario" required><br>
            <label for="contrasena">Contraseña:</label>
            <input type="password" id="contrasena" name="contrasena" required><br>
            <input type="submit" value="Iniciar Sesión">
        </form>
        <p>¿No tienes una cuenta? <a href="registro.py">Regístrate</a></p>
    </body>
    </html>
    """)
