from alchemyClasses.Rentas import Rentas
from alchemyClasses import db


# registra una renta en la base de datos
def registra_renta(fechaRenta, dias_de_renta, estatus):
    nueva_renta = Rentas(fechaRenta=fechaRenta, dias_de_renta=dias_de_renta, estatus=estatus)
    try:
        db.session.add(nueva_renta)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al registrar renta: ", e)
        db.session.rollback()  # Rollback en caso de error
        return -1


# ver las rentas registradas de una tabla
def ver_rentas():
    rentas = Rentas.query.all()
    return rentas


# Obtener una pelicula por su id
def renta_por_id(id_renta: int):
    renta = Rentas.query.filter_by(idRenta=id_renta).first()
    return renta


# Actualiza una renta en la base de datos
def actualizar_renta(id, fechaRenta=None, dias_de_renta=None, estatus=None):
    renta = renta_por_id(id)
    if renta:
        try:
            if fechaRenta is not None:
                renta.fechaRenta = fechaRenta
            if dias_de_renta is not None:
                renta.dias_de_renta = dias_de_renta
            if estatus is not None:
                renta.estatus = estatus
            db.session.commit()
            return 0
        except Exception as e:
            print("Error al actualizar renta: ", e)
            db.session.rollback()  # Rollback en caso de error
            return -1
    else:
        return -1
