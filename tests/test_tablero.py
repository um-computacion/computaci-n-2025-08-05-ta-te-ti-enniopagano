import unittest
from src.tablero import *

class TestTablero(unittest.TestCase):
    def setUp(self):
        self.tablero = Tablero()

    def test_set_chip(self):
        self.tablero.set_chip(1, 2, 'X')
        self.tablero.set_chip(2, 3, 'X')
        self.tablero.set_chip(3, 3, 'O')
        self.assertEqual(self.tablero.contenedor[0][1], 'X')
        self.assertEqual(self.tablero.contenedor[1][2], 'X')
        self.assertEqual(self.tablero.contenedor[2][2], 'O')

    def test_set_chip_edge_cases(self):
        with self.assertRaises(IndexError):
            self.tablero.set_chip(100, 2, 'X')
            self.tablero.set_chip(1, -50, 'X')
        with self.assertRaises(TypeError):
            self.tablero.set_chip('saas', 2, 'X')
            self.tablero.set_chip(1, 'leel', 'X')


    def test_posicion_ocupada(self):
        self.tablero.set_chip(1, 1, 'X')
        self.tablero.set_chip(2, 2, 'O')
        with self.assertRaises(PosOcupadaException):
            self.tablero.set_chip(1, 1, 'X')
            self.tablero.set_chip(2, 2, 'O')

    def test_condicion_victoria_horizontal(self):
        self.tablero.set_chip(1, 1, 'X')
        self.tablero.set_chip(1, 2, 'X')
        self.tablero.set_chip(1, 3, 'X')
        self.assertEqual(self.tablero.condicion_victoria(), True)

    def test_condicion_victoria_vertical(self):
        self.tablero.set_chip(1, 1, 'X')
        self.tablero.set_chip(2, 1, 'X')
        self.tablero.set_chip(3, 1, 'X')
        self.assertEqual(self.tablero.condicion_victoria(), True)

    def test_condicion_victoria_diagonal_1(self):
        self.tablero.set_chip(1, 1, 'X')
        self.tablero.set_chip(2, 2, 'X')
        self.tablero.set_chip(3, 3, 'X')
        self.assertEqual(self.tablero.condicion_victoria(), True)

    def test_condicion_victoria_diagonal_2(self):
        self.tablero.set_chip(1, 3, 'X')
        self.tablero.set_chip(2, 2, 'X')
        self.tablero.set_chip(3, 1, 'X')
        self.assertEqual(self.tablero.condicion_victoria(), True)

    def test_condicion_empate(self):
        empate = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        for i in range(3):
            for s in range(3):  
                self.tablero.set_chip(i, s, empate[i][s])
        self.assertEqual(self.tablero.condicion_empate(), True)

if __name__ == '__main__':
    unittest.main()