
#representa a el jugador del Tateti con su nombre y ficha

class Jugador:
    def __init__(self, nombre: str, ficha: str) -> None:
        self.nombre: str = nombre
        self.ficha: str = ficha

    def obtener_nombre(self) -> str:
        #nombre del jugador
        return self.nombre

    def obtener_ficha(self) -> str:
        #ficha del jugador 
        return self.ficha

    def __str__(self) -> str:
        #representación jugador
        return f"{self.nombre} ({self.ficha})"
