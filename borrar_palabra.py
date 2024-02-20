#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi
import mysql.connector

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')
palabra_a_borrar = form.getvalue('palabra_a_borrar')

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

def borrar_palabra(usuario, palabra_a_borrar):
    conexion = conectar()

    if conexion:
        try:
            cursor = conexion.cursor()
            # Mensaje de depuración para mostrar la consulta SQL
            cursor.execute("DELETE FROM palabras WHERE palabra = %s AND usuario = %s", (palabra_a_borrar, usuario))
            conexion.commit()
            print("""
            <html>
            <head>
                <title>Ahorcado - Palabra Borrada</title>
            </head>
            <body>
                <h1>Palabra Borrada</h1>
                <p>¡La palabra se ha borrado correctamente!</p>
                <p><a href="palabras_ahorcado.py?usuario={usuario}">Volver a Palabras del Ahorcado</a></p>
            </body>
            </html>
            """)
        except mysql.connector.Error as e:
            # Imprimir descripción detallada del error
            print(f"Error al borrar palabra: {e}")
            print("""
            <html>
            <head>
                <title>Error al Borrar Palabra</title>
            </head>
            <body>
                <h1>Error al Borrar Palabra</h1>
                <p>Ocurrió un error al borrar la palabra. Intenta nuevamente.</p>
                <p><a href="palabras_ahorcado.py?usuario={usuario}">Volver a Palabras del Ahorcado</a></p>
            </body>
            </html>
            """)
        finally:
            cerrar(conexion)

if usuario:
    if palabra_a_borrar:
        borrar_palabra(usuario[0], palabra_a_borrar)  # Solo se pasa el primer elemento de la lista
    print(f"""
    <html>
    <head>
        <title>Ahorcado - Borrar Palabra</title>
    </head>
    <body>
        <h1>Borrar Palabra</h1>
        <form action="" method="post">
            <input type="hidden" name="usuario" value="{usuario}">
            <label for="palabra_a_borrar">Palabra a Borrar:</label>
            <input type="text" id="palabra_a_borrar" name="palabra_a_borrar" required><br>
            <input type="submit" value="Borrar Palabra">
        </form>
        <p><a href="palabras_ahorcado.py?usuario={usuario}">Volver a Palabras del Ahorcado</a></p>
    </body>
    </html>
    """)
else:
    # Redirigir si no se proporcionó un usuario
    print("Location: index.py\n\n")
