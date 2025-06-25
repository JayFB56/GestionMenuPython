# Diccionario de menu de platos
menu_restaurante = {
    'arroz con pollo': {
        'precio': 7.5,
        'ingredientes': ('arroz', 'pollo', 'zanahoria', 'pimiento', 'cebolla', 'ajo', 'arvejas')
    },
    'encebollado': {
        'precio': 6.0,
        'ingredientes': ('pescado', 'yuca', 'cebolla morada', 'tomate', 'limon', 'cilantro')
    },
    'sopa de pollo': {
        'precio': 5.0,
        'ingredientes': ('pollo', 'papa', 'zanahoria', 'fideo', 'cebolla', 'ajo', 'cilantro')
    },
    'ceviche de camaron': {
        'precio': 8.0,
        'ingredientes': ('camaron', 'tomate', 'cebolla morada', 'limon', 'cilantro', 'naranja')
    },
    'ensalada de atun': {
        'precio': 5.5,
        'ingredientes': ('atun', 'lechuga', 'tomate', 'cebolla', 'huevo duro', 'mayonesa')
    },
    'pollo asado': {
        'precio': 7.0,
        'ingredientes': ('pollo', 'ajo', 'limon', 'comino', 'pimienta', 'sal')
    },
    'encocado de cangrejo': {
        'precio': 9.5,
        'ingredientes': ('cangrejo', 'leche de coco', 'cebolla', 'ajo', 'ají', 'pimiento', 'cilantro')
    }
}

# Funcion para mostrar el menu
def mostrar_menu(menu):
    print("\nMENU DEL RESTAURANTE")
    for nombre_plato, detalles in menu.items():
        print(f"\nPlato: {nombre_plato.title()}")
        print(f"Precio: ${detalles['precio']}")
        print(f"Ingredientes: {', '.join(detalles['ingredientes'])}")

mostrar_menu(menu_restaurante)
