from alchemyClasses.Peliculas import Peliculas  # Importa la clase Pelicula desde el módulo alchemyClasses.Pelicula
from alchemyClasses import db  # Importa la base de datos desde el módulo alchemyClasses


# Función para borrar una película por su ID
def borrar_pelicula_por_id(id_pelicula):
    pelicula = Peliculas.query.get(id_pelicula)  # Obtiene la película con el ID proporcionado
    if pelicula:
        db.session.delete(pelicula)  # Elimina la película de la base de datos
        db.session.commit()  # Confirma los cambios en la base de datos
        print(f"Película con el ID {id_pelicula} ha sido eliminada.")  # Muestra un mensaje de éxito
    else:
        print(
            f"No se encontró ninguna película con el ID {id_pelicula}.")  # Muestra un mensaje de error si no se
        # encuentra la película


# Función para borrar todas las películas
def borrar_todas_las_peliculas():
    peliculas = Peliculas.query.all()  # Obtiene todas las películas de la base de datos
    for pelicula in peliculas:
        db.session.delete(pelicula)  # Elimina cada película de la base de datos
    db.session.commit()  # Confirma los cambios en la base de datos
    print("Todas las películas han sido eliminadas.")  # Muestra un mensaje de éxito


# Función para actualizar el nombre de una película
def actualizar_nombre_pelicula(id_pelicula, nuevo_nombre):
    pelicula = Peliculas.query.get(id_pelicula)  # Obtiene la película con el ID proporcionado
    if pelicula:
        pelicula.nombre = nuevo_nombre  # Actualiza el nombre de la película
        db.session.commit()  # Confirma los cambios en la base de datos
        print("Nombre de la película actualizado con éxito!")  # Muestra un mensaje de éxito
    else:
        print(
            f"No se encontró ninguna película con el ID {id_pelicula}.")  # Muestra un mensaje de error si no se
        # encuentra la película


# Función para mostrar todas las películas
def mostrar_todas_las_peliculas():
    peliculas = Peliculas.query.all()  # Obtiene todas las películas de la base de datos
    for pelicula in peliculas:
        print(pelicula)  # Muestra la información de cada película


# Función para obtener el ID de una película por su nombre
def obtener_id_pelicula(nombre_pelicula):
    pelicula = Peliculas.query.filter_by(
        nombre=nombre_pelicula).first()  # Obtiene la primera película con el nombre proporcionado
    if pelicula:
        return pelicula.idPelicula  # Devuelve el ID de la película encontrada
    else:
        print(
            f"No se encontró ninguna película con el nombre '{nombre_pelicula}'.")  # Muestra un mensaje de error si
        # no se encuentra la película

# Ejemplo de uso:
# borrar_pelicula_por_id(1)
# borrar_todas_las_peliculas()
# actualizar_nombre_pelicula(1, "Nuevo Nombre")
# mostrar_todas_las_peliculas()
# id_pelicula = obtener_id_pelicula("Nombre Película")
