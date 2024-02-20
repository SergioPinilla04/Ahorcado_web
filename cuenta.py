#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi
import hashlib
import mysql.connector

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')
nuevo_usuario = form.getvalue('nuevo_usuario')
nueva_contrasena = form.getvalue('nueva_contrasena')
confirmar_cambios = form.getvalue('confirmar_cambios')

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

def verificar_contrasena(contrasena, contrasena_hash):
    hashed_password = hashlib.sha256(contrasena.encode()).hexdigest()
    return hashed_password == contrasena_hash

def obtener_usuario(usuario):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
            return cursor.fetchone()
        except mysql.connector.Error as e:
            print("Error al obtener usuario:", e)
        finally:
            cerrar(conexion)

def editar_cuenta(usuario, nuevo_usuario=None, nueva_contrasena=None):
    conexion = conectar()
    cambios_realizados = False

    if conexion:
        try:
            cursor = conexion.cursor()

            if nuevo_usuario:
                cursor.execute("UPDATE usuarios SET usuario = %s WHERE usuario = %s", (nuevo_usuario, usuario))
                cambios_realizados = True

            if nueva_contrasena:
                hashed_password = hashlib.sha256(nueva_contrasena.encode()).hexdigest()
                cursor.execute("UPDATE usuarios SET contrasena_hash = %s WHERE usuario = %s", (hashed_password, usuario))
                cambios_realizados = True

            if cambios_realizados:
                conexion.commit()

        except mysql.connector.Error as e:
            print("Error al editar cuenta:", e)
        finally:
            cerrar(conexion)

    return cambios_realizados

def borrar_cuenta(usuario):
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE usuario = %s", (usuario,))
            conexion.commit()
            return True
        except mysql.connector.Error as e:
            print("Error al borrar cuenta:", e)
        finally:
            cerrar(conexion)
    return False

if usuario:
    usuario_info = obtener_usuario(usuario)

    if usuario_info:
        if nuevo_usuario or nueva_contrasena:
            if confirmar_cambios == 'si':
                if nuevo_usuario and not nueva_contrasena:
                    editar_cuenta(usuario, nuevo_usuario)
                elif not nuevo_usuario and nueva_contrasena:
                    editar_cuenta(usuario, None, nueva_contrasena)
                elif nuevo_usuario and nueva_contrasena:
                    editar_cuenta(usuario, nuevo_usuario, nueva_contrasena)

                print(f"Location: {'index.py'}\n\n")
            elif confirmar_cambios == 'no':
                print(f"Location: {'menu.py?usuario=' + usuario}\n\n")
            elif confirmar_cambios == 'borrar':
                if borrar_cuenta(usuario):
                    # Después de borrar la cuenta, redirige al índice
                    print(f"Location: {'index.py'}\n\n")
                else:
                    # Si hubo un error al borrar la cuenta, redirige a una página de error o maneja de otra manera
                    print(f"""
                    <html>
                    <head>
                        <title>Ahorcado - Error al Borrar Cuenta</title>
                        <meta http-equiv="refresh" content="2;url=index.py">
                    </head>
                    <body>
                    <h1>Error al Borrar Cuenta</h1>
                        <p>Hubo un error al intentar borrar la cuenta. Por favor, inténtalo de nuevo.</p>
                    </body>
                    </html>
                    """)

            else:
                print(f"""
                <html>
                <head>
                    <title>Ahorcado - Confirmar Cambios</title>
                    <meta http-equiv="refresh" content="2;url=index.py">
                </head>
                <body>
                    <h1>Confirmar Cambios</h1>
                    <p>¿Estás seguro de que quieres realizar los cambios?</p>
                    <form action="cuenta.py" method="post">
                        <input type="hidden" name="usuario" value="{usuario}">
                        <input type="hidden" name="nuevo_usuario" value="{nuevo_usuario}">
                        <input type="hidden" name="nueva_contrasena" value="{nueva_contrasena}">
                        <input type="hidden" name="confirmar_cambios" value="si">
                        <input type="submit" value="Sí">
                    </form>
                    <form action="menu.py" method="get">
                        <input type="hidden" name="usuario" value="{usuario}">
                        <input type="submit" value="No">
                    </form>
                    <form action="cuenta.py" method="post">
                        <input type="hidden" name="usuario" value="{usuario}">
                        <input type="hidden" name="confirmar_cambios" value="borrar">
                        <input type="submit" value="Borrar Cuenta">
                    </form>
                </body>
                </html>
                """)
        else:
            if confirmar_cambios == 'si':
                borrar_cuenta(usuario)
                print(f"Location: {'index.py'}\n\n")
            elif confirmar_cambios == 'no':
                print(f"Location: {'menu.py?usuario=' + usuario}\n\n")
            else:
                print(f"""
                <html>
                <head>
                    <title>Ahorcado - Cuenta</title>
                </head>
                <body>
                    <h1>Editar Cuenta</h1>
                    <form action="cuenta.py" method="post">
                        <input type="hidden" name="usuario" value="{usuario}">
                        <label for="nuevo_usuario">Nuevo Nombre de Usuario:</label>
                        <input type="text" id="nuevo_usuario" name="nuevo_usuario" value="{usuario_info['usuario']}"><br>
                        <label for="nueva_contrasena">Nueva Contraseña:</label>
                        <input type="password" id="nueva_contrasena" name="nueva_contrasena"><br>
                        <input type="submit" value="Guardar Cambios">
                    </form>
                    <form action="menu.py" method="get">
                        <input type="hidden" name="usuario" value="{usuario}">
                        <input type="submit" value="Volver al Menú Principal">
                    </form>
                    <form action="cuenta.py" method="post">
                        <input type="hidden" name="usuario" value="{usuario}">
                        <input type="hidden" name="confirmar_cambios" value="borrar">
                        <input type="submit" value="Borrar Cuenta">
                    </form>
                </body>
                </html>
                """)
    else:
        print("Location: index.py\n\n")
else:
    print("Location: index.py\n\n")
