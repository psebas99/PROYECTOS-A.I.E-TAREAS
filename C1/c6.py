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
        cursor.execute("CREATE TABLE IF NOT EXISTS codigo6 (id SERIAL PRIMARY KEY, palabra TEXT, a INTEGER, e INTEGER, i INTEGER, o INTEGER, u INTEGER);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, palabra, ocurrencias_vocales):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo6 (palabra, a, e, i, o, u) VALUES (%s, %s, %s, %s, %s, %s);",
                       (palabra, ocurrencias_vocales['a'], ocurrencias_vocales['e'], ocurrencias_vocales['i'],
                        ocurrencias_vocales['o'], ocurrencias_vocales['u']))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for letra in palabra:
        if letra in vocales:
            contador_vocales[letra.lower()] += 1
    return contador_vocales

try:
    # Solicitar al usuario una palabra
    palabra = input("Ingrese una palabra: ")

    # Contar las ocurrencias de cada vocal en la palabra
    ocurrencias_vocales = contar_vocales(palabra)

    # Mostrar el resultado
    print("Resultado:")
    for vocal, cantidad in ocurrencias_vocales.items():
        print(f"{vocal.upper()}={cantidad}")

    # Conectar a la base de datos y guardar en la tabla
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)
        guardar_en_bd(conexion, palabra, ocurrencias_vocales)
        conexion.close()

except ValueError:
    print("Error: Ingrese una palabra válida.")
