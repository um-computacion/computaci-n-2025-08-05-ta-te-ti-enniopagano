from tateti import Tateti
from tablero import PosOcupadaException

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()
    nj1 = str(input('Nombre de jugador 1: '))
    nj2 = str(input('Nombre de jugador 2: '))
    while True:
        try:
            fj1 = int(input('Ficha de jugador 1 (1: X | 2: O):\n'))
            if fj1 in [1, 2]:
                if fj1 == 1:
                    j1 = juego.crear_jug(nj1, 'X')
                    j2 = juego.crear_jug(nj2, 'O')
                    juego.set_turn(j1)
                else:
                    j1 = juego.crear_jug(nj1, 'O')
                    j2 = juego.crear_jug(nj2, 'X')
                    juego.set_turn(j1)
                break
            else:
                print('Ingresa 1 o 2 para elegir tu ficha')
        except Exception as e:
            print('Elija numero 1 para "X" y numero 2 para "O"')
    contador = 2
    while True:
        if juego.check_tie():
                break
        print("Tablero: ")
        for fila in juego.tablero.contenedor:
            print(fila)
        if contador % 2 == 0:
            print(f"Turno de {j1}: ")
        else:
            print(f"Turno de {j2}: ")
        contador += 1
        try:
            fil = int(input("Ingrese fila (1,2 o 3): "))
            col = int(input("Ingrese columna (1,2 o 3): "))
            juego.pick(fil, col)
            if juego.check_win():
                break 
            juego.change_turn()
        except PosOcupadaException:
            print(e)
            contador -= 1
        except IndexError:
            print('Los números de fila y columna deben ser 1, 2 o 3')
            contador -= 1
        except ValueError:
            print('Los NÚMEROS de fila y columna deben ser 1, 2 o 3')
            contador -= 1

    for fila in juego.tablero.contenedor:
            print(fila)
    if juego.check_tie():
        print('Empate')
    else:
        if juego.check_winner(j1):
            print(f'{j1} es el ganador!')
        else:
            print(f'{j2} es el ganador!')


if __name__ == '__main__':
    main()