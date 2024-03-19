from sqlalchemy import Column, Integer, String, Boolean
from alchemyClasses import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200), nullable=True)
    password = Column(String(64))
    email = Column(String(200), default=None, unique=True)
    profilePicture = Column(String(200), nullable=True)
    superUser = Column(Boolean, default=None)

    def __init__(self, nombre, apPat, apMat, password, email, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f"IdUsuario: {self.idUsuario}\n"\
               f"Nombre: {self.nombre}\n"\
               f"ApellidoPaterno: {self.apPat}\n"\
               f"ApellidoMaterno: {self.apMat}\n"\
               f"Contraseña: {self.password}\n"\
               f"Email: {self.email}\n"
