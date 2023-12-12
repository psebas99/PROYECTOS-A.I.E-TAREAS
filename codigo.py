import psycopg2
from tabulate import tabulate
def Historial():
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "1234",
            dbname = "TAREA7"
            )
        cursor = conexion.cursor()
        cursor.execute("SELECT * from codigo;")
        
        # for row in cursor:
        #     print(row)
        print(tabulate(cursor, headers=["No. Producto", "Precio con IVA"], tablefmt="psql", numalign ="center"))
    except:
        print("Error en la conexion \n")

def Post(Numero):
    try:
        conexion = psycopg2.connect(
            host = "localhost",
            port = "5432",
            user = "postgres",
            password = "1234",
            dbname = "TAREA7"
            )
        cursor = conexion.cursor()
        Instruction = "insert into codigo(precio) values('"+str(Numero)+"');"
        cursor.execute(Instruction)
        conexion.commit()
        print("Se ha registrado el precio de su producto.")
    except:
        print("Error en el ingreso de datos o de conexion\n")


def Calculo():

    validez = True

    while validez:
        print("Ingrese el precio del producto")
        Entrada = input("Q")
        try:
            Numero = int(Entrada)
            Precio_total=Numero
            IVA=Numero*0.12
            Precio_sin_IVA = Precio_total-IVA

            print("El precio del producto sin iva es de: Q", str(Precio_sin_IVA)," por lo que su IVA es de: Q", str(IVA))

            validez=False
            break

        except:
            print("Ingrese una numero válida.\n")


    return Numero



opcion = " "

print("Bienvenidos al programa 'Calculadora de IVA'")

while opcion != 'Z':
    print("Seleccione una opción del siguiente menú: \n'A' Calculo \n'B' Ver historial \n'Z' Salir")
    opcion = input("Su elección: ").upper()

    if opcion=='A':
        numero = Calculo()
        Post(numero)
    elif opcion=='B':
        Historial()
    elif opcion=='Z':
        break
    else:
        print("Opcion no válida, ngrese una de las opciones del menú")