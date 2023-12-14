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
        cursor.execute("CREATE TABLE IF NOT EXISTS codigo3 (id SERIAL PRIMARY KEY, n INTEGER, r TEXT);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, numero, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo3 (n, r) VALUES (%s, %s);", (numero, resultado))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def mostrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(str(i))
    return "; ".join(divisores)

try:
    # Solicitar al usuario un número
    numero = int(input("Ingrese un número entero: "))

    # Verificar si el número es positivo
    if numero > 0:
        # Obtener la lista de divisores como cadena
        divisores_str = mostrar_divisores(numero)

        # Mostrar los divisores
        print(f"Los divisores de {numero} son: {divisores_str}")

        # Conectar a la base de datos y guardar en la tabla
        conexion = conectar_bd()
        if conexion:
            crear_tabla(conexion)
            guardar_en_bd(conexion, numero, divisores_str)
            conexion.close()
    else:
        print("Por favor, ingrese un número entero positivo.")
except ValueError:
    print("Error: Ingrese un número entero válido.")

with open("salida.txt", "w") as archivo:
    archivo.write(divisores_str)
