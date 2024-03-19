from flask import Blueprint, request, render_template, flash, url_for, redirect

import model.model_usuario
from model import model_usuario as mu

# CRUD Usuarios

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')


@usuario_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('baseUsuario.html')


# Agregar USUARIOS
@usuario_blueprint.route('/registra-usuario', methods=['GET', 'POST'])
def registra_usuario():
    if request.method == 'GET':
        return render_template('add_usuario.html')
    else:
        nombre = request.form['nombre']
        apPat = request.form['apPat']
        apMat = request.form['apMat']
        password = request.form['password']
        email = request.form['email']
        super_user = 0
        if 'SuperUser' in request.form:
            super_user = '1'
        mu.registra_usuario(nombre, apPat, apMat, password, email, None, super_user)
        flash('Usuario registrado exitosamente')
        return redirect(url_for('usuario.registra_usuario'))


# Ver USUARIO
@usuario_blueprint.route('/ver-usuarios')
def ver_usuarios():
    usuarios = mu.ver_usuarios()
    return render_template('ver_usuarios.html', usuarios=usuarios)


# Eliminar Usuario
@usuario_blueprint.route('/borrar-usuario', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'GET':
        return render_template('borrar_usuario.html')
    else:
        id = request.form['idUsuario']
        respuesta = mu.elimina_usuario(id)
        if respuesta == -1:
            flash('Error al eliminar el usuario')
        else:
            flash('Usuario eliminado correctamente')
        return redirect(url_for('usuario.eliminar_usuario'))


# Actualizar usuario
@usuario_blueprint.route('/actualizar-usuario', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'GET':
        return render_template('obtener_usuario.html')
    else:
        id_usuario = request.form['idUsuario']
        usuario = mu.usuario_por_id(id_usuario)
        if not usuario:
            flash('El ID de usuario proporcionado no es válido')
            return redirect(url_for('usuario.actualizar_usuario'))

        return render_template('actualizar_usuario.html', usuario=usuario)

@usuario_blueprint.route('/procesar-actualizacion', methods=['POST'])
def procesar_actualizacion():
    id_usuario = request.form['idUsuario']
    nombre = request.form.get('nombre')
    apPat = request.form.get('apPat')
    apMat = request.form.get('apMat')
    password = request.form.get('password')
    email = request.form.get('email')
    super_user = request.form.get('SuperUser')

    respuesta = mu.actualizar_usuario(id_usuario, nombre=nombre, apPat=apPat, apMat=apMat, password=password, email=email, superUser=super_user)

    if respuesta == 0:
        flash('Usuario actualizado correctamente')
    else:
        flash('Error al actualizar el usuario')

    return redirect(url_for('usuario.actualizar_usuario'))
