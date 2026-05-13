saldo = 400000
deuda = 100000

# inicio del ciclo general del menú:
menu = True
while menu:
    print("-----Menú-----")
    print("1. Pago de tarjeta de crédito")
    print("2. Simulación de compra")
    print("3. Salir")

    # validación: que el usuario ingrese números enteros int y no letras str
    while True:
        try:
            opcion_menu = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Error. Ingrese un número entero del 1 al 3.")

    # inicio opción 1:
    if opcion_menu == 1:
        print("Ahora usted podrá pagar la deuda de su tarjeta.")
        print(f"Su deuda actual es de: ${deuda}.")