import unittest
from codigo.tablero import Tablero
from codigo.excepciones import PosOcupadaException, PosFueraDeRangoException

class TestTablero(unittest.TestCase):

    def test_colocar_ficha_correctamente(self):
        tablero = Tablero()
        tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(tablero.obtener_tablero()[0][0], "X")

    def test_posicion_ocupada_lanza_excepcion(self):
        tablero = Tablero()
        tablero.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_la_ficha(0, 0, "O")

    def test_posicion_fuera_de_rango_lanza_excepcion(self):
        tablero = Tablero()
        with self.assertRaises(PosFueraDeRangoException):
            tablero.poner_la_ficha(3, 0, "X")
        with self.assertRaises(PosFueraDeRangoException):
            tablero.poner_la_ficha(0, -1, "O")

    def test_detectar_ganador_fila(self):
        tablero = Tablero()
        for col in range(3):
            tablero.poner_la_ficha(1, col, "X")
        self.assertTrue(tablero.hay_ganador("X"))

    def test_detectar_ganador_columna(self):
        tablero = Tablero()
        for fil in range(3):
            tablero.poner_la_ficha(fil, 2, "O")
        self.assertTrue(tablero.hay_ganador("O"))

    def test_detectar_ganador_diagonal(self):
        tablero = Tablero()
        for i in range(3):
            tablero.poner_la_ficha(i, i, "X")
        self.assertTrue(tablero.hay_ganador("X"))

    def test_tablero_lleno(self):
        tablero = Tablero()
        movimientos = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2)
        ]
        for idx, (fil, col) in enumerate(movimientos):
            ficha = "X" if idx % 2 == 0 else "O"
            tablero.poner_la_ficha(fil, col, ficha)
        self.assertTrue(tablero.tablero_lleno())

if __name__ == '__main__':
    unittest.main()

