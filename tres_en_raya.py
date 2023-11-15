"""
Este módulo permite llevar a cabo una partida de Tres en Raya con la IA, a través 
de diversas funciones de movimiento (ya sea del usuario o de la máquina), una
función para crear el tablero u otra para comprobar el estado del juego.
Se incluye la opción añadida de realizar un Torneo, con 3 partidas consecutivas,
y también se puede variar la dificultad de la IA (fácil/difícil).
"""

def dibujaTablero(tablero):
    
    '''
    Dibuja en la consola el tablero actual, indicando filas (1, 2, 3) y
    columnas (a, b, c).
    
            Parámetros:
                    tablero (list): una lista de listas definiendo el estado
                    del tablero de 3x3. Cada casilla puede contener uno de los
                    tres caracteres siguientes ' ', 'X', 'O'
    
            Devuelve:
                    none
    '''
    
    barra = '     +---+---+---+'
    
    # Encabezado
    print('\n')
    print('       a   b   c  ')

    # Filas
    print(barra)
    for i, c in enumerate(tablero):   
        print('   {0} | {1[0]} | {1[1]} | {1[2]} |'.format(1+i,c))
        print(barra)

    print('\n')
    

import tres_en_raya as TER   #tres_en_raya es un módulo

#%% EJERCICIO 1

# Implemente en el módulo una función denominada compruebaTablero que reciba 
# como argumento de entrada el tablero y compruebe si la partida ha terminado, 
# bien con la victoria de alguno de los jugadores, o bien con empate.

def compruebaTablero(tablero):
    for i in range(3):  
        
        # Verificamos que haya 3 en raya en las columnas
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i]!= " ":  
            return tablero[0][i]
        
        # Verificamos que haya 3 en raya en las filas
        elif tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0]!= " ": 
            return tablero[i][0]
        
        # Verificamos las diagonales
        elif tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0]!= " ": 
            return tablero[0][0]
        elif tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2]!= " ": 
            return tablero[0][2]
    
    
    # En caso de que no estén todas las casillas rellenas, aun no ha terminado la partida:
    for fila in tablero:
        for i in fila:
            if i == " ":
                return "Partida en juego"
            
    
    # Si no se cumple ninguna de las condiciones anteriores:
    return "Empate"

#%% EJERCICIO 2

# Implemente en el módulo una función denominada mueveJugador que registre un 
# movimiento del usuario. La función debe ser robusta a posibles errores 
# (casilla ocupada, casilla inexistente, etc).

def mueveJugador(tablero, jugador, fila, columna):
    # Fila y columna deben introducirse de acuerdo con el rango del tablero: 
    # (1, 2, 3) y ('a', 'b', 'c').
    # Por eso, los transformamos para que se encuentren en el rango [0,1,2]
    f = int(fila) - 1
    c = ord(columna) - ord("a")
    
    while True: 
    # Aseguramos que se introduzca el rango adecuado (matriz 3x3)
        if f not in [0,1,2]:
            print("\nLos valores introducidos no son válidos. El número de la fila debe ser 1, 2 o 3.")
            fila = int(input("\nIntroduce de nuevo la fila: "))
            f = int(fila) - 1
        elif c not in [0,1,2]:
            print("\nLos valores introducidos no son válidos. La columna debe ser a, b o c.")
            columna = input("\nIntroduce de nuevo la columna: ")
            c = ord(columna) - ord("a")
            
        elif tablero[f][c] != " ":    # Verificamos que la casilla no esté ocupada
            print("\nEsa casilla ya está ocupada. Debes elegir otra.")
            fila = int(input("Fila: "))
            columna = (input("Columna: "))
            f = int(fila) - 1
            c = ord(columna) - ord("a")
            
        else:
            # Solucionados los posibles errores, registramos el movimiento
            tablero[f][c] = jugador
            break
      
    # Devolvemos cómo ha quedado el tablero tras el movimiento
    return TER.dibujaTablero(tablero)

#%% EJERCICIO 3

# Implemente en el módulo una función denominada mueveIA que realice un 
# movimiento por parte de la IA, que se realizará escogiendo de forma aleatoria 
# una de las casillas vacías.

import random

def mueveIA(tablero, IA):   # IA hace referencia a la figura (X, O) con la que jugará la IA
    # Creamos una lista para incluir todas las casillas vacías
    vacias = []
    
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                vacias.append((fila, columna))
                
    # Comprobamos que haya casillas vacías para hacer el movimiento
    if vacias:
       fila, columna = random.choice(vacias)
       tablero[fila][columna] = IA
       
       return TER.dibujaTablero(tablero)
   
    else:
        print("\nNo hay ninguna casilla vacía, así que no se pueden hacer más movimientos.")

#%% EJERCICIO 4

# Implemente en el módulo una función denominada nuevoJuego, que gestione una 
# partida completa del usuario contra la IA. La IA empieza siempre moviendo.

def nuevoJuego(jugador):   # El usuario elige con qué figura quiere jugar
    tablero = [[' ',' ',' '],    # Creamos un tablero inicial vacío
               [' ',' ',' '],
               [' ',' ',' ']]
    
    # La IA usará la figura que no haya elegido el usuario
    if jugador == "X":
        IA = "O"
        print("\nComienza la partida.")
    elif jugador == "O":
        IA = "X"
        print("\nComienza la partida.")
    else:   # ROBUSTEZ, por si no se introduce ninguna de las dos figuras correctas
        print("Debes introducir 'O' o 'X' para poder jugar.")
      
        
    while jugador in ["X", "O"]:
        
        print("\n\n\nTurno de la IA.")
        TER.mueveIA(tablero, IA)
        
        
        # Comprobamos la situación del juego:
        
        situacion = TER.compruebaTablero(tablero)
        
        if situacion == jugador:
            print("¡Enhorabuena! Has ganado la partida.")
            return situacion
            break
        elif situacion == IA:
            print("La IA ha ganado la partida.")
            return situacion
            break
        elif situacion == "Empate":
            print("¡Empate!")
            return situacion
            break
        
        # Si la partida no ha terminado tras esta comprobación, es el turno del jugador. 
        
        print("\n\n\nEs tu turno.")  
        
        while True:
            fila = input("\nIntroduce la fila donde deseas mover a continuación (1, 2, 3): ")
        # Facilitamos la interacción con el jugador, transformando el nº dado por el usuario en el nº de la posición correspondiente
            if fila in ["1", "2", "3"]:
                break
            else:
                print("\nEl valor introducido debe estar en el rango (1, 2, 3).\nVuelve a intentarlo.")
            
        while True:
            columna = input("\nIntroduce la columna donde deseas mover a continuación (a, b, c): ")
        # Transformamos ahora la letra de cada columna en la posición que le corresponde:
            if columna in ["a", "b", "c"]:
                break
            else:
                print("\nEl valor introducido debe estar en el rango (a, b, c).\nVuelve a intentarlo.")
            
        
        TER.mueveJugador(tablero, jugador, fila, columna)
        
        # Volvemos a comprobar la situación del juego:
        
        situacion = TER.compruebaTablero(tablero)
        
        if situacion == jugador:
            print("\n¡Enhorabuena! Has ganado la partida.")
            return situacion
            break
        elif situacion == IA:
            print("\nLa IA ha ganado la partida.")
            return situacion
            break
        elif situacion == "Empate":
            print("\n¡Empate!")
            return situacion
            print(situacion)
            break
        
#%% EJERCICIO 5

# Implemente en el módulo una función denominada nuevoTorneo, que gestione un 
# torneo compuesto por 3 partidas consecutivas contra la IA. La función determinará 
# el ganador del torneo y lo indicará. En caso de empate, lanzará una partida 
# adicional de desempate.

def nuevoTorneo(jugador):
    
    while jugador not in ["X", "O"]:
        print("\nDebes introducir 'O' o 'X' para poder jugar.")
        jugador = input("Introduce de nuevo la figura que deseas (sin comillas): ").upper()
    
    print("\nBienvenido al Torneo.")
    
    # Inicializamos contadores de victoria
    gana_jugador = 0 
    gana_IA = 0
    
    for partida in range(3):
        print("\n\n\nPARTIDA Nº " + str(partida + 1))
        resultado = TER.nuevoJuego(jugador)

# Según el resultado que arroje nuevoJuego, contabilizamos la victoria:
        if resultado == jugador:
            gana_jugador += 1
            print("Te llevas un punto.")
        elif resultado == "Empate":
            print("El marcador no se modifica.")
        else: 
            gana_IA += 1
            print("El punto se lo lleva la IA.")

# Mostramos el marcador tras cada partida
        print("\nMarcador: Jugador", gana_jugador, "- IA", gana_IA)

    # Terminadas las 3 partidas, determinamos el ganador
    if gana_jugador > gana_IA:
        print("\nHas ganado el torneo.\n¡Felicidades!")
    elif gana_jugador < gana_IA:
        print("\nLa IA ha ganado el torneo. ¡Suerte para la próxima!")
    else:
        print("\n\nEl torneo ha resultado en empate. \nJugaremos una partida adicional para desempatar.")
        
# En caso de empate, jugamos partida de desempate:
        desempate = TER.nuevoJuego(jugador)
        
        if desempate == jugador:
            print("\nAl haber ganado la partida de desempate, ganas el torneo.\n¡Felicidades!")
        elif desempate == "Empate":
            print("\nEsta partida ha resultado también en empate, así que finalizamos el torneo con dicho resultado. Hasta la próxima.")
        else:
            print("\nLa IA es la vencedera del torneo. ¡Suerte para la próxima!")
            
#%% EJERCICIO 6

# Cree una nueva función de movimiento de la IA denominada mueveIA2, en la que 
# se reciba, además del tablero, un segundo argumento dificultad, que podrá 
# tomar los valores ‘fácil’ o ‘difícil’, que modificarán el comportamiento de la IA

def mueveIA2(tablero, IA, dificultad):
# Al igual que en la función mueveIA, IA se refiere a la figura con la que jugará la IA.

    from unidecode import unidecode
    # Nos aseguramos que la palabra está en minúsculas y sin tildes para que se pueda 
    # escribir de diferentes maneras por el usuario sin problema:
    dif = unidecode(dificultad).lower()  
   
    while IA not in ["O", "X"]:
        print("\nFigura no reconocida. Debes utilizar 'O' o 'X'")
        IA = input("Introduce de nuevo la figura que deseas (sin comillas): ").upper()
        
    # Para aplicar el modo difícil posteriormente, necesitamos conocer la figura con la que juega el usuario
    if IA == "X":    
        jugador = "O"
    elif IA == "O":
        jugador = "X"
        
    vacias = []
        
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                vacias.append((fila, columna))
                    
    # Comprobamos que haya casillas vacías para hacer el movimiento
    if vacias:
        if dif == "facil":  # En este caso, actúa igual que la función mueveIA
            fila, columna = random.choice(vacias)   # Ya habíamos importado random previamente
            
        elif dif == "dificil": 
            
            # Para aplicar el modo difícil, comprobamos si el usuario ganaría 
            # en la siguiente jugada, y en ese caso lo bloqueamos
           
            bloqueo = []
            
            for fila, columna in vacias:
               tablero[fila][columna] = jugador   #emulamos la jugada del usuario
               if compruebaTablero(tablero) == jugador:
                  bloqueo.append((fila,columna))  # Incluimos en la lista todos los movimientos que permitan bloquear al usuario
               tablero[fila][columna] = " "   # Deshacemos ese movimiento ficticio
               
               
            # Asimismo, la IA comprueba si podría ganar en el siguiente movimiento:
            ganar = []
            
            for fila, columna in vacias:
                tablero[fila][columna] = IA
                if compruebaTablero(tablero) == IA:
                    ganar.append((fila,columna))
                tablero[fila][columna] = " "  # Deshacemos el movimiento
            
            
            if bloqueo or ganar:
                if ganar:  
                # Si existen tanto movimientos de bloqueo como movimientos para ganar, realiza antes este último
                    fila, columna = random.choice(ganar)
                else:
                    fila, columna = random.choice(bloqueo)
                
            else:
            # Si no se cumplen ninguno de los casos anteriores (bloquear o ganar),
            # el movimiento es aleatorio
                fila, columna = random.choice(vacias)
                   
        else:
            print("\nNo se ha identificado ninguno de los dos modos de dificultad (Fácil/Difícil).\nPor tanto, aplicamos modo fácil por defecto.")
            fila, columna = random.choice(vacias)
    
    
    # La IA lleva a cabo el movimiento
    tablero[fila][columna] = IA
    
    return TER.dibujaTablero(tablero)


#%%   EXTRA

def nuevoJuego2(jugador, dificultad):   
    tablero = [[' ',' ',' '],    
               [' ',' ',' '],
               [' ',' ',' ']]
    
    # La IA usará la figura que no haya elegido el usuario
    if jugador == "X":
        IA = "O"
        print("\nComienza la partida.")
    elif jugador == "O":
        IA = "X"
        print("\nComienza la partida.")
    else:   # ROBUSTEZ, por si no se introduce ninguna de las dos figuras correctas
        print("Debes introducir 'O' o 'X' para poder jugar.")
      
        
    while jugador in ["X", "O"]:
        
        print("\n\n\nTurno de la IA.")
        TER.mueveIA2(tablero, IA, dificultad)
        
        
        # Comprobamos la situación del juego:
        
        situacion = TER.compruebaTablero(tablero)
        
        if situacion == jugador:
            print("¡Enhorabuena! Has ganado la partida.")
            return situacion
            break
        elif situacion == IA:
            print("La IA ha ganado la partida.")
            return situacion
            break
        elif situacion == "Empate":
            print("¡Empate!")
            return situacion
            break
        
        # Si la partida no ha terminado tras esta comprobación, es el turno del jugador. 
        
        print("\n\n\nEs tu turno.")  
        
        while True:
            fila = input("\nIntroduce la fila donde deseas mover a continuación (1, 2, 3): ")
        # Facilitamos la interacción con el jugador, transformando el nº dado por el usuario en el nº de la posición correspondiente
            if fila in ["1", "2", "3"]:
                break
            else:
                print("\nEl valor introducido debe estar en el rango (1, 2, 3).\nVuelve a intentarlo.")
            
        while True:
            columna = input("\nIntroduce la columna donde deseas mover a continuación (a, b, c): ")
        # Transformamos ahora la letra de cada columna en la posición que le corresponde:
            if columna in ["a", "b", "c"]:
                break
            else:
                print("\nEl valor introducido debe estar en el rango (a, b, c).\nVuelve a intentarlo.")
            
        
        TER.mueveJugador(tablero, jugador, fila, columna)
        
        # Volvemos a comprobar la situación del juego:
        
        situacion = TER.compruebaTablero(tablero)
        
        if situacion == jugador:
            print("\n¡Enhorabuena! Has ganado la partida.")
            return situacion
            break
        elif situacion == IA:
            print("\nLa IA ha ganado la partida.")
            return situacion
            break
        elif situacion == "Empate":
            print("\n¡Empate!")
            return situacion
            print(situacion)
            break

#%%  EXTRA

def nuevoTorneo2(jugador, dificultad):
    
    while jugador not in ["X", "O"]:
        print("\nDebes introducir 'O' o 'X' para poder jugar.")
        jugador = input("Introduce de nuevo la figura que deseas (sin comillas): ").upper()
    
    print("\nBienvenido al Torneo.")
    
    # Inicializamos contadores de victoria
    gana_jugador = 0 
    gana_IA = 0
    
    for partida in range(3):
        print("\n\n\nPARTIDA Nº " + str(partida + 1))
        resultado = TER.nuevoJuego2(jugador, dificultad)

# Según el resultado que arroje nuevoJuego, contabilizamos la victoria:
        if resultado == jugador:
            gana_jugador += 1
            print("Te llevas un punto.")
        elif resultado == "Empate":
            print("El marcador no se modifica.")
        else: 
            gana_IA += 1
            print("El punto se lo lleva la IA.")

# Mostramos el marcador tras cada partida
        print("\nMarcador: Jugador", gana_jugador, "- IA", gana_IA)

    # Terminadas las 3 partidas, determinamos el ganador
    if gana_jugador > gana_IA:
        print("\nHas ganado el torneo.\n¡Felicidades!")
    elif gana_jugador < gana_IA:
        print("\nLa IA ha ganado el torneo. ¡Suerte para la próxima!")
    else:
        print("\n\nEl torneo ha resultado en empate. \nJugaremos una partida adicional para desempatar.")
        
# En caso de empate, jugamos partida de desempate:
        desempate = TER.nuevoJuego2(jugador, dificultad)
        
        if desempate == jugador:
            print("\nAl haber ganado la partida de desempate, ganas el torneo.\n¡Felicidades!")
        elif desempate == "Empate":
            print("\nEsta partida ha resultado también en empate, así que finalizamos el torneo con dicho resultado. Hasta la próxima.")
        else:
            print("\nLa IA es la vencedera del torneo. ¡Suerte para la próxima!")
