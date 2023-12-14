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
        cursor.execute("CREATE TABLE IF NOT EXISTS codigo7 (id SERIAL PRIMARY KEY, n1 INTEGER, r INTEGER);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, numero, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo7 (n1, r) VALUES (%s, %s);", (numero, resultado))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def suma_hasta_numero(numero):
    if numero < 1:
        return "Por favor, ingrese un número entero positivo."

    suma = sum(range(1, numero + 1))
    return suma

try:
    # Solicitar al usuario un número
    numero = int(input("Ingrese un número entero: "))

    # Calcular la suma
    resultado = suma_hasta_numero(numero)

    # Mostrar el resultado
    print(f"Resultado: {resultado}")

    # Conectar a la base de datos y guardar en la tabla
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)
        guardar_en_bd(conexion, numero, resultado)
        conexion.close()

except ValueError:
    print("Error: Ingrese un número entero válido.")
