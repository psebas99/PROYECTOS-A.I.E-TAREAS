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

def guardar_en_bd(conexion, num1, num2, num3, resultado):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO codigo1(N1, N2, N3, R) VALUES (%s, %s, %s, %s);", (num1, num2, num3, resultado))
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al guardar en la base de datos: {e}")

def programa():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        num3 = float(input("Ingrese el tercer número:"))

        if num1 == num2 == num3:
            print("Todos son iguales!")
            resultado = f"Todos son iguales: {num1}, {num2}, {num3}"
        else:
            mayor = max(num1, num2, num3)
            if mayor == num1:
                resultado = f"La suma de los tres números es: {num1 + num2 + num3}"
            elif mayor == num2:
                resultado = f"La multiplicación de los tres números es: {num1 * num2 * num3}"
            else:
                resultado = f"La concatenación de los tres números es: {num1}{num2}{num3}"

            print(resultado)

        # Guardar en archivo salida.txt
        with open("salida.txt", "w") as archivo:
            archivo.write(resultado)

        # Conectar a la base de datos y guardar resultado
        conexion = conectar_bd()
        if conexion:
            guardar_en_bd(conexion, num1, num2, num3, resultado)
            conexion.close()

    except ValueError:
        print("Error: Ingrese solo números válidos.")

if __name__ == "__main__":
    programa()
