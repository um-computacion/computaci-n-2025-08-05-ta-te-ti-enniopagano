class PosOcupadaException(Exception):
    ...


class Tablero:
    def __init__(self):
        self.contenedor = [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]



    def set_chip(self, fil, col, ficha):
        fil -= 1
        col -= 1
        if self.contenedor[fil][col] == '':
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posicion ocupada!")
        
    def condicion_victoria(self):    
        for fila in self.contenedor:
            if all(celda == 'X' for celda in fila) or all(celda == 'O' for celda in fila):
                return True

        for col in range(3):
            if all(self.contenedor[fil][col] == 'X' for fil in range(3)) or all(self.contenedor[fil][col] == 'O' for fil in range(3)):
                return True

        if all(self.contenedor[i][i] == 'X' for i in range(3)) or all(self.contenedor[i][i] == 'O' for i in range(3)):
            return True
        
        if all(self.contenedor[i][2 - i] == 'X' for i in range(3)) or all(self.contenedor[i][2 - i] == 'O' for i in range(3)):
            return True
        
    def condicion_empate(self):
        return all(celda != '' for fila in self.contenedor for celda in fila)
    

    def __str__(self):
        return f"{self.contenedor}"