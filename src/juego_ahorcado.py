import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """
    cadena1= cadena.lower()
    cadena2= cadena1.strip()
    cadena3= cadena2.replace('á','a').replace('é','e').replace('í','o').replace('ó','o').replace('ú','u').replace('ä','a').replace('ë','e').replace('ï','o').replace('ö','o').replace('ü','u')
    return cadena3
    # TODO: Implementa esta función (y elimina la instrucción pass)
    

def ocultar(palabra_secreta, letras_usadas=""):
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    # TODO: Implementa esta función (y elimina la instrucción pass)
    for letra in palabra_secreta:
        if letra not in letras_usadas:
            palabra_secreta = palabra_secreta.replace(letra, '_')
    return palabra_secreta


def ha_ganado(palabra_enmascarada):
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''
    # TODO: Implementa esta función (y elimina la instrucción pass)
    estado = False
    if '_' not in palabra_enmascarada:
        estado= True
    return estado


# TODO: Implementa la función mostrar_estado
def mostrar_estado(palabra_enmascarada, letras_usadas="ninguna", intentos_restantes=0):
    '''Muestra al jugador el estado actual de su partida, tanto el progreso en el juego como las letras ya usadas y los intentos restantes
    
    Parámetros:
    - palabra_enmascarada: progreso de cómo va la palabra a adivinar
    - letras_usadas: letras que ya se han usado
    - intentos_restantes: número de intentos restantes

    Devuelve:
    Estado: letras que quedan por adivinar
    Letras usadas: letras que ya se han usado
    Intentos restantes: número de intentos que le quedan
    '''
    palabra_estado = " ".join(palabra_enmascarada)
    print(f'''Estado: {palabra_estado}\nLetras usadas: {letras_usadas}\nIntentos restantes: {intentos_restantes}''')
# TODO: Implementa la función pedir_letra
def pedir_letra(letra, letras_usadas=""):
    '''Pide al jugador que introduzca una letra y se asegura de que la entrada es válida (una sola letra del alfabeto que no haya sido usada antes).

    Parámetros:
    letra: letra introducida por el jugador
    letras_usadas: letras que ya se han usado

    Devuelve:
    - letra: letra introducida por el jugador
    '''
    letra1= letra.lower()
    if len(letra1) != 1:
        print('Sólo puedes introducir una única letra')
        return None
    elif not letra1.isalpha():
        print('Debes introducir una letra')
        return None
    elif letra1 in letras_usadas:
        print('Ya has usado esta letra')
        return None
    else:
        return letra1 
# TODO: Implementa la función jugar
def jugar(palabra_secreta = elige_palabra(), num_max_intentos = 6):
    '''Recibe la palabra secreta que hay que adivinar y el número máximo de intentos e implementa toda la lógica del juego

    Parámetros:
    palabra_secreta: palabra que hay que adivinar
    num_max_intentos: número máximo de intentos

    Devuelve:
    Toda la dinámica del juego
    '''
    solucion = palabra_secreta
    palabra_secreta = normalizar(palabra_secreta)
    palabra_enmascarada = palabra_secreta
    palabra_enmascarada = ocultar(palabra_enmascarada)
    print('¡Bienvenido al juego del ahorcado!')
    letras_usadas = ''
    intentos_restantes = num_max_intentos
    while intentos_restantes > 0 and not ha_ganado(palabra_enmascarada):
        if len(letras_usadas) == 0:
            mostrar_estado(palabra_enmascarada, 'ninguna' , intentos_restantes)
        else:
            mostrar_estado(palabra_enmascarada, letras_usadas ,intentos_restantes)
        letra= input('-Introduce una letra: ')
        while not pedir_letra(letra, letras_usadas):
            letra= input('-Introduce una letra: ')
            mostrar_estado(palabra_enmascarada, letras_usadas ,intentos_restantes)
        letra = pedir_letra(letra, letras_usadas)
        letras_usadas += letra
        if letra  in palabra_secreta:
            print('La letra sí pertenece a la palabra')
            palabra_enmascarada = ocultar(palabra_secreta, letras_usadas)
                
                
        else:
            intentos_restantes -= 1
            print('La letra no está en la palabra')

    if ha_ganado(palabra_enmascarada):
        print(f'¡Has ganado! La palabra original era {palabra_secreta}.')
    else:
        print(f'Has perdido. La palabra original era {palabra_secreta}.')

# TODO: Escribe el programa principal
