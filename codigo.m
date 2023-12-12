pkg load database
conn = conn = pq_connect(setdbopts('dbname', 'TAREA7', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', '1234'));
Instruccion = "select * from codigo ;";
precio = input("Ingrese el precio de su producto: Q")

IVA = precio * 0.12;
precio_sin_iva= precio - IVA;

fprintf("El precio del producto sin IVA es de Q%0.0f , por lo que el IVA es de Q%0.0f\n", precio_sin_iva, IVA)

try
   Ins1 = 'insert into codigo (precio) values(';
   Ins2 = ");";
   Instruccion = strcat(Ins1, num2str(precio), Ins2);
   Registro = pq_exec_params(conn, Instruccion);
   Instruccion1 = "select * from codigo ;";
   conn = pq_connect(setdbopts('dbname', 'TAREA7', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', '1234'));
   Registro = pq_exec_params(conn, Instruccion1);

    [FilasR ColumnasR] = size(Registro.data);
    Registro.data
     catch e
    disp(['Error durante la conexion a la DB, consulte sobre el error: ' e.message]);
end
