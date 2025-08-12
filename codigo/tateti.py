
#coordina el juego, los turnos y define ganadores o empates

from codigo.tablero import Tablero
from codigo.jugadores import Jugador

class Tateti:
    def __init__(self, jugador1: Jugador, jugador2: Jugador) -> None:
        self.tablero: Tablero = Tablero()
        self.jugador1: Jugador = jugador1
        self.jugador2: Jugador = jugador2
        self.turno_actual: Jugador = jugador1
        self.ganador: Jugador | None = None
        self.empate: bool = False

    def ocupar_una_de_las_casillas(self, fil: int, col: int) -> None:
        self.tablero.poner_la_ficha(fil, col, self.turno_actual.obtener_ficha())

        if self.tablero.hay_ganador(self.turno_actual.obtener_ficha()):
            self.ganador = self.turno_actual
        elif self.tablero.tablero_lleno():
            self.empate = True
        else:
            self.cambiar_turno()

    def cambiar_turno(self) -> None:
        #cambio el turno entre jugador1 y jugador2
        if self.turno_actual == self.jugador1:
            self.turno_actual = self.jugador2
        else:
            self.turno_actual = self.jugador1

    def obtener_tablero(self) -> list[list[str]]:
        return self.tablero.obtener_tablero()

    def reiniciar_juego(self) -> None:
        self.tablero.reiniciar()
        self.turno_actual = self.jugador1
        self.ganador = None
        self.empate = False
