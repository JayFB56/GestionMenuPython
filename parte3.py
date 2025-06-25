from parte1 import * 

# Aplicar 10% de descuento al Ceviche de Camaron
menu_restaurante['ceviche de camaron']['precio'] *= 0.9
print("\nSe aplico un descuento del 10% al Ceviche de Camaron.")

# Añadir nuevo plato del dia Arroz con Huevo
menu_restaurante['arroz con huevo'] = {
    'precio': 3.5,
    'ingredientes': ('arroz', 'huevo', 'aceite', 'sal')
}
print("PLATO DEL DIA añadido: Arroz con Huevo.")

# Mostrar el menu actualizado
mostrar_menu(menu_restaurante)

# Seleccion de platos especiales actualizada con ceviche de camaron y arroz con pollo
especiales_del_dia = ['ceviche de camaron', 'arroz con pollo', 'encocado de cangrejo']

print("\nESPECIALES DEL DIA")
for plato in especiales_del_dia:
    if plato in menu_restaurante:
        detalles = menu_restaurante[plato]
        print(f"\nPlato: {plato.title()}")
        print(f"Precio: ${detalles['precio']}")
        print(f"Ingredientes: {', '.join(detalles['ingredientes'])}")

#print('------------------------------------')