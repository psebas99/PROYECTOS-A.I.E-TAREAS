import psycopg2

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            database="CORTO1",
            user="postgres",
            password="1234"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tabla(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS codigo5 (id SERIAL PRIMARY KEY, palabra TEXT, r INTEGER);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, palabra, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo5 (palabra, r) VALUES (%s, %s);", (palabra, resultado))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador_vocales = 0
    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
    return contador_vocales

try:
    # Solicitar al usuario una palabra
    palabra = input("Ingrese una palabra: ")

    # Contar las vocales en la palabra
    cantidad_vocales = contar_vocales(palabra)

    # Mostrar el resultado
    print(f"La palabra '{palabra}' tiene {cantidad_vocales} vocales.")

    # Conectar a la base de datos y guardar en la tabla
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)
        guardar_en_bd(conexion, palabra, cantidad_vocales)
        conexion.close()

except ValueError:
    print("Error: Ingrese una palabra válida.")
