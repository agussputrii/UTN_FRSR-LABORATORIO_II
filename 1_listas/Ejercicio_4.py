seleccion_argentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
}
# Funcion para mostrar los jugadores de la seleccion Argentina
def mostrar_jugadores():
    for numero, datos in seleccion_argentina.items():
        print(f'Numero: {numero}')
        for clave, valor in datos.items():
            print(f'{clave}: {valor}')
        print('')
# Funcion para agregar jugadores a la lista seleccion_argentina
def agregar_jugador(numero, nombre, edad, altura, precio, posicion):
    seleccion_argentina[numero] = {'Nombre': nombre, 'Edad': edad, 'Altura': altura, 'Precio': precio, 'Posicion': posicion}


def main():
    mostrar_jugadores()
    print('Agregando jugadores...')
    agregar_jugador(9, 'Gonzalo Higuain', 32, 1.80, '15 Millones', 'Media Punta')
    agregar_jugador(3, 'Nicolas Tagliafico', 30, 1.75, '5 Millones', 'Lateral Izquierdo')
    agregar_jugador(20, 'Giovani Lo Celso', 27, 1.70, '20 Millones', 'Media Punta')
    agregar_jugador(16, 'Angel Correa', 28, 1.75, '15 Millones', 'Media Punta')
    mostrar_jugadores()
