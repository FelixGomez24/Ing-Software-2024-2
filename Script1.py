import random


def convertir_puntos_a_string(punto):
    """
    Convierte el puntaje numérico de un jugador en una cadena de los puntos validos: 15, 30, 40, Ventaja  .
    Parameters:
        punto (int): Puntaje numérico de un jugador.
    Returns:
        str: Representación de puntos obtenidos puntaje.
    """
    if punto == 0:
        return "0"
    elif punto == 1:
        return "15"
    elif punto == 2:
        return "30"
    elif punto == 3:
        return "40"
    else:
        return "Ventaja"


class JuegoTenis:
    def __init__(self, jugador01, jugador02):
        """
        Inicializamos un nuevo juego de tenis con dos jugadores y puntajes iniciales en ceros .
        Parametros:
            jugador01 (str): Nombre del primer jugador.
            jugador02 (str): Nombre del segundo jugador.
        """
        self.jugadores = [jugador01, jugador02]  # Lista de jugadores
        self.sets = [0, 0]  # Puntajes de Sets de cada jugador
        self.juegos = [0, 0]  # Puntajes de Juegos de cada jugador
        self.puntos = [0, 0]  # Puntajes de Puntos de cada jugador
        self.sacador_actual = random.randint(0, 1)  # Selección aleatoria del jugador que comienza saca

    def imprimir_puntuacion(self):
        """
        Imprimimos en consola la puntuación actual del juego.
        """
        p1_puntos, p2_puntos = self.puntos
        sacando = self.jugadores[self.sacador_actual]
        descripcion_puntuacion = f"{convertir_puntos_a_string(p1_puntos)}-{convertir_puntos_a_string(p2_puntos)}"
        print("\nMarcador:")
        print(f"Sets: {self.jugadores[0]} {self.sets[0]} - {self.sets[1]} {self.jugadores[1]}")
        print(f"Juegos: {self.juegos[0]} - {self.juegos[1]}")
        print(f"Puntos: {descripcion_puntuacion}")
        print(f"Sacando: {sacando}")

    def anotar_punto(self, ganadorJuego):
        """
        Registramos el puntaje para el jugador ganador del punto y verifica si se ganó un juego.
        Parameters:
            ganadorJuego (int): Índice del jugador ganador del punto (1 para jugador1, 2 para jugador2).
        """
        if ganadorJuego == 1:
            self.puntos[0] += 1
        else:
            self.puntos[1] += 1
        self.verificar_ganador_juego()

    def verificar_ganador_juego(self):
        """
        Verificamos si algún jugador ganó un juego y actualiza los puntajes en consecuencia.
        """
        if self.puntos[0] >= 4 or self.puntos[1] >= 4:
            if abs(self.puntos[0] - self.puntos[1]) >= 2: # Diferencia de 2 para poder ganar, anotar dos puntos seguidos
                ganador_juego = self.jugadores[0] if self.puntos[0] > self.puntos[1] else self.jugadores[1]
                print(f"\nJuego para {ganador_juego}")
                if ganador_juego == self.jugadores[0]:
                    self.juegos[0] += 1
                else:
                    self.juegos[1] += 1
                self.puntos[0], self.puntos[1] = 0, 0
                self.verificar_ganador_set()
                self.cambiar_sacador()
                self.verificar_cambio_cancha()
            elif self.puntos[0] == self.puntos[1]:  # Empate en 40-40
                self.puntos[0], self.puntos[1] = 3, 3  # Reiniciar a 40-40

    def verificar_ganador_set(self):
        """
        Verificamos si algún jugador ganó un set y se actualizan los puntajes en consecuencia.
        """
        if self.juegos[0] >= 6 or self.juegos[1] >= 6:
            if abs(self.juegos[0] - self.juegos[1]) >= 2: # Debe de ganar 2 juegos mas que el otro jugador
                ganador_set = self.jugadores[0] if self.juegos[0] > self.juegos[1] else self.jugadores[1]
                print(f"\nSet para {ganador_set}")
                if ganador_set == self.jugadores[0]:
                    self.sets[0] += 1
                else:
                    self.sets[1] += 1
                self.juegos[0], self.juegos[1] = 0, 0
                if self.sets[0] == 2 or self.sets[1] == 2:
                    print(f"\n{ganador_set} gana el partido {self.sets[0]}-{self.sets[1]} sets.")
                    exit()

    def cambiar_sacador(self):
        """
        Cambiamos el jugador que sirve en el próximo punto.
        """
        self.sacador_actual = 1 - self.sacador_actual  # Cambio alternado del sacador

    def verificar_cambio_cancha(self):
        """
        Verifica si se necesita un cambio de cancha y lo imprime en consola.
        """
        total_juegos = sum(self.juegos)
        if total_juegos % 2 != 0:
            print("\nCambio de cancha.")

    def obtener_jugador_sirviendo(self):
        """
        Determina el jugador que sirve en el próximo punto.

        Returns:
            str: Nombre del jugador que sirve.
        """
        if sum(self.puntos) % 2 == 0:
            return self.jugadores[self.sacador_actual]
        else:
            return self.jugadores[1 - self.sacador_actual]


# Aquí comienza la ejecución del juego

jugador1 = input("Ingrese el nombre del Jugador 1: ")
jugador2 = input("Ingrese el nombre del Jugador 2: ")

juego = JuegoTenis(jugador1, jugador2)

while True:
    juego.imprimir_puntuacion()
    try:
        ganador = int(input(f"\n¿Quien gana el punto? [{jugador1}(1) o {jugador2}(2)]: "))
        if ganador not in [1, 2]:
            raise ValueError("Entrada invalida. Elija 1 o 2.")
        juego.anotar_punto(ganador)
    except ValueError as e:
        print(e)
