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
        cursor.execute("CREATE TABLE IF NOT EXISTS codigo8 (id SERIAL PRIMARY KEY, numero INTEGER);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, numero):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo8 (numero) VALUES (%s);", (numero,))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def mostrar_historial(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT numero FROM codigo8;")
            historial = cursor.fetchall()
            return historial
    except Exception as e:
        print(f"Error al obtener el historial: {e}")
        return None

def numeros_impares_hasta_100():
    impares = [num for num in range(1, 101) if num % 2 != 0]
    cantidad_impares = len(impares)
    return impares, cantidad_impares

try:
    # Calcular los números impares y su cantidad
    impares, cantidad_impares = numeros_impares_hasta_100()

    # Mostrar los números impares
    print("Números impares del 1 al 100:", impares)
    print(f"Total de números impares: {cantidad_impares}")

    # Conectar a la base de datos y guardar en la tabla
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)
        for impar in impares:
            guardar_en_bd(conexion, cantidad_impares)
        conexion.close()

    # Opción de mostrar el historial
    opcion_mostrar_historial = input("¿Desea mostrar el historial? (S/N): ").upper()
    if opcion_mostrar_historial == 'S':
        conexion = conectar_bd()
        historial = mostrar_historial(conexion)
        if historial:
            print("Historial de números impares guardados:")
            for registro in historial:
                print(registro[0])
        conexion.close()

except ValueError:
    print("Error: Ingrese un número entero válido.")
