# Interfaz Tateti

from src.tateti import Tateti
from src.jugador import Jugador
from src.tablero import PosOcupadaException

def main():
    print("¡Bienvenidos al Tateti!")

    nombre1 = input("Ingrese nombre del jugador X: ")
    nombre2 = input("Ingrese nombre del jugador O: ")
    j1 = Jugador(nombre1, "X")
    j2 = Jugador(nombre2, "O")

    juego = Tateti(j1, j2)

    while True:
        print("\nTablero:")
        juego.tablero.mostrar_tablero()
        jugador = juego.jugador_actual()
        print(f"Turno de {jugador.nombre} ({jugador.ficha})")

        try:
            fila = int(input("Ingrese fila (0-2): "))
            columna = int(input("Ingrese columna (0-2): "))
            juego.ocupar_casilla(fila, columna)
        
            # Evaluar ganador
            if juego.tablero.hay_ganador(jugador.ficha):
                juego.tablero.mostrar_tablero()
                print(f"¡Felicidades {jugador.nombre}! Ganaste el juego.")
                break

            # Evaluar empate
            if juego.tablero.contenedor_lleno():
                juego.tablero.mostrar_tablero()
                print("¡Es un empate! No quedan más movimientos.")
                break

        except ValueError:
            print("Debe ingresar números válidos.")
        except PosOcupadaException as e:
            print(e)
        except IndexError:
            print("Fila o columna fuera de rango.")

if __name__ == '__main__':
    main()