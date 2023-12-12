pkg load database
conn = conn = pq_connect(setdbopts('codigo', 'examen1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'mapache'));
Instruccion = "select * from tarea7 ;";
precio = input("Ingrese el precio de su producto: Q")

  IVA = precio * 0.12;
  precio_sin_iva= precio - IVA;

  fprintf("El precio del producto sin IVA es de Q%0.0f , por lo que el IVA es de Q%0.0f\n", precio_sin_iva, IVA)

  try
   Ins1 = 'insert into tarea7 (precio) values(';
   Ins2 = ");";
   Instruccion = strcat(Ins1, num2str(precio), Ins2);
   Registro = pq_exec_params(conn, Instruccion);
   Instruccion1 = "select * from tarea7 ;";
   conn = pq_connect(setdbopts('dbname', 'examen1', 'host', 'localhost', 'port', '5432', 'user', 'postgres', 'password', 'mapache'));
   Registro = pq_exec_params(conn, Instruccion1);

    [FilasR ColumnasR] = size(Registro.data);
    Registro.data
     catch e
    disp(['Error durante la conexion a la DB, consulte sobre el error: ' e.message]);
  end
