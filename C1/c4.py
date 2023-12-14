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
        cursor.execute("CREATE TABLE IF NOT EXISTS codigo4 (id SERIAL PRIMARY KEY, n1 INTEGER, n2 INTEGER, r TEXT);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, num1, num2, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo4 (n1, n2, r) VALUES (%s, %s, %s);", (num1, num2, resultado))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def obtener_lista_ascendente(num1, num2):
    menor = min(num1, num2)
    mayor = max(num1, num2)
    numeros_ascendentes = list(range(menor, mayor + 1, 2))
    return numeros_ascendentes

try:
    # Solicitar al usuario dos números
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    # Determinar cuál es el mayor
    if num1 == num2:
        print(f"Ambos números son iguales: {num1}")
    else:
        mayor = max(num1, num2)
        print(f"El número mayor es: {mayor}")

        # Obtener la lista de números ascendentes de 2 en 2
        lista_ascendente = obtener_lista_ascendente(num1, num2)

        # Mostrar la lista
        print(f"La lista de números entre {num1} y {num2} de 2 en 2 es: {lista_ascendente}")

        # Conectar a la base de datos y guardar en la tabla
        conexion = conectar_bd()
        if conexion:
            crear_tabla(conexion)
            guardar_en_bd(conexion, num1, num2, str(lista_ascendente))
            conexion.close()

except ValueError:
    print("Error: Ingrese números enteros válidos.")
