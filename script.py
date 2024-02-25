import pymysql
import random
from datetime import datetime, timedelta

def establecer_conexion():
    """
    Establece una conexión con la base de datos y devuelve el objeto de conexión.
    """
    return pymysql.connect(host='localhost',
                           user='lab',
                           password='Developer123!',
                           database='lab_ing_software',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

def insertar_usuario():
    """
    Inserta un nuevo usuario en la base de datos con datos aleatorios.
    """
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            # Generar datos aleatorios para el nuevo usuario
            sql = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)"
            num_aleatorio = random.randint(0, 100)
            usuario = f'User{num_aleatorio}'
            num_aleatorio = random.randint(0, 100)
            apPat = f'LastName1{num_aleatorio}'
            num_aleatorio = random.randint(0, 100)
            apMat = f'LastName2{num_aleatorio}'
            num_aleatorio = random.randint(0, 100)
            contrasenia = f'password{num_aleatorio}'
            correo = f'{usuario}@example.com'
            # Ejecutar la consulta SQL para insertar el nuevo usuario
            cursor.execute(sql, (usuario, apPat, apMat, contrasenia, correo, 0))
            conexion.commit()
            print(f"Usuario insertado: {usuario} {apPat} {apMat}")
    finally:
        conexion.close()

def insertar_pelicula():
    """
    Inserta una nueva película en la base de datos con datos aleatorios.
    """
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            # Lista de géneros de películas
            generos = ['Acción', 'Drama', 'Comedia', 'Ciencia Ficción', 'Romance', 'Suspenso', 'Animación']
            # Elegir un género aleatorio
            genero = random.choice(generos)
            # Duración aleatoria entre 60 y 180 minutos
            duracion = random.randint(60, 180)
            # Consulta SQL para insertar la nueva película
            sql = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            num_aleatorio = random.randint(0, 1000)
            nombre_pelicula = f'Movie{num_aleatorio}'
            # Ejecutar la consulta SQL
            cursor.execute(sql, (nombre_pelicula, genero, duracion, 1))
            conexion.commit()
            print(f"Película insertada: {nombre_pelicula}, Género: {genero}, Duración: {duracion} minutos")
    finally:
        conexion.close()

def insertar_renta():
    """
    Inserta un nuevo registro de renta en la base de datos con datos aleatorios.
    """
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            # Obtener un usuario aleatorio
            cursor.execute("SELECT idUsuario FROM usuarios ORDER BY RAND() LIMIT 1")
            id_usuario = cursor.fetchone()['idUsuario']
            # Obtener una película aleatoria
            cursor.execute("SELECT idPelicula FROM peliculas ORDER BY RAND() LIMIT 1")
            id_pelicula = cursor.fetchone()['idPelicula']
            # Fecha de renta aleatoria entre 1 y 10 días atrás
            fecha_renta = datetime.now() - timedelta(days=random.randint(1, 10))
            # Duración de la renta aleatoria entre 1 y 5 días
            dias_de_renta = random.randint(1, 5)
            # Estatus de la renta aleatorio (0 o 1)
            estatus = random.randint(0, 1)
            # Consulta SQL para insertar la renta
            sql = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            # Ejecutar la consulta SQL
            cursor.execute(sql, (id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus))
            conexion.commit()
            print(f"Renta insertada para el usuario con ID: {id_usuario} y película con ID: {id_pelicula}")
    finally:
        conexion.close()

def insertar_registros_en_todas_las_tablas():
    """
    Inserta al menos un registro en cada tabla de la base de datos.
    """
    insertar_usuario()
    insertar_pelicula()
    insertar_renta()

def filtrar_usuarios_apellido(apellido_terminacion):
    """
    Filtra y muestra los usuarios cuyo apellido coincide con la terminación dada.
    """
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
            patron = f'%{apellido_terminacion}'
            cursor.execute(sql, (patron, patron))
            resultado = cursor.fetchall()
            if not resultado:
                print("No se encontraron usuarios con ese apellido")
            for usuario in resultado:
                print(usuario)
    finally:
        conexion.close()

def cambiar_genero_pelicula(pelicula, genero):
    """
    Cambia el género de una película en la base de datos.
    """
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            # Buscar la película por nombre
            sql_buscar_pelicula = "SELECT * FROM peliculas WHERE nombre = %s"
            cursor.execute(sql_buscar_pelicula, (pelicula,))
            pelicula_cambiar = cursor.fetchone()
            if pelicula_cambiar:
                # Actualizar el género de la película
                sql_cambiar_genero = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
                cursor.execute(sql_cambiar_genero, (genero, pelicula))
                conexion.commit()
                print("Género cambiado con éxito!")
            else:
                print("Película no encontrada!")
    finally:
        conexion.close()

def eliminar_rentas_antiguas():
    """
    Elimina las rentas que tienen más de 3 días de antigüedad.
    """
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

def eliminar_registros_todas_las_tablas():
    """
    Elimina todos los registros de todas las tablas en la base de datos.
    """
    conexion = establecer_conexion()
    try:
        with conexion.cursor() as cursor:
            # Eliminar todos los registros de la tabla de rentas
            cursor.execute("DELETE FROM rentar")
            # Eliminar todos los registros de la tabla de usuarios
            cursor.execute("DELETE FROM usuarios")
            # Eliminar todos los registros de la tabla de películas
            cursor.execute("DELETE FROM peliculas")
            conexion.commit()
            print("Todos los registros de todas las tablas han sido eliminados")
    finally:
        conexion.close()

def main():
    """
    Función principal que muestra un menú y ejecuta las funciones según la opción seleccionada por el usuario.
    """
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

if __name__ == "__main__":
    main()

 
