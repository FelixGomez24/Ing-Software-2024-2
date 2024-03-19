from flask import Blueprint, request, render_template, flash, url_for, redirect
from datetime import date
from model import model_renta as mr

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')


@renta_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('baseRenta.html')


@renta_blueprint.route('/ver-rentas')
def ver_rentas():
    rentas = mr.ver_rentas()
    return render_template('ver_rentas.html', rentas=rentas)


# Agregar una nueva renta
@renta_blueprint.route('/agregar-renta', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        fecha_renta = date.today()  # Obtener la fecha actual
        id_usuario = request.form['idUsuario']
        id_pelicula = request.form['idPelicula']
        dias_de_renta = int(request.form['dias_de_renta'])
        estatus = True  # Supongamos que siempre inicia rentada

        resultado = mr.registra_renta(fecha_renta, id_usuario, id_pelicula, dias_de_renta, estatus)
        if resultado == 0:
            flash('Renta agregada correctamente', 'success')
        else:
            flash('Error al agregar la renta', 'error')

        return redirect(url_for('renta.ver_rentas'))

    # Si es método GET, renderizar el formulario para agregar una renta
    # Aquí debes proporcionar los datos necesarios para seleccionar un usuario y una película
    return render_template('add_renta.html')


@renta_blueprint.route('/actualiza-renta', methods=['GET', 'POST'])
def actualizar_renta():
    if request.method == 'GET':
        return render_template('obtener_renta.html')
    else:
        id_renta = request.form['idRenta']
        renta = mr.renta_por_id(id_renta)
        if not renta:
            flash('El ID de renta proporcionado no es válido')
            return redirect(url_for('renta.actualizar_renta'))

        return render_template('actualizar_renta.html', renta=renta)

@renta_blueprint.route('/procesar-actualizacion', methods=['POST'])
def procesar_actualizacion():
    id_renta = request.form['idRenta']
    fecha_renta = request.form.get('fechaRenta')
    dias_de_renta = request.form.get('diasDeRenta')
    estatus = request.form.get('estatus')

    respuesta = mr.actualizar_renta(id_renta, fechaRenta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)

    if respuesta == 0:
        flash('Renta actualizada correctamente')
    else:
        flash('Error al actualizar la renta')

    return redirect(url_for('renta.actualizar_renta'))


