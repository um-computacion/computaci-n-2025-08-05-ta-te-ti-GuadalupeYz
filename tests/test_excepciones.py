import unittest
from codigo.excepciones import PosOcupadaException, PosFueraDeRangoException

class TestExcepciones(unittest.TestCase):

    def test_excepcion_ocupada(self):
        with self.assertRaises(PosOcupadaException):
            raise PosOcupadaException("Casilla ocupada.")

    def test_excepcion_fuera_rango(self):
        with self.assertRaises(PosFueraDeRangoException):
            raise PosFueraDeRangoException("Fuera de rango.")

if __name__ == '__main__':
    unittest.main()
