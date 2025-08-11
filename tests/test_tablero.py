import unittest
from tablero import Tablero, PosOcupadaException

class TestTablero(unittest.TestCase):

    def test_posicion_ocupada(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_ficha(0, 0, "O")

    def test_ganador_columna(self):
        tablero = Tablero()
        tablero.contenedor = [
            ["X", "", ""],
            ["X", "", ""],
            ["X", "", ""]
            ]
        self.assertTrue(tablero.es_ganador("X"))

    def test_ganador_fila(self):
        tablero = Tablero()
        tablero.contenedor = [
            ["O", "O", "O"],
            ["", "", ""],
            ["", "", ""]
        ]
        self.assertTrue(tablero.es_ganador("O"))

    def test_empate(self):
        tablero = Tablero()
        tablero.contenedor = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertTrue(tablero.lleno())