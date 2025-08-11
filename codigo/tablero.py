from codigo.excepciones import PosOcupadaException, PosFueraDeRangoException

class Tablero:
    def __init__(self):
        self.contenedor = [["", "", ""] for _ in range(3)]

    def poner_la_ficha(self, fil, col, ficha):
        if not (0 <= fil <= 2 and 0 <= col <= 2):
            raise PosFueraDeRangoException(" Posición fuera del tablero (0 a 2).")

        if self.contenedor[fil][col] != "":
            raise PosOcupadaException(" Esa casilla ya está ocupada.")

        self.contenedor[fil][col] = ficha

    def tablero_lleno(self):
        return all(celda != "" for fila in self.contenedor for celda in fila)

    def hay_ganador(self, ficha):
        # Filas y columnas
        for i in range(3):
            if all(self.contenedor[i][j] == ficha for j in range(3)):
                return True
            if all(self.contenedor[j][i] == ficha for j in range(3)):
                return True
        # Diagonales
        if all(self.contenedor[i][i] == ficha for i in range(3)):
            return True
        if all(self.contenedor[i][2 - i] == ficha for i in range(3)):
            return True

        return False

    def obtener_tablero(self):
        return self.contenedor

    def reiniciar(self):
        self.contenedor = [["", "", ""] for _ in range(3)]

