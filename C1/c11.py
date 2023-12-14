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
            cursor.execute("CREATE TABLE IF NOT EXISTS codigo11 (id SERIAL PRIMARY KEY, lado1 INT, lado2 INT, lado3 INT, tipo TEXT, resultado TEXT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, lado1, lado2, lado3, tipo, resultado):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO codigo11 (lado1, lado2, lado3, tipo, resultado) VALUES (%s, %s, %s, %s, %s);", (lado1, lado2, lado3, tipo, resultado))
            conexion.commit()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def determinar_tipo_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

def mostrar_historial(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT lado1, lado2, lado3, tipo, resultado FROM codigo11;")
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
        print("\nPrograma de Tipos de Triángulo:")
        lado1 = int(input("Ingrese el primer lado del triángulo: "))
        lado2 = int(input("Ingrese el segundo lado del triángulo: "))
        lado3 = int(input("Ingrese el tercer lado del triángulo: "))

        tipo = determinar_tipo_triangulo(lado1, lado2, lado3)
        resultado = f"Triángulo {tipo}"

        print(f"Resultado: {resultado}")

        guardar_en_bd(conexion, lado1, lado2, lado3, tipo, resultado)

        mostrar_historial_opcion = input("¿Desea ver el historial? (S/N): ").upper()
        if mostrar_historial_opcion == 'S':
            historial = mostrar_historial(conexion)
            if historial:
                print("\nHistorial de Tipos de Triángulo:")
                for registro in historial:
                    print(f"Lados: {registro[0]}, {registro[1]}, {registro[2]}, Tipo: {registro[3]}, Resultado: {registro[4]}")
            else:
                print("No hay historial disponible.")

        continuar_opcion = input("¿Desea ingresar más triángulos? (S/N): ").upper()
        if continuar_opcion != 'S':
            break

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cerrar la conexión al salir del programa
    if conexion:
        conexion.close()
