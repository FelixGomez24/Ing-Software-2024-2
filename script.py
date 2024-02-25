import pymysql
import random
from datetime import datetime, timedelta

# Función para establecer la conexión con la base de datos
def establecer_conexion():
    return pymysql.connect(host='localhost',
                           user='lab',
                           password='Developer123!',
                           database='lab_ing_software',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

# Función para insertar un nuevo usuario
def insertar_usuario():
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)"
            num_aleatorio = random.randint(0, 1000)
            usuario = f'Usuario{num_aleatorio}'
            num_aleatorio = random.randint(0, 1000)
            apPat = f'ApellidoP{num_aleatorio}'
            num_aleatorio = random.randint(0, 1000)
            apMat = f'ApellidoM{num_aleatorio}'
            num_aleatorio = random.randint(0, 1000)
            contrasenia = f'contrasenia{num_aleatorio}'
            correo = f'{usuario}@correo.com'
            cursor.execute(sql, (usuario, apPat, apMat, contrasenia, correo, 0))
            conexion.commit()
            print(f"Usuario insertado: {usuario} {apPat} {apMat}")
    finally:
        conexion.close()

# Función para insertar una nueva película
def insertar_pelicula():
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            num_aleatorio = random.randint(0, 1000)
            nombre_pelicula = f'Pelicula{num_aleatorio}'
            cursor.execute(sql, (nombre_pelicula, 'Accion', 160, 1))
            conexion.commit()
            print(f"Pelicula insertada: {nombre_pelicula}")
    finally:
        conexion.close()

# Función para insertar una nueva renta
def insertar_renta():
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idUsuario FROM usuarios ORDER BY RAND() LIMIT 1")
            id_usuario = cursor.fetchone()['idUsuario']
            cursor.execute("SELECT idPelicula FROM peliculas ORDER BY RAND() LIMIT 1")
            id_pelicula = cursor.fetchone()['idPelicula']
            fecha_renta = datetime.now() - timedelta(days=random.randint(1, 10))
            dias_de_renta = random.randint(1, 5)
            estatus = random.randint(0, 1)
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus))
            conexion.commit()
            print(f"Renta insertada del usuario con id: {id_usuario} y pelicula con id: {id_pelicula}")
    finally:
        conexion.close()

# Función para insertar al menos un registro en cada tabla
def insertar_registros_en_todas_las_tablas():
    """
    Inserta al menos un registro en cada tabla de la base de datos.
    """
    insertar_usuario()
    insertar_pelicula()
    insertar_renta()

# Función para filtrar usuarios por la terminación de su apellido
def filtrar_usuarios_apellido(apellido_terminacion):
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
            patron = f'%{apellido_terminacion}'
            cursor.execute(sql, (patron, patron))
            resultado = cursor.fetchall()
            if not resultado:
                print("No se encontraron usuarios")
            for usuario in resultado:
                print(usuario)
    finally:
        conexion.close()

# Función para cambiar el género de una película
def cambiar_genero_pelicula(pelicula, genero):
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            sql_buscar_pelicula = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql_buscar_pelicula, (pelicula,))
            pelicula_cambiar = cursor.fetchone()
            if pelicula_cambiar:
                sql_cambiar_genero = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql_cambiar_genero, (genero, pelicula))
                conexion.commit()
                print("Genero cambiado con éxito!")
            else:
                print("Pelicula no encontrada!")
    finally:
        conexion.close()

# Función para eliminar las rentas antiguas
def eliminar_rentas_antiguas():
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            fecha_limite = datetime.now() - timedelta(days=3)
            sql_eliminar_rentas = "DELETE FROM rentar WHERE fecha_renta < %s"
            cursor.execute(sql_eliminar_rentas, (fecha_limite,))
            conexion.commit()
            eliminadas = cursor.rowcount
            print(f"Rentas eliminadas: {eliminadas}")
    finally:
        conexion.close()

# Función para eliminar todos los registros de todas las tablas
def eliminar_registros_todas_las_tablas():
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM rentar")
            cursor.execute("DELETE FROM usuarios")
            cursor.execute("DELETE FROM peliculas")
            conexion.commit()
            print("Todos los registros de todas las tablas han sido eliminados")
    finally:
        conexion.close()

# Función principal que muestra el menú y maneja las opciones del usuario
def main():
    while True:
        print("\nMenú:")
        print("1. Insertar registros en todas las tablas")
        print("2. Filtrar usuarios por apellido")
        print("3. Cambiar género de película")
        print("4. Eliminar rentas antiguas")
        print("5. Eliminar todos los registros de todas las tablas")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            insertar_registros_en_todas_las_tablas()
        elif opcion == "2":
            apellido = input("Ingrese la terminación del apellido a buscar: ")
            filtrar_usuarios_apellido(apellido)
        elif opcion == "3":
            pelicula = input("Ingrese el nombre de la película: ")
            genero = input("Ingrese el nuevo género: ")
            cambiar_genero_pelicula(pelicula, genero)
        elif opcion == "4":
            eliminar_rentas_antiguas()
        elif opcion == "5":
            eliminar_registros_todas_las_tablas()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Llama a la función principal
if __name__ == "__main__":
    main()
