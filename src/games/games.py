class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        
        opciones = ["piedra", "papel", "tijera"]
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        
        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"
        
        if jugador1 == jugador2:
            return "empate"
        
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "papel" and jugador2 == "piedra") or \
           (jugador1 == "tijera" and jugador2 == "papel"):
            return "jugador1"
        else:
            return "jugador2"   

    def adivinar_numero_pista(self, numero_secreto, intento):
        
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"
    
    def ta_te_ti_ganador(self, tablero):
        
        
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
             return fila[0]

         
        for col in range(3):
         if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
            return tablero[0][col]

        
        hay_espacios = False
        for fila in tablero:
         if " " in fila:
            hay_espacios = True

        
        if not hay_espacios:

            if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
                return tablero[0][0]

            if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
                return tablero[0][2]

            return "empate"

        return "continua"   
    
    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
    
        import random
        return [random.choice(colores_disponibles) for _ in range(longitud)]
    
    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
       
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False

        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        
        if desde_fila == hasta_fila:

            paso = 1 if hasta_col > desde_col else -1

            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False

            return True

       
        if desde_col == hasta_col:

            paso = 1 if hasta_fila > desde_fila else -1

            for f in range(desde_fila + paso, hasta_fila, paso):
                if tablero[f][desde_col] != " ":
                    return False

            return True

        