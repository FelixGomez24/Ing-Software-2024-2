from sqlalchemy import Column, Integer, DateTime, ForeignKey
from alchemyClasses import db
from datetime import date

from alchemyClasses.Peliculas import Peliculas
from alchemyClasses.Usuarios import Usuarios


class Renta(db.Model):
    from sqlalchemy import Column, Integer, DateTime, ForeignKey
    from alchemyClasses import db
    from datetime import date

    from alchemyClasses.Peliculas import Peliculas
    from alchemyClasses.Usuarios import Usuarios

    class Rentar(db.Model):
        __tablename__ = 'rentar'
        idRentar = Column(Integer, primary_key=True)
        idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
        idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
        fecha_renta = Column(DateTime)
        dias_de_renta = Column(Integer, default=5)
        estatus = Column(Integer, default=1)

        def __init__(self, idUsuario, idPelicula, fechaRenta, fechaDevolucion):
            self.idUsuario = idUsuario
            self.idPelicula = idPelicula
            self.fechaRenta = fechaRenta
            self.fechaDevolucion = fechaDevolucion
            self.rentaActiva = True

        def __str__(self):
            return (
                f'idRentar: {self.idRentar}, idUsuario: {self.idUsuario}, idPelicula: {self.idPelicula}, fecha_renta:'
                f' {self.fecha_renta}, dias_de_renta: {self.dias_de_renta}, estatus: {self.estatus}')
