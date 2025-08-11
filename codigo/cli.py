
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from codigo.tateti import Tateti
from codigo.jugadores import Jugador
from codigo.excepciones import PosOcupadaException, PosFueraDeRangoException


def mostrar_tablero(tablero):
    print("\n  0   1   2")
    for idx, fila in enumerate(tablero):
        print(f"{idx} {' | '.join(c if c != '' else ' ' for c in fila)}")
        if idx < 2:
            print("  ---------")

def main():
    print(" ¡¡Bienvenidos al juego Tateti!! \n")

    nombre1 = input("Ingrese el nombre del Jugador 1 (ficha X): ")
    nombre2 = input("Ingrese el nombre del Jugador 2 (ficha O): ")

    jugador1 = Jugador(nombre1, "X")
    jugador2 = Jugador(nombre2, "O")

    juego = Tateti(jugador1, jugador2)

    while True:
        mostrar_tablero(juego.obtener_tablero())
        print(juego.turno_actual.obtener_nombre())
        print(juego.turno_actual.obtener_ficha())


        try:
            fil = int(input("Ingrese fila (0, 1, 2): "))
            col = int(input("Ingrese columna (0, 1, 2): "))
            juego.ocupar_una_de_las_casillas(fil, col)

        except ValueError:
            print(" Error: Ingrese un número entero válido.")
            continue
        except (PosOcupadaException, PosFueraDeRangoException) as e:
            print(f" {str(e)}")
            continue

        if juego.ganador:
            mostrar_tablero(juego.obtener_tablero())
            print(f"\n ¡{juego.ganador.nombre} ganó el juego! \n")
        elif juego.empate:
            mostrar_tablero(juego.obtener_tablero())
            print("\n ¡Empate! El tablero está lleno.\n")

        if juego.ganador or juego.empate:
            opcion = input("¿Desean jugar otra vez? (si/no): ").lower()
            if opcion == "si":
                juego.reiniciar_juego()
            else:
                print("¡¡Gracias por jugar mi Tateti!!")
                break

if __name__ == '__main__':
    main()

