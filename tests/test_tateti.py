import unittest
from src.tateti import Tateti
from src.jugador import Jugador
from src.tablero import PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.j1 = Jugador("Jugador1", "X")
        self.j2 = Jugador("Jugador2", "O")
        self.juego = Tateti(self.j1, self.j2)

    def test_cambio_turno(self):
        self.juego.ocupar_casilla(1, 1)
        self.assertEqual(self.juego.jugador_actual().ficha, "O")

    def test_ganador(self):
        self.juego.tablero.contenedor = [
            ["X", "X", ""],
            ["", "O", ""], 
            ["", "", "O"] 
        ]
        resultado = self.juego.ocupar_casilla(0, 2)
        self.assertTrue(resultado)

    def test_empate(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", ""]
        ]
        resultado = self.juego.ocupar_casilla(2, 2)
        self.assertTrue(resultado)

    def test_posicion_ocupada(self):
        self.juego.ocupar_casilla(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_casilla(0, 0)