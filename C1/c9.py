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
            cursor.execute("CREATE TABLE IF NOT EXISTS codigo9 (id SERIAL PRIMARY KEY, figura TEXT, resultado FLOAT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, figura, resultado):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO codigo9 (figura, resultado) VALUES (%s, %s);", (figura, resultado))
            conexion.commit()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def calcular_area_triangulo():
    try:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = 0.5 * base * altura
        print(f"El área del triángulo es: {area}")
        return area
    except ValueError:
        print("Error: Ingrese un número válido.")
        return None

def mostrar_historial(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT figura, resultado FROM codigo9;")
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
        print("\nCalculadora de Áreas:")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Cuadrado")
        print("4. Rectángulo")
        print("5. Mostrar Historial")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            pass  # Implementar la función para calcular el área del círculo
        elif opcion == '2':
            resultado = calcular_area_triangulo()
            if resultado is not None:
                guardar_en_bd(conexion, "Triángulo", resultado)
        elif opcion == '3':
            pass  # Implementar la función para calcular el área del cuadrado
        elif opcion == '4':
            pass  # Implementar la función para calcular el área del rectángulo
        elif opcion == '5':
            historial = mostrar_historial(conexion)
            if historial:
                print("\nHistorial de Áreas:")
                for registro in historial:
                    print(f"{registro[0]}: {registro[1]}")
            else:
                print("No hay historial disponible.")
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cerrar la conexión al salir del programa
    if conexion:
        conexion.close()
