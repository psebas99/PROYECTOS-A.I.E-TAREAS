import psycopg2
from tabulate import tabulate

def conectar_bd():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            port=5432,
            database="PARCIAL1",
            user="tu_usuario",
            password="tu_contraseña"
        )
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tabla(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS inventario (producto TEXT PRIMARY KEY, cantidad INTEGER, precio_unitario FLOAT);")
        conexion.commit()
        cursor.close()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def agregar_producto(conexion, producto, cantidad, precio_unitario):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO inventario (producto, cantidad, precio_unitario) VALUES (%s, %s, %s) ON CONFLICT (producto) DO UPDATE SET cantidad = inventario.cantidad + EXCLUDED.cantidad;", (producto, cantidad, precio_unitario))
        conexion.commit()
        cursor.close()
        print("Producto agregado al inventario.")
    except Exception as e:
        print(f"Error al agregar producto: {e}")

def actualizar_inventario(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario;")
        inventario = cursor.fetchall()

        print(tabulate(inventario, headers=["Producto", "Cantidad", "Precio Unitario"], tablefmt="psql", numalign="center"))

        producto = input("Ingrese el nombre del producto que desea actualizar: ")
        cantidad = int(input("Ingrese la nueva cantidad: "))

        cursor.execute("UPDATE inventario SET cantidad = %s WHERE producto = %s;", (cantidad, producto))
        conexion.commit()
        cursor.close()

        print("Inventario actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar inventario: {e}")

def generar_informe_ventas(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM inventario;")
        inventario = cursor.fetchall()

        print(tabulate(inventario, headers=["Producto", "Cantidad", "Precio Unitario"], tablefmt="psql", numalign="center"))
    except Exception as e:
        print(f"Error al generar informe de ventas: {e}")

if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)

        while True:
            print("\nMenú de Inventario:")
            print("1. Agregar Producto")
            print("2. Actualizar Inventario")
            print("3. Generar Informe de Ventas")
            print("4. Salir")

            opcion = input("Seleccione una opción (1-4): ")

            if opcion == '1':
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio_unitario = float(input("Ingrese el precio unitario: "))
                agregar_producto(conexion, producto, cantidad, precio_unitario)
            elif opcion == '2':
                actualizar_inventario(conexion)
            elif opcion == '3':
                generar_informe_ventas(conexion)
            elif opcion == '4':
                break
            else:
                print("Opción no válida. Intente de nuevo.")

        conexion.close()
