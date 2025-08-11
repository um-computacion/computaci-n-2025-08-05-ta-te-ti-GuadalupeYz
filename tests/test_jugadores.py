import unittest
from codigo.jugadores import Jugador

class TestJugador(unittest.TestCase):

    def test_crear_jugador(self):
        jugador = Jugador("Guada", "X")
        self.assertEqual(jugador.obtener_nombre(), "Guada")
        self.assertEqual(jugador.obtener_ficha(), "X")


    def test_ficha_valida(self):
        jugador = Jugador("Lupita", "O")
        self.assertIn(jugador.obtener_ficha(), ["X", "O"])

if __name__ == '__main__':
    unittest.main()
