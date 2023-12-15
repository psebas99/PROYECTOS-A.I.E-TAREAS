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
            cursor.execute("CREATE TABLE IF NOT EXISTS ventas (id SERIAL PRIMARY KEY, producto VARCHAR(255), cantidad INT, monto FLOAT, fecha DATE);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def agregar_venta(conexion, producto, cantidad, monto, fecha):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO ventas (producto, cantidad, monto, fecha) VALUES (%s, %s, %s, %s);", (producto, cantidad, monto, fecha))
            conexion.commit()
            print("Venta registrada correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar venta: {e}")

def generar_informe(conexion, fecha_inicio, fecha_fin):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM ventas WHERE fecha BETWEEN %s AND %s;", (fecha_inicio, fecha_fin))
            ventas = cursor.fetchall()
            if ventas:
                print("\nInforme de Ventas:")
                for venta in ventas:
                    print(f"ID: {venta[0]}, Producto: {venta[1]}, Cantidad: {venta[2]}, Monto: {venta[3]}, Fecha: {venta[4]}")
            else:
                print("No hay ventas registradas en el período seleccionado.")
    except Exception as e:
        print(f"Error al generar informe: {e}")

def programa():
    # Conectar a la base de datos y crear la tabla si no existe
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)

        while True:
            print("\nPrograma de Monitoreo de Ventas:")
            print("1. Agregar Venta")
            print("2. Generar Informe de Ventas")
            print("3. Salir")

            opcion = input("Seleccione una opción (1-3): ")

            if opcion == "1":
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad vendida: "))
                monto = float(input("Ingrese el monto de la venta: "))
                fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")
                agregar_venta(conexion, producto, cantidad, monto, fecha)

            elif opcion == "2":
                fecha_inicio = input("Ingrese la fecha de inicio para el informe (YYYY-MM-DD): ")
                fecha_fin = input("Ingrese la fecha de fin para el informe (YYYY-MM-DD): ")
                generar_informe(conexion, fecha_inicio, fecha_fin)

            elif opcion == "3":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        # Cerrar la conexión al salir del programa
        conexion.close()

if __name__ == "__main__":
    programa()
