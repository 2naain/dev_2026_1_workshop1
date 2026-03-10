import random
class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        
        j1 = jugador1.lower()
        j2 = jugador2.lower()

        if j1 == j2:
            return "empate"

        victorias = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }

        return "jugador1" if victorias[j1] == j2 else "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        return "muy alto" if intento > numero_secreto else "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        lineas = (
            [[tablero[i][j] for j in range(3)] for i in range(3)] +  
            [[tablero[i][j] for i in range(3)] for j in range(3)] + 
            [[tablero[i][i] for i in range(3)]] +                    
            [[tablero[i][2 - i] for i in range(3)]]                 
        )

        for linea in lineas:
            if linea[0] != " " and all(c == linea[0] for c in linea):
                return linea[0]

        if all(tablero[i][j] != " " for i in range(3) for j in range(3)):
            return "empate"

        return "continua"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

      
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for col in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][col] != " ":
                    return False
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for fila in range(desde_fila + paso, hasta_fila, paso):
                if tablero[fila][desde_col] != " ":
                    return False

        return True