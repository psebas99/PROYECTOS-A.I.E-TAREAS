import psycopg2

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

def crear_tabla(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS gastos (id SERIAL PRIMARY KEY, concepto VARCHAR(255), monto FLOAT, presupuesto FLOAT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def agregar_gasto(conexion, concepto, monto):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO gastos (concepto, monto, presupuesto) VALUES (%s, %s, %s);", (concepto, monto, 0))
            conexion.commit()
            print("Gasto agregado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar gasto: {e}")

def mostrar_gastos(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM gastos;")
            gastos = cursor.fetchall()
            if gastos:
                print("\nLista de Gastos:")
                for gasto in gastos:
                    print(f"ID: {gasto[0]}, Concepto: {gasto[1]}, Monto: {gasto[2]}, Presupuesto: {gasto[3]}")
            else:
                print("No hay gastos registrados.")
    except Exception as e:
        print(f"Error al obtener la lista de gastos: {e}")

def ajustar_presupuesto(conexion, gasto_id, nuevo_presupuesto):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE gastos SET presupuesto=%s WHERE id=%s;", (nuevo_presupuesto, gasto_id))
            conexion.commit()
            print("Presupuesto ajustado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al ajustar presupuesto: {e}")

def programa():
    # Conectar a la base de datos y crear la tabla si no existe
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)

        while True:
            print("\nPrograma de Seguimiento de Gastos:")
            print("1. Agregar Gasto")
            print("2. Mostrar Gastos")
            print("3. Ajustar Presupuesto")
            print("4. Salir")

            opcion = input("Seleccione una opción (1-4): ")

            if opcion == "1":
                concepto = input("Ingrese el concepto del gasto: ")
                monto = float(input("Ingrese el monto del gasto: "))
                agregar_gasto(conexion, concepto, monto)

            elif opcion == "2":
                mostrar_gastos(conexion)

            elif opcion == "3":
                gasto_id = int(input("Ingrese el ID del gasto a ajustar: "))
                nuevo_presupuesto = float(input("Ingrese el nuevo presupuesto: "))
                ajustar_presupuesto(conexion, gasto_id, nuevo_presupuesto)

            elif opcion == "4":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        # Cerrar la conexión al salir del programa
        conexion.close()

if __name__ == "__main__":
    programa()
