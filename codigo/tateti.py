from codigo.tablero import Tablero

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.tablero = Tablero()
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno_actual = jugador1
        self.ganador = None
        self.empate = False

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno_actual.obtener_ficha())

        if self.tablero.hay_ganador(self.turno_actual.ficha):
            self.ganador = self.turno_actual
        elif self.tablero.tablero_lleno():
            self.empate = True
        else:
            self.cambiar_turno()

    def cambiar_turno(self):
        self.turno_actual = self.jugador1 if self.turno_actual == self.jugador2 else self.jugador2

    def obtener_tablero(self):
        return self.tablero.obtener_tablero()

    def reiniciar_juego(self):
        self.tablero.reiniciar()
        self.turno_actual = self.jugador1
        self.ganador = None
        self.empate = False
