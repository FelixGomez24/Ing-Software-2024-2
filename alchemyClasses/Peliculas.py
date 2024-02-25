from sqlalchemy import Column, Integer, String
from alchemyClasses import db


class Peliculas(db.Model):
    __tablename__ = 'peliculas'
    id_pelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    genero = Column(String(45))
    duracion = Column(Integer, default=None)
    inventario = Column(Integer, nullable=True, default=1)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return (f'idPelicula: {self.idPelicula}, nombre: {self.nombre}, genero: {self.genero}, duracion: '
                f'{self.duracion}, inventario: {self.inventario}')
