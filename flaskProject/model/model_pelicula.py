from alchemyClasses.Peliculas import Peliculas
from alchemyClasses import db


# registra una pelicula en la base de datos
def registra_pelicula(nombre, genero, duracion, inventario):
    nueva_pelicula = Peliculas(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
    try:
        db.session.add(nueva_pelicula)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al registrar pelicula: ", e)
        db.session.rollback()  # Rollback en caso de error
        return -1


# ver las peliculas registradas de una tabla
def ver_peliculas():
    peliculas = Peliculas.query.all()
    return peliculas


# Obtener una pelicula por su id
def pelicula_por_id(id_pelicula: int):
    pelicula = Peliculas.query.filter_by(idPelicula=id_pelicula).first()
    return pelicula


# Elimina una pelicula de la base de datos
def elimina_pelicula(id: int):
    pelicula = pelicula_por_id(id)
    try:
        db.session.delete(pelicula)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al eliminar pelicula: ", e)
        return -1


# Actualiza una pelicula en la base de datos
def actualizar_pelicula(id, nombre=None, genero=None, duracion=None, inventario=None):
    pelicula = pelicula_por_id(id)
    if pelicula:
        try:
            if nombre is not None:
                pelicula.nombre = nombre
            if genero is not None:
                pelicula.genero = genero
            if duracion is not None:
                pelicula.duracion = duracion
            if inventario is not None:
                pelicula.inventario = inventario
            db.session.commit()
            return 0
        except Exception as e:
            print("Error al actualizar pelicula: ", e)
            db.session.rollback()  # Rollback en caso de error
            return -1
    else:
        return -1