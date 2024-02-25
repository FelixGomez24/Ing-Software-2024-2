from alchemyClasses.Usuarios import Usuarios  # Importa la clase Usuarios desde el módulo alchemyClasses.Usuario
from alchemyClasses import db  # Importa la base de datos desde el módulo alchemyClasses


# Función para borrar un usuario por su ID
def borrar_usuario_por_id(id_usuario):
    usuario = Usuarios.query.get(id_usuario)  # Obtiene el usuario con el ID proporcionado
    if usuario:
        db.session.delete(usuario)  # Elimina el usuario de la base de datos
        db.session.commit()  # Confirma los cambios en la base de datos
        print(f"Usuario con el ID {id_usuario} ha sido eliminado.")  # Muestra un mensaje de éxito
    else:
        print(
            f"No se encontró ningún usuario con el ID {id_usuario}.")  # Muestra un mensaje de error si no se
        # encuentra el usuario


# Función para borrar todos los usuarios
def borrar_todos_los_usuarios():
    usuarios = Usuarios.query.all()  # Obtiene todos los usuarios de la base de datos
    for usuario in usuarios:
        db.session.delete(usuario)  # Elimina cada usuario de la base de datos
    db.session.commit()  # Confirma los cambios en la base de datos
    print("Todos los usuarios han sido eliminados.")  # Muestra un mensaje de éxito


# Función para actualizar el nombre de un usuario
def actualizar_nombre_usuario(id_usuario, nuevo_nombre):
    usuario = Usuarios.query.get(id_usuario)  # Obtiene el usuario con el ID proporcionado
    if usuario:
        usuario.nombre = nuevo_nombre  # Actualiza el nombre del usuario
        db.session.commit()  # Confirma los cambios en la base de datos
        print("Nombre del usuario actualizado con éxito!")  # Muestra un mensaje de éxito
    else:
        print(
            f"No se encontró ningún usuario con el ID {id_usuario}.")  # Muestra un mensaje de error si no se
        # encuentra el usuario


# Función para mostrar todos los usuarios
def mostrar_todos_los_usuarios():
    usuarios = Usuarios.query.all()  # Obtiene todos los usuarios de la base de datos
    for usuario in usuarios:
        print(usuario)  # Muestra la información de cada usuario


# Función para obtener el ID de un usuario por su nombre
def obtener_id_usuario(email_usuario):
    usuario = Usuarios.query.filter_by(
        email=email_usuario).first()  # Obtiene el primer usuario con el email proporcionado
    if usuario:
        return usuario.idUsuario  # Devuelve el ID del usuario encontrado
    else:
        print(
            f"No se encontró ningún usuario con el email '{email_usuario}'.")  # Muestra un mensaje de error si no se
        # encuentra el usuario

# Ejemplo de uso:
# borrar_usuario_por_id(1)
# borrar_todos_los_usuarios()
# actualizar_nombre_usuario(1, "Nuevo Nombre")
# mostrar_todos_los_usuarios()
# id_usuario = obtener_id_usuario("correo@ejemplo.com")
