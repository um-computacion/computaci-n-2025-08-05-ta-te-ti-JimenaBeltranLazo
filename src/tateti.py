from src.tablero import Tablero

class Tateti:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.turno = jugador1
        self.tablero = Tablero()

    def jugador_actual(self):
        return self.turno

    def ocupar_casilla(self, fila, columna):
        self.tablero.poner_ficha(fila, columna, self.turno.ficha)

        # Verificar ganador
        if self.tablero.hay_ganador(self.turno.ficha):
            print(f"¡Felicidades {self.turno.nombre}! Has ganado el juego.")
            return True

        # Verificar empate
        if self.tablero.contenedor_lleno():
            print("¡Es un empate! No hay más movimientos posibles.")
            return True

        # Cambiar turno
        self.turno = self.jugador2 if self.turno == self.jugador1 else self.jugador1
        return False
