import matplotlib.pyplot as plt
import numpy as np

def montana(x):
    """
    Función que calcula la altura de una montaña en función de la distancia.

    Parameters:
        x (array_like): Valores de distancia a lo largo del eje x.

    Returns:
        array_like: Altura correspondiente a cada valor de distancia.
    """
    return np.abs(np.sin(x))

def graficar_montana():
    """
    Función que grafica una montaña utilizando la librería Matplotlib.
    """
    plt.figure(figsize=(8, 6))

    # Generar valores para la montaña
    x_values = np.linspace(0, 4 * np.pi, 1000)  # Valores de distancia a lo largo del eje x
    y_values = montana(x_values)  # Altura correspondiente a cada valor de distancia

    # Graficar la montaña
    plt.plot(x_values, y_values, 'b')  # 'b' para especificar el color azul

    # Etiquetas y título del gráfico
    plt.xlabel('Distancia')
    plt.ylabel('Altura')
    plt.title('Montaña')

    # Mostrar la cuadrícula en el gráfico
    plt.grid(True)

    # Mostrar el gráfico
    plt.show()

if __name__ == '__main__':
    graficar_montana()
