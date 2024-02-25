from flask import Flask

from alchemyClasses import db
from model import model_usuarios, model_peliculas, model_renta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


def mostrar_menu():
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por ID.")
    print("3. Actualizar la columna nombre de un registro.")
    print("4. Eliminar un registro por ID o todos los registros.")
    print("5. Salir")


def menu_ver_registros():
    print("1. Usuarios")
    print("2. Películas")
    print("3. Rentar")


def menu_filtrar_por_id():
    print("1. Filtrar usuarios por ID")
    print("2. Filtrar películas por ID")
    print("3. Filtrar rentas por ID")


def menu_actualizar_nombre():
    print("1. Actualizar nombre de usuario")
    print("2. Actualizar nombre de película")
    print("3. Actualizar fecha de renta")


def menu_eliminar():
    print("1. Eliminar un registro por ID")
    print("2. Eliminar todos los registros")


if __name__ == '__main__':
    with app.app_context():
        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                menu_ver_registros()
                opcion_tabla = input("Seleccione una tabla: ")
                if opcion_tabla == "1":
                    model_usuarios.mostrar_todos_los_usuarios()
                elif opcion_tabla == "2":
                    model_peliculas.mostrar_todas_las_peliculas()
                elif opcion_tabla == "3":
                    model_renta.mostrar_todas_las_rentas()

            elif opcion == "2":
                menu_filtrar_por_id()
                opcion_tabla = input("Seleccione una tabla: ")
                if opcion_tabla == "1":
                    id_usuario = int(input("Ingrese el ID del usuario que desea filtrar: "))
                    model_usuarios.obtener_id_usuario(id_usuario)
                elif opcion_tabla == "2":
                    id_pelicula = int(input("Ingrese el ID de la película que desea filtrar: "))
                    model_peliculas.obtener_id_pelicula(id_pelicula)
                elif opcion_tabla == "3":
                    id_renta = int(input("Ingrese el ID de la renta que desea filtrar: "))
                    model_renta.filtrar_renta_por_id(id_renta)

            elif opcion == "3":
                menu_actualizar_nombre()
                opcion_tabla = input("Seleccione una tabla: ")
                if opcion_tabla == "1":
                    id_usuario = int(input("Ingrese el ID del usuario que desea actualizar: "))
                    nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
                    model_usuarios.actualizar_nombre_usuario(id_usuario, nuevo_nombre)
                elif opcion_tabla == "2":
                    id_pelicula = int(input("Ingrese el ID de la película que desea actualizar: "))
                    nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
                    model_peliculas.actualizar_nombre_pelicula(id_pelicula, nuevo_nombre)
                elif opcion_tabla == "3":
                    id_renta = int(input("Ingrese el ID de la renta que desea actualizar: "))
                    nueva_fecha = input("Ingrese la nueva fecha de la renta (YYYY-MM-DD): ")
                    model_renta.actualizar_fecha_renta(id_renta, nueva_fecha)

            elif opcion == "4":
                menu_eliminar()
                opcion_tabla = input("Seleccione una tabla: ")
                if opcion_tabla == "1":
                    id_usuario = int(input("Ingrese el ID del usuario que desea eliminar: "))
                    model_usuarios.borrar_usuario_por_id(id_usuario)
                elif opcion_tabla == "2":
                    id_pelicula = int(input("Ingrese el ID de la película que desea eliminar: "))
                    model_peliculas.borrar_pelicula_por_id(id_pelicula)
                elif opcion_tabla == "3":
                    id_renta = int(input("Ingrese el ID de la renta que desea eliminar: "))
                    model_renta.borrar_renta_por_id(id_renta)
                elif opcion_tabla == "4":
                    opcion_borrar_todo = input("¿Está seguro que desea borrar todos los registros? (S/N): ")
                    if opcion_borrar_todo.upper() == "S":
                        model_usuarios.borrar_todos_los_usuarios()
                        model_peliculas.borrar_todas_las_peliculas()
                        model_renta.borrar_todas_las_rentas()

            elif opcion == "5":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
