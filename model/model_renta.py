from alchemyClasses.Renta import Renta  # Importa la clase Rentar desde el módulo alchemyClasses.Rentar
from alchemyClasses import db  # Importa la base de datos desde el módulo alchemyClasses


# Función para mostrar todas las rentas
def mostrar_todas_las_rentas():
    rentas = Renta.query.all()  # Obtiene todas las rentas de la base de datos
    for renta in rentas:
        print(renta)  # Muestra la información de cada renta


# Función para filtrar una renta por su ID
def filtrar_renta_por_id(id_renta):
    renta = Renta.query.get(id_renta)  # Obtiene la renta con el ID proporcionado
    if renta:
        print(renta)  # Muestra la información de la renta
    else:
        print(
            f"No se encontró ninguna renta con el ID {id_renta}.")  # Muestra un mensaje de error si no se encuentra
        # la renta


# Función para actualizar la fecha de una renta
def actualizar_fecha_renta(id_renta, nueva_fecha_renta):
    renta = Renta.query.get(id_renta)  # Obtiene la renta con el ID proporcionado
    if renta:
        renta.fecha_renta = nueva_fecha_renta  # Actualiza la fecha de la renta
        db.session.commit()  # Confirma los cambios en la base de datos
        print("Fecha de la renta actualizada con éxito!")  # Muestra un mensaje de éxito
    else:
        print(
            f"No se encontró ninguna renta con el ID {id_renta}.")  # Muestra un mensaje de error si no se encuentra
        # la renta


# Función para borrar una renta por su ID
def borrar_renta_por_id(id_renta):
    renta = Renta.query.get(id_renta)  # Obtiene la renta con el ID proporcionado
    if renta:
        db.session.delete(renta)  # Elimina la renta de la base de datos
        db.session.commit()  # Confirma los cambios en la base de datos
        print(f"Renta con el ID {id_renta} ha sido eliminada.")  # Muestra un mensaje de éxito
    else:
        print(
            f"No se encontró ninguna renta con el ID {id_renta}.")  # Muestra un mensaje de error si no se encuentra
        # la renta


# Función para borrar todas las rentas
def borrar_todas_las_rentas():
    rentas = Renta.query.all()  # Obtiene todas las rentas de la base de datos
    for renta in rentas:
        db.session.delete(renta)  # Elimina cada renta de la base de datos
    db.session.commit()  # Confirma los cambios en la base de datos
    print("Todas las rentas han sido eliminadas.")  # Muestra un mensaje de éxito

# Ejemplo de uso:
# mostrar_todas_las_rentas()
# filtrar_renta_por_id(1)
# actualizar_fecha_renta(1, nueva_fecha_renta)
# borrar_renta_por_id(1)
# borrar_todas_las_rentas()
