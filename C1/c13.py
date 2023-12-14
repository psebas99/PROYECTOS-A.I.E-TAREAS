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
        with conexion.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS codigo13 (id SERIAL PRIMARY KEY, ano_nacimiento INT, es_bisiesto BOOLEAN, resultado TEXT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def es_bisiesto(ano):
    # Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def guardar_en_bd(conexion, ano_nacimiento, es_bisiesto, resultado):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO codigo13 (ano_nacimiento, es_bisiesto, resultado) VALUES (%s, %s, %s);", (ano_nacimiento, es_bisiesto, resultado))
            conexion.commit()
    except Exception as e:
        conexion.rollback()  # Revertir la transacción en caso de error
        print(f"Error al guardar en la base de datos: {e}")

def mostrar_historial(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT ano_nacimiento, es_bisiesto, resultado FROM codigo13;")
            historial = cursor.fetchall()
            return historial
    except Exception as e:
        print(f"Error al obtener el historial: {e}")
        return None

# Conectar a la base de datos y crear la tabla
conexion = conectar_bd()
if conexion:
    crear_tabla(conexion)

try:
    while True:
        print("\nPrograma para verificar si un año es bisiesto:")
        ano_nacimiento = int(input("Ingrese el año de nacimiento (positivo): "))

        if ano_nacimiento <= 0:
            print("Error: Ingrese un año positivo.")
            continue

        es_bisiesto_resultado = es_bisiesto(ano_nacimiento)
        resultado = f"El año {ano_nacimiento} {'es' if es_bisiesto_resultado else 'no es'} bisiesto."

        print(f"Resultado: {resultado}")

        guardar_en_bd(conexion, ano_nacimiento, es_bisiesto_resultado, resultado)

        mostrar_historial_opcion = input("¿Desea ver el historial? (S/N): ").upper()
        if mostrar_historial_opcion == 'S':
            historial = mostrar_historial(conexion)
            if historial:
                print("\nHistorial de Años Bisiestos:")
                for registro in historial:
                    print(f"Año de nacimiento: {registro[0]}, Resultado: {registro[1]}, {registro[2]}")
            else:
                print("No hay historial disponible.")

        continuar_opcion = input("¿Desea ingresar más años? (S/N): ").upper()
        if continuar_opcion != 'S':
            break

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cerrar la conexión al salir del programa
    if conexion:
        conexion.close()

