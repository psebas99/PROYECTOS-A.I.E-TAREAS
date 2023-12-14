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

def guardar_en_bd(conexion, num1, num2, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo2 (n1, n2, r) VALUES (%s, %s, %s);", (num1, num2, resultado))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def mostrar_numeros_de_dos_en_dos(inicio, fin):
    # Asegurarse de que el inicio sea impar si es necesario
    if inicio % 2 == 1:
        inicio += 1

    # Crear lista para almacenar los números de dos en dos
    numeros = list(range(inicio, fin + 1, 2))

    # Mostrar los números de dos en dos
    print("Resultado:", end=" ")
    for i, numero in enumerate(numeros):
        print(numero, end="; " if i < len(numeros) - 1 else "")
    print()  # Imprimir nueva línea al final

    return numeros

# Programa principal
try:
    # Solicitar números de inicio y fin al usuario
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número de fin: "))

    # Validar que el número de inicio sea menor que el número de fin
    if inicio >= fin:
        print("Error: El número de inicio debe ser menor que el número de fin.")
    else:
        # Mostrar los números de dos en dos
        numeros = mostrar_numeros_de_dos_en_dos(inicio, fin)

        # Conectar a la base de datos y guardar resultado
        conexion = conectar_bd()
        if conexion:
            resultado_str = "; ".join(map(str, numeros))
            guardar_en_bd(conexion, numeros[0], numeros[-1], resultado_str)
            conexion.close()

except ValueError:
    print("Error: Ingrese números enteros válidos.")
except Exception as e:
    print(f"Error: {e}")
    # Guardar en archivo salida.txt
    
with open("salida.txt", "w") as archivo:
    archivo.write(resultado_str)
