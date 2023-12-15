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
            cursor.execute("CREATE TABLE IF NOT EXISTS estudiantes (id SERIAL PRIMARY KEY, nombre VARCHAR(255), edad INT, genero VARCHAR(10), direccion TEXT);")
            conexion.commit()
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def agregar_estudiante(conexion, nombre, edad, genero, direccion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO estudiantes (nombre, edad, genero, direccion) VALUES (%s, %s, %s, %s);", (nombre, edad, genero, direccion))
            conexion.commit()
            print("Estudiante agregado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al agregar estudiante: {e}")

def mostrar_estudiantes(conexion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM estudiantes;")
            estudiantes = cursor.fetchall()
            if estudiantes:
                print("\nLista de Estudiantes:")
                for estudiante in estudiantes:
                    print(f"ID: {estudiante[0]}, Nombre: {estudiante[1]}, Edad: {estudiante[2]}, Género: {estudiante[3]}, Dirección: {estudiante[4]}")
            else:
                print("No hay estudiantes registrados.")
    except Exception as e:
        print(f"Error al obtener la lista de estudiantes: {e}")

def editar_estudiante(conexion, estudiante_id, nombre, edad, genero, direccion):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE estudiantes SET nombre=%s, edad=%s, genero=%s, direccion=%s WHERE id=%s;",
                           (nombre, edad, genero, direccion, estudiante_id))
            conexion.commit()
            print("Información del estudiante actualizada correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al editar estudiante: {e}")

def eliminar_estudiante(conexion, estudiante_id):
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM estudiantes WHERE id=%s;", (estudiante_id,))
            conexion.commit()
            print("Estudiante eliminado correctamente.")
    except Exception as e:
        conexion.rollback()
        print(f"Error al eliminar estudiante: {e}")

def programa():
    # Conectar a la base de datos y crear la tabla si no existe
    conexion = conectar_bd()
    if conexion:
        crear_tabla(conexion)

        while True:
            print("\nPrograma de Gestión de Estudiantes:")
            print("1. Agregar Estudiante")
            print("2. Mostrar Estudiantes")
            print("3. Editar Estudiante")
            print("4. Eliminar Estudiante")
            print("5. Salir")

            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del estudiante: ")
                edad = int(input("Ingrese la edad del estudiante: "))
                genero = input("Ingrese el género del estudiante: ")
                direccion = input("Ingrese la dirección del estudiante: ")
                agregar_estudiante(conexion, nombre, edad, genero, direccion)

            elif opcion == "2":
                mostrar_estudiantes(conexion)

            elif opcion == "3":
                estudiante_id = int(input("Ingrese el ID del estudiante a editar: "))
                nombre = input("Ingrese el nuevo nombre del estudiante: ")
                edad = int(input("Ingrese la nueva edad del estudiante: "))
                genero = input("Ingrese el nuevo género del estudiante: ")
                direccion = input("Ingrese la nueva dirección del estudiante: ")
                editar_estudiante(conexion, estudiante_id, nombre, edad, genero, direccion)

            elif opcion == "4":
                estudiante_id = int(input("Ingrese el ID del estudiante a eliminar: "))
                eliminar_estudiante(conexion, estudiante_id)

            elif opcion == "5":
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        # Cerrar la conexión al salir del programa
        conexion.close()

if __name__ == "__main__":
    programa()
