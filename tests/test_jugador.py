import unittest
from src.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_ingreso_datos(self):
        jugador = Jugador("Lucía", "X")
        self.assertEqual(jugador.nombre, "Lucía")
        self.assertEqual(jugador.ficha, "X")