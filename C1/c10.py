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
            cursor.execute("CREATE TABLE IF NOT EXISTS codigo10 (id SERIAL PRIMARY KEY, nota1 INT, nota2 INT, nota3 INT, promedio FLOAT, resultado TEXT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def guardar_en_bd(conexion, nota1, nota2, nota3, promedio, resultado):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO codigo10 (nota1, nota2, nota3, promedio, resultado) VALUES (%s, %s, %s, %s, %s);", (nota1, nota2, nota3, promedio, resultado))
            conexion.commit()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def calcular_promedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

def determinar_estado(promedio):
    if promedio >= 60:
        return "APROBADO"
    else:
        return "REPROBADO"

def mostrar_historial(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT nota1, nota2, nota3, promedio, resultado FROM codigo10;")
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
        print("\nPrograma de Notas:")
        nota1 = int(input("Ingrese la primera nota: "))
        nota2 = int(input("Ingrese la segunda nota: "))
        nota3 = int(input("Ingrese la tercera nota: "))

        promedio = calcular_promedio(nota1, nota2, nota3)
        resultado = determinar_estado(promedio)

        print(f"Promedio: {promedio}")
        print(f"Resultado: {resultado}")

        guardar_en_bd(conexion, nota1, nota2, nota3, promedio, resultado)

        mostrar_historial_opcion = input("¿Desea ver el historial? (S/N): ").upper()
        if mostrar_historial_opcion == 'S':
            historial = mostrar_historial(conexion)
            if historial:
                print("\nHistorial de Notas:")
                for registro in historial:
                    print(f"Notas: {registro[0]}, {registro[1]}, {registro[2]}, Promedio: {registro[3]}, Resultado: {registro[4]}")
            else:
                print("No hay historial disponible.")

        continuar_opcion = input("¿Desea ingresar más notas? (S/N): ").upper()
        if continuar_opcion != 'S':
            break

except Exception as e:
    print(f"Error inesperado: {e}")

finally:
    # Cerrar la conexión al salir del programa
    if conexion:
        conexion.close()
