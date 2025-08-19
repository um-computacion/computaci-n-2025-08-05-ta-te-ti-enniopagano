import unittest
from src.tateti import Tateti
from src.jugador import Jugador

class TestTateti(unittest.TestCase):
    def setUp(self):
        self.juego = Tateti()

    def test_crear_jug(self):
        nombre = 'Player'
        jugador = self.juego.crear_jug(nombre, 'X')

        self.assertIsInstance(jugador, Jugador)
        self.assertEqual(jugador.nombre, nombre)
        self.assertEqual(jugador.ficha, 'X')

    def test_set_turn(self):
        jugador = self.juego.crear_jug('Player', 'X')
        self.juego.set_turn(jugador)
        self.assertEqual(self.juego.turno, jugador.ficha)

    def test_change_turn(self):
        self.juego.turno = 'X'
        self.juego.change_turn()
        self.assertEqual(self.juego.turno, 'O')
        self.juego.change_turn()
        self.assertEqual(self.juego.turno, 'X')

    def test_check_winner(self):
        jugador = self.juego.crear_jug('Player', 'X')
        jugador2 = self.juego.crear_jug('Player2', 'O')
        self.juego.turno = 'X'
        self.assertEqual(self.juego.check_winner(jugador), True)
        self.assertEqual(self.juego.check_winner(jugador2), None)
        


if __name__ == '__main__':
    unittest.main()