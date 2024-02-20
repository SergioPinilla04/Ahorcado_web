#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')

if usuario:
    print(f"""
    <html>
    <head>
        <title>Ahorcado - Menú Principal</title>
    </head>
    <body>
        <h1>Bienvenido al Menú Principal, {usuario}!</h1>
        <ul>
            <li><a href="jugar.py?usuario={usuario}">Jugar</a></li>
            <li><a href="cuenta.py?usuario={usuario}">Cuenta</a></li>
            <li><a href="palabras_ahorcado.py?usuario={usuario}">Palabras del Ahorcado</a></li>
            <li><a href="index.py">Salir</a></li>
        </ul>
    </body>
    </html>
    """)
else:
    # Redirigir a la página de inicio de sesión si el usuario no está presente
    print("Location: index.py\n\n")
