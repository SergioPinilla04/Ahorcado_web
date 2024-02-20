#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi
import mysql.connector
import random

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')
accion_juego = form.getvalue('accion_juego')
letra = form.getvalue('letra')

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
            cursor = conexion.cursor()
            cursor.execute("SELECT palabra FROM palabras")
            palabras = cursor.fetchall()
            return [palabra[0] for palabra in palabras]
        except mysql.connector.Error as e:
            print(f"Error al obtener palabras: {e}")
        finally:
            cerrar(conexion)

    return []

def usuario_existe(usuario):
    conexion = conectar()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT usuario FROM usuarios WHERE usuario = %s", (usuario,))
            return cursor.fetchone() is not None
        except mysql.connector.Error as e:
            print(f"Error al verificar si el usuario existe: {e}")
        finally:
            cerrar(conexion)

    return False

def obtener_palabra_aleatoria():
    palabras_juego = obtener_palabras()
    if palabras_juego:
        return random.choice(palabras_juego)
    else:
        return None

def obtener_palabra_oculta(palabra, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra])

def registrar_intento(usuario, palabra, fallos):
    if usuario_existe(usuario):
        conexion = conectar()

        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO intentos (usuario, palabra, n_fallos) VALUES (%s, %s, %s)",
                               (usuario, palabra, fallos))
                conexion.commit()
            except mysql.connector.Error as e:
                print(f"Error al registrar intento: {e}")
            finally:
                cerrar(conexion)
    else:
        print(f"El usuario '{usuario}' no existe. No se puede registrar el intento.")

def jugar(usuario, letra, letras_adivinadas):
    palabra = obtener_palabra_aleatoria()
    if not palabra:
        print("No hay palabras disponibles para jugar. Añade palabras desde la opción 'Palabras del ahorcado'.")
        return

    fallos_maximos = 10
    fallos = 0

    palabra_oculta = obtener_palabra_oculta(palabra, letras_adivinadas)

    if letra:
        encontrada = False

        for i in range(len(palabra)):
            if palabra[i] == letra:
                letras_adivinadas.add(letra)
                encontrada = True

        if encontrada:
            print("¡Enhorabuena! La letra", letra, "está en la palabra:", obtener_palabra_oculta(palabra, letras_adivinadas))
        else:
            fallos += 1
            print("¡Fallaste! La letra", letra, "no está en la palabra. Llevas", fallos, "fallos.")

        if '_' not in palabra_oculta:
            print("¡Enhorabuena! Has adivinado la palabra:", obtener_palabra_oculta(palabra, letras_adivinadas))
        elif fallos == fallos_maximos:
            print("Has alcanzado el límite de fallos. La palabra era:", obtener_palabra_oculta(palabra, letras_adivinadas))

        registrar_intento(usuario, palabra, fallos)

        # Agregamos un botón para probar con otra letra
        print(f"""
        <form id="otraLetraForm" action="jugar.py" method="post">
            <input type="hidden" name="usuario" value="{usuario}">
            <input type="hidden" name="accion_juego" value="jugar">
            <input type="text" name="letra" maxlength="1">
            <input type="submit" value="Prueba con otra letra">
        </form>
        """)
        # Imprimimos las letras adivinadas
        print(f"Letras adivinadas: {' '.join(sorted(letras_adivinadas))}")

    else:
        print("""
        <html>
        <head>
            <title>Ahorcado - Jugar</title>
        </head>
        <body>
            <h1>Jugar Ahorcado</h1>
            <p>¡Bienvenido al juego del Ahorcado!</p>
            <p>Intenta adivinar la palabra. Tienes un máximo de 10 fallos permitidos.</p>
            <p>Palabra a adivinar: {' '.join(['_' for _ in palabra])}</p>
            <form id="juegoForm" action="jugar.py" method="post">
                <input type="hidden" name="usuario" value="{usuario}">
                <input type="hidden" name="accion_juego" value="jugar">
                <input type="text" name="letra" maxlength="1">
                <input type="submit" value="Prueba con una letra">
            </form>
            <p><a href="menu.py?usuario={usuario}">Volver al Menú Principal</a></p>
        </body>
        </html>
        """)

letras_adivinadas = set()

if usuario and accion_juego == "jugar":
    jugar(usuario, letra, letras_adivinadas)
else:
    print(f"""
    <html>
    <head>
        <title>Ahorcado - Jugar</title>
    </head>
    <body>
        <h1>Jugar Ahorcado</h1>
        <p>¡Bienvenido al juego del Ahorcado!</p>
        <p>Intenta adivinar la palabra. Tienes un máximo de 10 fallos permitidos.</p>
        <p>Palabra a adivinar: _</p>
        <form id="juegoForm" action="jugar.py" method="post">
            <input type="hidden" name="usuario" value="{usuario}">
            <input type="hidden" name="accion_juego" value="jugar">
            <input type="text" name="letra" maxlength="1">
            <input type="submit" value="Prueba con una letra!">
        </form>
        <p><a href="menu.py?usuario={usuario}">Volver al Menú Principal</a></p>
    </body>
    </html>
    """)
