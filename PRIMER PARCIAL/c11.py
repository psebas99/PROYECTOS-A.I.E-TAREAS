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

def desplegar_listado(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM canciones;")
        result = cursor.fetchall()

        print('Listado de canciones:')
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error al desplegar listado de canciones: {e}")

def buscar_por_artista(conexion):
    try:
        cursor = conexion.cursor()
        artista = input('Ingrese el nombre del artista: ')
        query = f"SELECT * FROM canciones WHERE artista = '{artista}';"
        cursor.execute(query)
        result = cursor.fetchall()

        print(f'Canciones del artista {artista}:')
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error al buscar por artista: {e}")

def buscar_por_cancion(conexion):
    try:
        cursor = conexion.cursor()
        cancion = input('Ingrese el nombre de la canción: ')
        query = f"SELECT * FROM canciones WHERE cancion = '{cancion}';"
        cursor.execute(query)
        result = cursor.fetchall()

        print(f'Información de la canción {cancion}:')
        for row in result:
            print(row)
    except Exception as e:
        print(f"Error al buscar por canción: {e}")

def agregar_cancion(conexion):
    try:
        cursor = conexion.cursor()
        artista = input('Ingrese el nombre del artista: ')
        cancion = input('Ingrese el nombre de la canción: ')
        letra = input('Ingrese la letra de la canción: ')

        query = f"INSERT INTO canciones (artista, cancion, letra) VALUES ('{artista}', '{cancion}', '{letra}');"
        cursor.execute(query)
        conexion.commit()

        print('Canción agregada correctamente.')
    except Exception as e:
        print(f"Error al agregar canción: {e}")

if __name__ == "__main__":
    conexion = conectar_bd()

    if conexion:
        opcion = 0

        while opcion != 5:
            print("Seleccione una opción:")
            print("1. Desplegar listado de canciones")
            print("2. Buscar por artista")
            print("3. Buscar por canción")
            print("4. Agregar canción")
            print("5. Salir")

            try:
                opcion = int(input("Ingrese su elección: "))

                if opcion == 1:
                    desplegar_listado(conexion)
                elif opcion == 2:
                    buscar_por_artista(conexion)
                elif opcion == 3:
                    buscar_por_cancion(conexion)
                elif opcion == 4:
                    agregar_cancion(conexion)
                elif opcion == 5:
                    print("Saliendo del programa")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Ingrese un número válido.")

        conexion.close()
    else:
        print("No se pudo conectar a la base de datos.")
