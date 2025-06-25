from parte1 import * 

# Lista para el carrito
pedido_actual = []
total_cuenta = 0

# Mostrar el menu
mostrar_menu(menu_restaurante)

# Bucle para recibir pedidos
while True:
    entrada = input("\nIntroduce el nombre del plato deseado o 'fin' para terminar: ").lower()
    
    if entrada == 'fin':
        break
    elif entrada in menu_restaurante:
        pedido_actual.append(entrada)
        total_cuenta += menu_restaurante[entrada]['precio']
        print(f"'{entrada.title()}' añadido al carrito")
    else:
        print("Lo sentimos, ese plato no esta en el menu.")

# Mostrar todo el pedido
print("\nRESUMEN DEL PEDIDO")
for plato in pedido_actual:
    print(f"- {plato.title()}")
print(f"Total a pagar: ${total_cuenta}")
