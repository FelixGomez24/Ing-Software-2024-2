from flask import Blueprint, request, render_template, flash, url_for, redirect

import model.model_pelicula
from model import model_pelicula as mp

# CRUD Películas

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')


@pelicula_blueprint.route('/', methods=['GET'])
def raiz():
    return render_template('basePelicula.html')


# Agregar PELÍCULAS
@pelicula_blueprint.route('/registra-pelicula', methods=['GET', 'POST'])
def registra_pelicula():
    if request.method == 'GET':
        return render_template('add_pelicula.html')
    else:
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        mp.registra_pelicula(nombre, genero, duracion, inventario)
        flash('Pelicula registrada exitosamente')
        return redirect(url_for('pelicula.registra_pelicula'))


# Ver PELÍCULAS
@pelicula_blueprint.route('/ver-peliculas')
def ver_peliculas():
    peliculas = mp.ver_peliculas()
    return render_template('ver_peliculas.html', peliculas=peliculas)


# Eliminar PELÍCULAS
@pelicula_blueprint.route('/borrar-pelicula', methods=['GET', 'POST'])
def eliminar_pelicula():
    if request.method == 'GET':
        return render_template('borrar_pelicula.html')
    else:
        id_pelicula = request.form['idPelicula']
        respuesta = mp.elimina_pelicula(id_pelicula)
        if respuesta == -1:
            flash('Error al eliminar la película')
        else:
            flash('Película eliminada correctamente')
        return redirect(url_for('pelicula.eliminar_pelicula'))


# Actualizar película
@pelicula_blueprint.route('/actualizar-pelicula', methods=['GET', 'POST'])
def actualizar_pelicula():
    if request.method == 'GET':
        return render_template('obtener_pelicula.html')
    else:
        id_pelicula = request.form['idPelicula']
        pelicula = mp.pelicula_por_id(id_pelicula)
        if not pelicula:
            flash('El ID de película proporcionado no es válido')
            return redirect(url_for('pelicula.actualizar_pelicula'))

        return render_template('actualizar_pelicula.html', pelicula=pelicula)


@pelicula_blueprint.route('/procesar-actualizacion', methods=['POST'])
def procesar_actualizacion():
    id_pelicula = request.form['idPelicula']
    nombre = request.form.get('nombre')
    genero = request.form.get('genero')
    duracion = request.form.get('duracion')
    inventario = request.form.get('inventario')

    respuesta = mp.actualizar_pelicula(id_pelicula, nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)

    if respuesta == 0:
        flash('Película actualizada correctamente')
    else:
        flash('Error al actualizar la película')

    return redirect(url_for('pelicula.actualizar_pelicula'))
