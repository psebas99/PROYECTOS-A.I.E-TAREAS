import psycopg2
from tabulate import tabulate

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            database="PARCIAL1",
            user="postgres",
            password="1234"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tabla_sensores(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS sensores (id SERIAL PRIMARY KEY, nombre VARCHAR(255), valor FLOAT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla de sensores: {e}")

def agregar_sensor(conexion, nombre, valor):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO sensores (nombre, valor) VALUES (%s, %s);", (nombre, valor))
            conexion.commit()
            print("Sensor agregado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar sensor: {e}")

def obtener_lista_sensores(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT DISTINCT nombre FROM sensores;")
            sensores = cursor.fetchall()
            return [sensor[0] for sensor in sensores]
    except Exception as e:
        print(f"Error al obtener la lista de sensores: {e}")
        return []

def obtener_datos_sensor(conexion, nombre_sensor):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM sensores WHERE nombre=%s;", (nombre_sensor,))
            datos_sensor = cursor.fetchall()
            return datos_sensor
    except Exception as e:
        print(f"Error al obtener datos del sensor: {e}")
        return []

def mostrar_tabla_datos(datos_sensor):
    if datos_sensor:
        headers = ["ID", "Nombre", "Valor"]
        print(tabulate(datos_sensor, headers=headers, tablefmt="grid"))
    else:
        print("No hay datos disponibles para este sensor.")

def programa():
    # Conectar a la base de datos y crear la tabla de sensores si no existe
    conexion = conectar_bd()
    if conexion:
        crear_tabla_sensores(conexion)

        while True:
            print("\nPrograma de Análisis de Datos de Sensores:")
            print("1. Agregar Sensor")
            print("2. Seleccionar Sensor y Mostrar Datos")
            print("3. Salir")

            opcion = input("Seleccione una opción (1-3): ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del sensor: ")
                valor = float(input("Ingrese el valor del sensor: "))
                agregar_sensor(conexion, nombre, valor)

            elif opcion == "2":
                lista_sensores = obtener_lista_sensores(conexion)
                if lista_sensores:
                    print("\nSensores Disponibles:")
                    for i, sensor in enumerate(lista_sensores, 1):
                        print(f"{i}. {sensor}")

                    seleccion = int(input("Seleccione el sensor (1-" + str(len(lista_sensores)) + "): "))
                    if 1 <= seleccion <= len(lista_sensores):
                        nombre_sensor_seleccionado = lista_sensores[seleccion - 1]
                        datos_sensor = obtener_datos_sensor(conexion, nombre_sensor_seleccionado)
                        mostrar_tabla_datos(datos_sensor)
                    else:
                        print("Selección no válida. Intente de nuevo.")

                else:
                    print("No hay sensores registrados.")

            elif opcion == "3":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        # Cerrar la conexión al salir del programa
        conexion.close()

if __name__ == "__main__":
    programa()
