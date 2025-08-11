class PosOcupadaException(Exception):
    """Se lanza cuando se intenta ocupar una posición ya ocupada en el tablero."""
    pass

class PosFueraDeRangoException(Exception):
    """Se lanza cuando se intenta poner una ficha fuera del tablero (índices inválidos)."""
    pass