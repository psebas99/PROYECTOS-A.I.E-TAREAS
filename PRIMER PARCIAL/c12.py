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

def menu_principal():
    print("Menú Principal:")
    print("1. Jugar")
    print("2. Instrucciones")
    print("3. Ver preguntas")
    print("4. Salir")

def mostrar_preguntas(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT pregunta FROM preguntas;")
        preguntas = cursor.fetchall()
        cursor.close()

        print("Preguntas disponibles:")
        for pregunta in preguntas:
            print(pregunta[0])

    except Exception as e:
        print(f"Error al obtener las preguntas: {e}")

def jugar(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT pregunta, respuesta FROM preguntas;")
        preguntas = cursor.fetchall()
        cursor.close()

        vidas = 3
        puntaje = 0

        for pregunta, respuesta in preguntas:
            print(f"\nVidas: {vidas} | Puntaje actual: {puntaje}")
            print(f"Pregunta: {pregunta}")
            respuesta_usuario = input("Tu respuesta: ")

            if respuesta_usuario.lower() == respuesta.lower():
                print("¡Respuesta correcta! Ganaste 1 punto.")
                puntaje += 1
            else:
                print("Respuesta incorrecta. Pierdes una vida.")
                vidas -= 1

            if vidas == 0:
                print("¡Tus vidas se agotaron! Juego terminado.")
                break

        print("\n--- Juego terminado ---")
        print(f"Puntaje final: {puntaje}")

    except Exception as e:
        print(f"Error al jugar: {e}")

def main():
    conexion = conectar_bd()

    if conexion:
        while True:
            menu_principal()
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                jugar(conexion)
            elif opcion == "2":
                print("Instrucciones: Responde correctamente las preguntas para ganar puntos y conservar vidas.")
            elif opcion == "3":
                mostrar_preguntas(conexion)
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

        conexion.close()

if __name__ == "__main__":
    main()
