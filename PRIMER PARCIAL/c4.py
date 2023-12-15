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
            cursor.execute("CREATE TABLE IF NOT EXISTS pedidos (id SERIAL PRIMARY KEY, cliente VARCHAR(255), producto VARCHAR(255), cantidad INT, completado BOOLEAN);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def agregar_pedido(conexion, cliente, producto, cantidad):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO pedidos (cliente, producto, cantidad, completado) VALUES (%s, %s, %s, %s);", (cliente, producto, cantidad, False))
            conexion.commit()
            print("Pedido agregado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar pedido: {e}")

def mostrar_pedidos(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM pedidos;")
            pedidos = cursor.fetchall()
            if pedidos:
                print("\nLista de Pedidos:")
                for pedido in pedidos:
                    print(f"ID: {pedido[0]}, Cliente: {pedido[1]}, Producto: {pedido[2]}, Cantidad: {pedido[3]}, Completado: {pedido[4]}")
            else:
                print("No hay pedidos registrados.")
    except Exception as e:
        print(f"Error al obtener la lista de pedidos: {e}")

def actualizar_pedido(conexion, pedido_id):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE pedidos SET completado=%s WHERE id=%s;", (True, pedido_id))
            conexion.commit()
            print("Estado del pedido actualizado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al actualizar el pedido: {e}")

def eliminar_pedido(conexion, pedido_id):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM pedidos WHERE id=%s;", (pedido_id,))
            conexion.commit()
            print("Pedido eliminado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al eliminar el pedido: {e}")

def programa():
    # Conectar a la base de datos y crear la tabla si no existe
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)

        while True:
            print("\nPrograma de Seguimiento de Pedidos:")
            print("1. Agregar Pedido")
            print("2. Mostrar Pedidos")
            print("3. Actualizar Estado del Pedido")
            print("4. Eliminar Pedido")
            print("5. Salir")

            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "1":
                cliente = input("Ingrese el nombre del cliente: ")
                producto = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                agregar_pedido(conexion, cliente, producto, cantidad)

            elif opcion == "2":
                mostrar_pedidos(conexion)

            elif opcion == "3":
                pedido_id = int(input("Ingrese el ID del pedido a actualizar: "))
                actualizar_pedido(conexion, pedido_id)

            elif opcion == "4":
                pedido_id = int(input("Ingrese el ID del pedido a eliminar: "))
                eliminar_pedido(conexion, pedido_id)

            elif opcion == "5":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        # Cerrar la conexión al salir del programa
        conexion.close()

if __name__ == "__main__":
    programa()
