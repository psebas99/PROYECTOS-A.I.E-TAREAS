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
            cursor.execute("CREATE TABLE IF NOT EXISTS inventario (id SERIAL PRIMARY KEY, nombre VARCHAR(255), cantidad INT, precio FLOAT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def agregar_producto(conexion, nombre, cantidad, precio):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO inventario (nombre, cantidad, precio) VALUES (%s, %s, %s);", (nombre, cantidad, precio))
            conexion.commit()
            print("Producto agregado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar producto: {e}")

def mostrar_inventario(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM inventario;")
            inventario = cursor.fetchall()
            if inventario:
                print("\nInventario:")
                for producto in inventario:
                    print(f"ID: {producto[0]}, Nombre: {producto[1]}, Cantidad: {producto[2]}, Precio: {producto[3]}")
            else:
                print("El inventario está vacío.")
    except Exception as e:
        print(f"Error al obtener el inventario: {e}")

def actualizar_producto(conexion, producto_id, nueva_cantidad, nuevo_precio):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE inventario SET cantidad=%s, precio=%s WHERE id=%s;", (nueva_cantidad, nuevo_precio, producto_id))
            conexion.commit()
            print("Información del producto actualizada correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al actualizar producto: {e}")

def eliminar_producto(conexion, producto_id):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM inventario WHERE id=%s;", (producto_id,))
            conexion.commit()
            print("Producto eliminado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al eliminar producto: {e}")

def programa():
    # Conectar a la base de datos y crear la tabla si no existe
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)

        while True:
            print("\nPrograma de Gestión de Inventario:")
            print("1. Agregar Producto")
            print("2. Mostrar Inventario")
            print("3. Actualizar Producto")
            print("4. Eliminar Producto")
            print("5. Salir")

            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                agregar_producto(conexion, nombre, cantidad, precio)

            elif opcion == "2":
                mostrar_inventario(conexion)

            elif opcion == "3":
                producto_id = int(input("Ingrese el ID del producto a actualizar: "))
                nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                actualizar_producto(conexion, producto_id, nueva_cantidad, nuevo_precio)

            elif opcion == "4":
                producto_id = int(input("Ingrese el ID del producto a eliminar: "))
                eliminar_producto(conexion, producto_id)

            elif opcion == "5":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        # Cerrar la conexión al salir del programa
        conexion.close()

if __name__ == "__main__":
    programa()
