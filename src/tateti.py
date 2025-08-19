from tablero import Tablero
from jugador import Jugador

class Tateti:
    def __init__(self):
        self.turno = ''
        self.tablero = Tablero()


    def set_turn(self, Jugador):
        self.turno = Jugador.ficha

    def change_turn(self):
        if self.turno == 'X':
            self.turno = 'O'
        else:
            self.turno = 'X'

    def pick(self, fil, col):
        self.tablero.set_chip(fil, col, self.turno)

    def check_win(self):
        return self.tablero.condicion_victoria()
    
    def check_tie(self):
        return self.tablero.condicion_empate()
    
    def check_winner(self, Jugador):
        if Jugador.ficha == self.turno:
            return True

    def crear_jug(self, nombre, ficha):
        return Jugador(nombre, ficha)


    