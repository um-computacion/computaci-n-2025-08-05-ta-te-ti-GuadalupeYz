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

    def test_str_jugador(self):
        jugador = Jugador("Ana", "X")
        self.assertEqual(str(jugador), "Ana (X)")

    def test_nombre_distintos(self):
        j1 = Jugador("Juan", "X")
        j2 = Jugador("Pedro", "O")
        self.assertNotEqual(j1.obtener_nombre(), j2.obtener_nombre())

    def test_ficha_distinta(self):
        j1 = Jugador("Juan", "X")
        j2 = Jugador("Pedro", "O")
        self.assertNotEqual(j1.obtener_ficha(), j2.obtener_ficha())

    def test_cambiar_nombre(self):
        jugador = Jugador("ViejoNombre", "X")
        jugador.nombre = "NuevoNombre"
        self.assertEqual(jugador.obtener_nombre(), "NuevoNombre")

    def test_cambiar_ficha(self):
        jugador = Jugador("Guada", "X")
        jugador.ficha = "O"
        self.assertEqual(jugador.obtener_ficha(), "O")


if __name__ == '__main__':
    unittest.main()

