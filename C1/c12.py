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
            cursor.execute("CREATE TABLE IF NOT EXISTS codigo12 (id SERIAL PRIMARY KEY, numero INT, factorial TEXT, resultado TEXT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def calcular_factorial(numero):
    if numero % 7 == 0:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return str(factorial)
    else:
        raise ValueError("Error: El número no es divisible por 7")

def guardar_en_bd(conexion, numero, factorial, resultado):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO codigo12 (numero, factorial, resultado) VALUES (%s, %s, %s);", (numero, factorial, resultado))
            conexion.commit()
    except Exception as e:
        conexion.rollback()  # Revertir la transacción en caso de error
        print(f"Error al guardar en la base de datos: {e}")

def mostrar_historial(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT numero, factorial, resultado FROM codigo12;")
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
        print("\nPrograma de Factorial (si divisible por 7):")
        numero = int(input("Ingrese un número entero positivo: "))

        try:
            factorial = calcular_factorial(numero)
            resultado = f"Factorial: {factorial}"

            print(f"Resultado: {resultado}")

            guardar_en_bd(conexion, numero, factorial, resultado)

        except ValueError as e:
            print(e)

        mostrar_historial_opcion = input("¿Desea ver el historial? (S/N): ").upper()
        if mostrar_historial_opcion == 'S':
            historial = mostrar_historial(conexion)
            if historial:
                print("\nHistorial de Factoriales:")
                for registro in historial:
                    print(f"Número: {registro[0]}, Resultado: {registro[1]}, {registro[2]}")
            else:
                print("No hay historial disponible.")

        continuar_opcion = input("¿Desea ingresar más números? (S/N): ").upper()
        if continuar_opcion != 'S':
            break

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cerrar la conexión al salir del programa
    if conexion:
        conexion.close()
