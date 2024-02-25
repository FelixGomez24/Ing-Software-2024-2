from sqlalchemy import Column, Integer, String, LargeBinary, Boolean, Index

from alchemyClasses import db


class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = (
        Index('email_unique_idx', 'email', unique=True),
    )
    idUsuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200), nullable=False)
    apPat = Column(String(200), nullable=False)
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(200), default=None, unique=True)
    profilePicture = Column(LargeBinary)
    superUser = Column(Boolean, default=False)
    __table_args__ = (
        {'mysql_engine': 'InnoDB', 'mysql_auto_increment': 13, 'mysql_charset': 'utf8mb4'},
    )

    def __init__(self, nombre, appat, apmat=None, password=None, email=None, superuser=False):
        self.nombre = nombre
        self.apPat = appat
        self.apMat = apmat
        self.password = password
        self.email = email
        self.superUser = superuser

    def __str__(self):
        return (f'idUsuario: {self.idUsuario}, nombre: {self.nombre}, apPat: {self.apPat}, apMat: {self.apMat}, '
                f'password: {self.password}, email: {self.email}, superUser: {self.superUser}')
