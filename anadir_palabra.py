#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi
import mysql.connector

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')
nueva_palabra = form.getvalue('nueva_palabra')

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

def agregar_palabra(usuario, nueva_palabra):
    conexion = conectar()

    if conexion:
        try:
            cursor = conexion.cursor()
            usuario_str = str(usuario)  # Convertir a cadena
            cursor.execute("INSERT INTO palabras (palabra, usuario) VALUES (%s, %s)", (nueva_palabra, usuario_str))
            conexion.commit()
            print("""
            <html>
            <head>
                <title>Ahorcado - Palabra Agregada</title>
            </head>
            <body>
                <h1>Palabra Agregada</h1>
                <p>¡La palabra se ha añadido correctamente!</p>
            </body>
            </html>
            """.format(usuario=usuario_str))
        except mysql.connector.Error as e:
            # Imprimir descripción detallada del error
            print(f"Error al agregar palabra: {e}")
            print("""
            <html>
            <head>
                <title>Error al Agregar Palabra</title>
            </head>
            <body>
                <h1>Error al Agregar Palabra</h1>
                <p>Ocurrió un error al agregar la palabra. Intenta nuevamente.</p>
                <p><a href="palabras_ahorcado.py?usuario={usuario}">Volver a Palabras del Ahorcado</a></p>
            </body>
            </html>
            """.format(usuario=usuario_str))
        finally:
            cerrar(conexion)

if usuario:
    if nueva_palabra:
        agregar_palabra(usuario[0], nueva_palabra)  # Solo se pasa el primer elemento de la lista
    print(f"""
    <html>
    <head>
        <title>Ahorcado - Añadir Palabra</title>
    </head>
    <body>
        <h1>Añadir Palabra</h1>
        <form action="" method="post">
            <input type="hidden" name="usuario" value="{usuario}">
            <label for="nueva_palabra">Nueva Palabra:</label>
            <input type="text" id="nueva_palabra" name="nueva_palabra" required><br>
            <input type="submit" value="Agregar Palabra">
        </form>
        <p><a href="palabras_ahorcado.py?usuario={usuario}">Volver a Palabras del Ahorcado</a></p>
    </body>
    </html>
    """)
else:
    # Redirigir si no se proporcionó un usuario
    print("Location: index.py\n\n")
