from sqlalchemy import Column, Integer, DateTime, ForeignKey
from alchemyClasses import db


class Rentas(db.Model):
    __tablename__ = 'rentas'
    idRenta = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fechaRenta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, default=5)
    estatus = Column(Integer, default=0)

    def __init__(self, idUsuario, idPelicula, fechaRenta, dias_de_renta, estatus):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fechaRenta = fechaRenta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f"IdRenta: {self.idRenta}\n" \
               f"IdUsuario: {self.idUsuario}\n" \
               f"IdPelicula: {self.idPelicula}\n" \
               f"FechaRenta: {self.fechaRenta}\n" \
               f"Dias de renta: {self.dias_de_renta}\n" \
               f"Estatus: {self.estatus}\n"
