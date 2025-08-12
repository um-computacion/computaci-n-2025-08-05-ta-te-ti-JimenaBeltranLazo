import unittest
from src.tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):

    def test_posicion_ocupada(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_ficha(0, 0, "O")

    def test_ganador_columna(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 1, "O")
        tablero.poner_ficha(1, 1, "O")
        tablero.poner_ficha(2, 1, "O")
        self.assertTrue(tablero.hay_ganador("O"))

    def test_ganador_fila(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        tablero.poner_ficha(0, 1, "X")
        tablero.poner_ficha(0, 2, "X")
        self.assertTrue(tablero.hay_ganador("X"))

    def test_ganador_diagonal(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        tablero.poner_ficha(1, 1, "X")
        tablero.poner_ficha(2, 2, "X")
        self.assertTrue(tablero.hay_ganador("X"))

    def test_empate(self):
        tablero = Tablero()
        fichas = ["X", "O"]
        f = 0
        for i in range(3):
            for j in range(3):
                tablero.poner_ficha(i, j, fichas[f])
                f = 1 - f
        self.assertTrue(tablero.contenedor_lleno())