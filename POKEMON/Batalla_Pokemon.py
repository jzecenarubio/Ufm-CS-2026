'''
Simulación de batalla pokemon, SIN utilizar OOP.

Equivalencias respecto a la versión con clases:
- class Pokemon + __init__  ->  función crear_pokemon() que devuelve un diccionario
- atributos (self.hp, ...)  ->  llaves del diccionario (pokemon['hp'], ...)
- __repr__                  ->  función info_pokemon()
- métodos damage / attack   ->  funciones damage(pokemon, ...) / attack(atacante, rival)
'''


from random import choice
from time import sleep


# ---------- "Clase" Pokemon (como funciones + diccionarios) ----------

# Constructor
def crear_pokemon(param_nombre: str, param_tipo: str, param_hp: int, param_ad: int) -> dict:
    return {
        'nombre': param_nombre.capitalize(),
        'tipo': param_tipo,
        'hp': param_hp,
        'ad': param_ad,
    }


# Equivalente a __repr__
def info_pokemon(pokemon: dict) -> str:
    return f'\n{pokemon["nombre"]} | HP: {pokemon["hp"]}'


# Equivalente a damage()
def damage(pokemon: dict, hp_lost: int):
    pokemon['hp'] = pokemon['hp'] - hp_lost


# Equivalente a attack()
def attack(atacante: dict, rival: dict):

    if atacante['tipo'] == 'electrico':
        ataque = 'Impactrueno'
    elif atacante['tipo'] == 'planta':
        ataque = 'Hoja navaja'
    elif atacante['tipo'] == 'fuego':
        ataque = 'Llamarada'
    else:
        ataque = 'Cañon de agua'

    damage(rival, atacante['ad'])

    print(f'\n({atacante["nombre"]}) Ataca con {ataque} | -{atacante["ad"]}')


# ---------- Utils ----------
def waiting():
    print('\n...')
    sleep(0.5)


# ---------- Simulación ----------

# Crear 4 pokemon de inventario
pikachu = crear_pokemon('pikachu', 'electrico', 60, 15)
chikorita = crear_pokemon('chikorita', 'planta', 45, 10)
charmander = crear_pokemon('charmander', 'fuego', 40, 10)
froakie = crear_pokemon('froakie', 'agua', 40, 20)


# Seleccionar 2 pokemon para batalla
pokemon_posibles = [pikachu, chikorita, charmander, froakie]

poke_1 = choice(pokemon_posibles)
poke_2 = choice(pokemon_posibles)

print('\n ------ POKEMON SELECCIONADOS ------')

waiting()
print(f'\nPokemon 1: {poke_1["nombre"]} (HP: {poke_1["hp"]} | AD: {poke_1["ad"]})')
print(f'Pokemon 2: {poke_2["nombre"]} (HP: {poke_2["hp"]} | AD: {poke_2["ad"]})')

# Manejo de turnos (ciclo con ambos turnos hasta que uno pierda)
while True:

    # Turno Poke_1
    waiting()
    attack(poke_1, poke_2)

    # Verificar si poke_2 perdió
    if poke_2['hp'] <= 0:
        print(f'\nGAME OVER: {poke_1["nombre"]} venció a {poke_2["nombre"]}')
        break

    # Turno Poke_2
    waiting()
    attack(poke_2, poke_1)

    # Verificar si poke_1 perdió
    if poke_1['hp'] <= 0:
        print(f'\nGAME OVER: {poke_2["nombre"]} venció a {poke_1["nombre"]}')
        break

    # Imprimir vidas restantes
    waiting()
    print(f'\nHPs restantes')
    print(f'{poke_1["nombre"]}: {poke_1["hp"]}')
    print(f'{poke_2["nombre"]}: {poke_2["hp"]}')