#!C:/Users/sergio/AppData/Local/Programs/Python/Python310-32/python.exe
print("Content-type: text/html\n\n")

import cgi

form = cgi.FieldStorage()
usuario = form.getvalue('usuario')

print(f"""
<html>
<head>
    <title>Ahorcado - Palabras del Ahorcado</title>
</head>
<body>
    <h1>Palabras del Ahorcado</h1>
    <ul>
        <li><a href="anadir_palabra.py?usuario={usuario}">Añadir una palabra al Ahorcado</a></li>
        <li><a href="borrar_palabra.py?usuario={usuario}">Borrar una palabra del Ahorcado</a></li>
        <li><a href="palabras.py?usuario={usuario}">Lista de palabras</a></li>
        <li><a href="menu.py?usuario={usuario}">Volver al menú</a></li>
    </ul>
</body>
</html>
""")