from alchemyClasses.Usuarios import Usuarios
from alchemyClasses import db


# registra un usuario en la base de datos
def registra_usuario(nombre, apPat, apMat, password, email, profilePicture=None, superUser=None):
    nuevo_usuario = Usuarios(nombre=nombre, apPat=apPat, apMat=apMat, password=password, email=email, profilePicture=profilePicture, superUser=bool(superUser))
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al registrar usuario: ", e)
        db.session.rollback()  # Rollback en caso de error
        return -1


# ver los usuarios registrados de una tabla
def ver_usuarios():
    usuarios = Usuarios.query.all()
    return usuarios


# Obtener un usuario por su id
def usuario_por_id(id_Usuario:int):
    usuario = Usuarios.query.filter_by(idUsuario=id_Usuario).first()
    return usuario


# Elimina un usuario de la base de datos
def elimina_usuario(id:int):
    usuario = usuario_por_id(id)
    try:
        db.session.delete(usuario)
        db.session.commit()
        return 0
    except Exception as e:
        print("Error al eliminar usuario: ", e)
        return -1


# Actualiza un usuario en la base de datos

def actualizar_usuario(id, nombre=None, apPat=None, apMat=None, password=None, email=None, superUser=None):
    usuario = usuario_por_id(id)
    if usuario:
        try:
            if nombre is not None:
                usuario.nombre = nombre
            if apPat is not None:
                usuario.apPat = apPat
            if apMat is not None:
                usuario.apMat = apMat
            if password is not None:
                usuario.password = password
            if email is not None:
                usuario.email = email
            if superUser is not None:
                usuario.superUser = bool(superUser)

            db.session.commit()
            return 0
        except Exception as e:
            print("Error al actualizar usuario: ", e)
            return -1
    else:
        print("No se encontró ningún usuario con el ID proporcionado.")
        return -1
