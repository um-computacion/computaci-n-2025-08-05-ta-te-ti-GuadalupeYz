import unittest
from codigo.excepciones import PosOcupadaException, PosFueraDeRangoException
from codigo.tablero import Tablero
from codigo.jugadores import Jugador
from codigo.tateti import Tateti


class TestExcepciones(unittest.TestCase):

    def test_excepcion_ocupada_directa(self):
        with self.assertRaises(PosOcupadaException):
            raise PosOcupadaException("Casilla ocupada.")

    def test_excepcion_fuera_rango_directa(self):
        with self.assertRaises(PosFueraDeRangoException):
            raise PosFueraDeRangoException("Fuera de rango.")

    def test_excepcion_ocupada_en_tablero(self):
        tablero = Tablero()
        tablero.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_la_ficha(0, 0, "O")

    def test_excepcion_fuera_rango_en_tablero(self):
        tablero = Tablero()
        with self.assertRaises(PosFueraDeRangoException):
            tablero.poner_la_ficha(3, 0, "X")  # fila invalida

    def test_excepcion_fuera_rango_negativo(self):
        tablero = Tablero()
        with self.assertRaises(PosFueraDeRangoException):
            tablero.poner_la_ficha(-1, 0, "X")  # fila negativa

    def test_excepcion_ocupada_en_juego(self):
        jugador1 = Jugador("J1", "X")
        jugador2 = Jugador("J2", "O")
        juego = Tateti(jugador1, jugador2)
        juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            juego.ocupar_una_de_las_casillas(0, 0)  # misma casilla


if __name__ == '__main__':
    unittest.main()
