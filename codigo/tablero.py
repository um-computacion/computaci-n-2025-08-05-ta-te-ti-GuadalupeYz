
#es el tablero del Tateti y tamb sirve para colocar fichas y verificar resultados

from codigo.excepciones import PosOcupadaException, PosFueraDeRangoException

class Tablero:
    def __init__(self) -> None:
        #lista de listas para representar las 3 filas y 3 columnas
        self.contenedor: list[list[str]] = [["", "", ""] for _ in range(3)]

    def poner_la_ficha(self, fil: int, col: int, ficha: str) -> None:
        if not (0 <= fil <= 2 and 0 <= col <= 2):
            raise PosFueraDeRangoException("Posición fuera del tablero (0 a 2).")

        if self.contenedor[fil][col] != "":
            raise PosOcupadaException("Esa casilla ya está ocupada.")

        self.contenedor[fil][col] = ficha

    def tablero_lleno(self) -> bool:
        #Da True si todas las casillas están ocupadas
        for fila in self.contenedor:
            for celda in fila:
                if celda == "":
                    return False
        return True

    def hay_ganador(self, ficha: str) -> bool:
        #si hay 3 fichas iguales en línea
        # Filas
        for fila in self.contenedor:
            if fila[0] == ficha and fila[1] == ficha and fila[2] == ficha:
                return True
        # Columnas
        for col in range(3):
            if (self.contenedor[0][col] == ficha and
                self.contenedor[1][col] == ficha and
                self.contenedor[2][col] == ficha):
                return True
        # Diagonales
        if (self.contenedor[0][0] == ficha and
            self.contenedor[1][1] == ficha and
            self.contenedor[2][2] == ficha):
            return True
        if (self.contenedor[0][2] == ficha and
            self.contenedor[1][1] == ficha and
            self.contenedor[2][0] == ficha):
            return True

        return False

    def obtener_tablero(self) -> list[list[str]]:
        return self.contenedor

    def reiniciar(self) -> None:
        #pongo tablero vacío
        self.contenedor = [["", "", ""] for _ in range(3)]
