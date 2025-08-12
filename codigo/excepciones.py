#aca defino excepciones q pueden pasar en el juego

class PosOcupadaException(Exception):
    #error cuando un jugador intenta poner una ficha en una casilla ocupada
    pass

class PosFueraDeRangoException(Exception):
    #error cuando un jugador ingresa una fila o columna fuera del rango 0 a 2
    pass
