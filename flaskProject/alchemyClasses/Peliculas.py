from sqlalchemy import Column, Integer, String
from alchemyClasses import db


class Peliculas(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    genero = Column(String(45), default=None)
    duracion = Column(Integer, default=None)
    inventario = Column(Integer, default=1)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"IdPelicula: {self.idPelicula}\n"\
               f"Nombre: {self.nombre}\n"\
               f"Genero: {self.genero}\n"\
               f"Duracion: {self.duracion}\n"\
               f"Inventario: {self.inventario}\n"