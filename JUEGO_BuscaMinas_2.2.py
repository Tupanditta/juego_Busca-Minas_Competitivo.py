####################################################

# Autor: Ander Lifeng Sola López
# Identificador UPNA: sola.180528

# Grado: Ingeniería Informática
# Asignatura: determina la asignatura
# Centro: Universidad Pública de Navarra; Campus de Arrosadía

# Fecha: Sun Nov  2 07:44:51 2025
# Archivo: JUEGO_BuscaMinas_2.2.py
# Lenguaje: python
# Descripción: Breve descripción de este proyecto/archivo.

####################################################



#JUEGO 1: Busca Minas

#Presentación del juego
print('Dos jugadores comienzan con 100 puntos cada uno')
print('Cada ronda se obtienen dos números [Suma, Resta]')
print('El valor tanto de [suma] como de [resta] será uno aleatorio en el intervalo de 5-100')
print('Introduciendo las coordenadas de una casilla [fila, columna], si en ella se encuentra una mina *,')
print('el jugador conseguirá tantos puntos como [suma] y el otro jugador perderá tantos puntos como [resta]')
print('Pierde el primero en quedarse sin puntos, o cuando uno de ellos encuentre todas las minas,')
print('quien tenga menos puntos.')

print() #Visual y estilo

#LIBRERIAS
import random

#FUNCIONES
def crear_tabla(dificultad, cantidad): 
    tabla = []
    posicion_minas = []
    numero_minas = cantidad
    N = dificultad
    
    for i in range(N):
        fila_tabla = []
        for j in range(N):
            fila_tabla.append('0')
        tabla.append(fila_tabla)
    
    for i in range(numero_minas):
        mina_in = True
        
        while mina_in:
            fila_posicion = random.randint(0, N-1)
            columna_posicion = random.randint(0, N-1)
            if [fila_posicion, columna_posicion] not in posicion_minas:
                mina_in = False
                posicion_minas.append([fila_posicion, columna_posicion])
            
        tabla[fila_posicion][columna_posicion] = '*'
            
    return tabla

def mostrar_juego(tabla_m_1, tabla_ver_1, puntos_ver_1, tabla_m_2, tabla_ver_2, puntos_ver_2, tamaño):
    
    #Listas
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    #variables
    espacios_J = ((tamaño-3)*3)+8
    espacios_P = (((tamaño-3)*3)+10)
    if len(puntos_ver_1) != 0: 
        espacios_P = (((10-3)*3)+10)
        for elemento in puntos_ver_1:
            espacios_P -= len(str(elemento))
        espacios_P = espacios_P - ((len(puntos_ver_1)//2)+4)
        
    #Cuerpo principal
    print() #estilo y visual
    print() #estilo y visual
    
        #Linea puntos y jugador
    print('    ', 'JUGADOR 1', end=' '*espacios_J) #El end debe ir acorde al número de columnas
    print('JUGADOR 2')
    print('     Puntos:', *puntos_ver_1, end=' '*espacios_P) #El end debe ir acorde al número de columnas
    print('Puntos:', *puntos_ver_2)
    
        #Linea indice columnas
    print('       ', end='') #estilo y visual
    for numero in range(tamaño):
        print(numero, end='  ')
        
    print('       ', end='') #estilo y visual: los espacios aquí no importan
    for numero in range(tamaño):
        print(numero, end='  ')
    print()
    
        #Lineas filas
    for fila in range(len(tabla_m_1)):
            #Linea jugador 1
        print('    ', abc[fila], end='  ')
        for columna in range(len(tabla_m_1)):
            if [fila, columna] in tabla_ver_1:
                print(tabla_m_1[fila][columna], end='  ')
            else: 
                print('_', end='  ') 
                
            #Linea jugador 2
        print('    ', abc[fila], end='  ')
        for columna in range(len(tabla_m_2)):
            if [fila, columna] in tabla_ver_2:
                print(tabla_m_2[fila][columna], end='  ')
            else: 
                print('_', end='  ')
        
        print()
        
    print() #estilo y visual

def dado_puntos():
    intervalo_suma = random.randint(1, 22)
    intervalo_resta = random.randint(1, 22)
    
    if intervalo_suma <= 10:
        suma = 5 
    elif intervalo_suma <= 15:
        suma = 10
    elif intervalo_suma <= 18:
        suma = 20
    elif intervalo_suma <= 20:
        suma = 30
    else:
        suma = 100
    
    if intervalo_resta <= 10:
        resta = 5 
    elif intervalo_resta <= 15:
        resta = 10
    elif intervalo_resta <= 18:
        resta = 20
    elif intervalo_resta <= 20:
        resta = 30
    else:
        resta = 100
    
    print('Suma: {}   Resta: {}'.format(suma, resta))
    
    return [suma, resta]

def cambio_letra(letra):
    if letra == 'a':
        fila_n = 0
    elif letra == 'b':
        fila_n = 1
    elif letra == 'c':
        fila_n = 2
    elif letra == 'd':
        fila_n = 3
    elif letra == 'e':
        fila_n = 4
    elif letra == 'f':
        fila_n = 5
    elif letra == 'g':
        fila_n = +6
    elif letra == 'h':
        fila_n = 7
    elif letra == 'i':
        fila_n = 8
    elif letra == 'j':
        fila_n = 9
        
    return fila_n

#VARIABLES
puntos_ver_1 = []
puntos_ver_2 = []

#LISTAS
tabla_posiciones_1 = []
tabla_posiciones_2 = []
minas_encontradas_1 = 0
minas_encontradas_2 = 0
tabla_puntos_1 = []
tabla_puntos_2 = []

#INICIO
print()
tabla_tamaño = int(input('DIFICULTAD escoga el tamaño NxN de la tabla de juego:  '))
numero_minas = int(input('Escoga el número de minas en el tablero de juego10: '))

        #Crear tablas de juego mediante funciones
tabla_juego_1 = crear_tabla(tabla_tamaño, numero_minas) #llamar a la función
tabla_juego_2 = crear_tabla(tabla_tamaño, numero_minas) #llamar a la función

mostrar_juego(tabla_juego_1, tabla_posiciones_1, puntos_ver_1, tabla_juego_2, tabla_posiciones_2, puntos_ver_2, tabla_tamaño) #llamar a la función

#MEDIO JUEGO
    #Otras Variables
puntos_1 = 100
puntos_2 = 100
while (puntos_1 > 0) and (puntos_2 > 0) and minas_encontradas_1 != numero_minas and minas_encontradas_2 != numero_minas:
    #Listas
    puntos_ver_1 = [puntos_1]
    puntos_ver_2 = [puntos_2]
    
    tabla_puntos = dado_puntos()
    
    #Jugador 1
    casilla_nueva_1 = True
    while casilla_nueva_1: #Controlar si la casilla introducida ya se había introducido antes
        casilla_1 = input('JUGADOR 1: Introduza una casilla en formato [fila columna]: ').split()
        
        casilla_1[0] = cambio_letra(casilla_1[0])
        casilla_1[1] = int(casilla_1[1])
        
        if casilla_1 not in tabla_posiciones_1:
            casilla_nueva_1 = False #La casilla introducida SÍ es NUEVA
        else:
            print('La casilla [{}, {}] ya se ha introducido antes, introduzca una casilla nueva'.format(casilla_1[0], casilla_1[1]))
            
    tabla_posiciones_1.append(casilla_1)
    
    if tabla_juego_1[casilla_1[0]][casilla_1[1]] == '*': #Contador de puntos
        puntos_ver_1.append('+')
        puntos_ver_1.append(tabla_puntos[0])
        puntos_ver_2.append('-')
        puntos_ver_2.append(tabla_puntos[1])
        puntos_1 += tabla_puntos[0]
        puntos_2 -= tabla_puntos[1]
        minas_encontradas_1 += 1
    else:
        puntos_ver_1.append('+')
        puntos_ver_1.append(0)
        puntos_ver_2.append('-')
        puntos_ver_2.append(0)
        
    #Jugador 2
    casilla_nueva_2 = True
    while casilla_nueva_2: #Controlar si la casilla introducida ya se había introducido antes
        casilla_2 = input('JUGADOR 2: Introduza una casilla en formato [fila,columna]: ').split()
        
        casilla_2[0] = cambio_letra(casilla_2[0])
        casilla_2[1] = int(casilla_2[1])
        
        if casilla_2 not in tabla_posiciones_2:
            casilla_nueva_2 = False #La casilla introducida SÍ es NUEVA
        else:
            print('La casilla [{}, {}] ya se ha introducido antes, introduzca una casilla nueva'.format(casilla_2[0], casilla_2[1]))
    
    tabla_posiciones_2.append(casilla_2)
    
    if tabla_juego_2[casilla_2[0]][casilla_2[1]] == '*': #Contador de puntos
        puntos_ver_2.append('+')
        puntos_ver_2.append(tabla_puntos[0])
        puntos_ver_1.append('-')
        puntos_ver_1.append(tabla_puntos[1])
        puntos_2 += tabla_puntos[0]
        puntos_1 -= tabla_puntos[1]
        minas_encontradas_2 += 1
        
    else:
        puntos_ver_2.append('+')
        puntos_ver_2.append(0)
        puntos_ver_1.append('-')
        puntos_ver_1.append(0)
    
    puntos_ver_1.append('=')
    puntos_ver_1.append(puntos_1)
    puntos_ver_2.append('=')
    puntos_ver_2.append(puntos_2)
    
    #Mostar Juego
    mostrar_juego(tabla_juego_1, tabla_posiciones_1, puntos_ver_1, tabla_juego_2, tabla_posiciones_2, puntos_ver_2, tabla_tamaño) #llamar a la función

    
#FINAL
if puntos_1 > puntos_2:
    print('FELICIDADES JUGADOR 1, HAS GANADO')
else:
    print('FELICIDADES JUGADOR 2, HAS GANADO')

