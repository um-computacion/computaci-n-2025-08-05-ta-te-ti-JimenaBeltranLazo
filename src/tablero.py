class PosOcupadaException(Exception):
    pass

class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def poner_ficha(self, fila, columna, ficha):
        if self.contenedor[fila][columna] == "":
            self.contenedor[fila][columna] = ficha
        else:
            raise PosOcupadaException("¡Posición ocupada!")
    
    def mostrar_tablero(self):
        for fila in self.contenedor:
            print(" | ".join(columna if columna != "" else " " for columna in fila))
            print("-" * 9)

    def hay_ganador(self, ficha):
        # Filas
        for fila in self.contenedor:
            if fila[0] == ficha and fila[1] == ficha and fila[2] == ficha:
                return True
        # Columnas
        for columna in range(3):
            if self.contenedor[0][columna] == ficha and \
            self.contenedor[1][columna] == ficha and \
            self.contenedor[2][columna] == ficha:
                return True
        # Diagonales
        if self.contenedor[0][0] == ficha and \
        self.contenedor[1][1] == ficha and \
        self.contenedor[2][2] == ficha:
            return True
        if self.contenedor[0][2] == ficha and \
        self.contenedor[1][1] == ficha and \
        self.contenedor[2][0] == ficha:
            return True
        return False

    def contenedor_lleno(self):
        for fila in range(3):
            for columna in range(3):
                if self.contenedor[fila][columna] == "":
                    return False
        return True