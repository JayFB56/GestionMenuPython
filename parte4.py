from parte2 import *

# 1. Error de IndexError
print("\nIndexError")
try:
    # Acceder a un indice fuera de la lista pedido_actual
    print(pedido_actual[10])
except IndexError as e:
    print(f"Error: {e}")

# 2. Error de Clave (KeyError)
print("\nKeyError")
try:
    # Acceder a una clave que no existe en menu_restaurante
    print(menu_restaurante['arroz con salchica'])
except KeyError as e:
    print(f"Error: {e}")

# 3. Inmutabilidad de Tuplas (TypeError)
print("\nTypeError")
try:
    # Modificar un ingrediente dentro de la tupla
    menu_restaurante['ceviche de camaron']['ingredientes'][0] = 'tomate' 
except TypeError as e:
    print(f"Error: {e}")
