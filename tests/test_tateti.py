import unittest
from codigo.jugadores import Jugador
from codigo.tateti import Tateti
from codigo.excepciones import PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.j1 = Jugador("Jugador 1", "X")
        self.j2 = Jugador("Jugador 2", "O")
        self.juego = Tateti(self.j1, self.j2)

    def test_turno_alternado(self):
        self.assertEqual(self.juego.turno_actual, self.j1)
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno_actual, self.j2)

    def test_ganador_detectado(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 0)  # O
        self.juego.ocupar_una_de_las_casillas(0, 1)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(0, 2)  # X gana

        self.assertEqual(self.juego.ganador, self.j1)

    def test_empate_detectado(self):
        jugadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2),
        ]
        for idx, (f, c) in enumerate(jugadas):
            self.juego.ocupar_una_de_las_casillas(f, c)
        self.assertTrue(self.juego.empate)

    def test_reiniciar_juego(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.juego.reiniciar_juego()
        self.assertEqual(self.juego.obtener_tablero(), [["", "", ""], ["", "", ""], ["", "", ""]])
        self.assertIsNone(self.juego.ganador)
        self.assertFalse(self.juego.empate)
        self.assertEqual(self.juego.turno_actual, self.j1)
    def test_jugada_en_posicion_ocupada_lanza_excepcion(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_ganador_por_columna(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(0, 1)  # O
        self.juego.ocupar_una_de_las_casillas(1, 0)  # X
        self.juego.ocupar_una_de_las_casillas(1, 1)  # O
        self.juego.ocupar_una_de_las_casillas(2, 0)  # X gana
        self.assertEqual(self.juego.ganador, self.j1)

    def test_ganador_por_diagonal(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  # X
        self.juego.ocupar_una_de_las_casillas(0, 1)  # O
        self.juego.ocupar_una_de_las_casillas(1, 1)  # X
        self.juego.ocupar_una_de_las_casillas(0, 2)  # O
        self.juego.ocupar_una_de_las_casillas(2, 2)  # X gana
        self.assertEqual(self.juego.ganador, self.j1)

    def test_empate_no_deja_jugar_mas(self):
        jugadas = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2),
        ]
        for idx, (f, c) in enumerate(jugadas):
            self.juego.ocupar_una_de_las_casillas(f, c)
        self.assertTrue(self.juego.empate)
        tablero_antes = self.juego.obtener_tablero()
        # Intentar otra jugada no debería cambiar nada
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(tablero_antes, self.juego.obtener_tablero())

if __name__ == '__main__':
    unittest.main()
