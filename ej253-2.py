deuda = 100000
cupo = 500000

# inicio del ciclo general del menú:
menu = True
while menu:
    print("-----Menú-----")
    print("1. Pago de tarjeta de crédito")
    print("2. Simulación de compra")
    print("3. Salir")
    print("-----Información-----")
    print(f"Deuda tarjeta: ${deuda}.")
    print(f"Cupo tarjeta (disponible sólo si la deuda está pagada): ${cupo}.")

    # validación: que el usuario ingrese números int y no letras str
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

        # ingreso pago deuda:
        while True:
            try:
                pago_deuda = int(input("Ingrese monto a pagar (igual o menor a su deuda): "))
                break
            except ValueError:
                print("Error. Ingrese un número entero.")

        # inicio proceso post pago deuda:
        if pago_deuda >= 0: # verificacion error pago menor a 0
            if pago_deuda <= deuda:
                deuda = deuda - pago_deuda
                print("Pago recibido")
                if deuda == 0:
                    print(f"Nuevo saldo: $0. Ahora puede usar su cupo de: ${cupo}.")
                else:
                    print(f"Pago recibido. Aún mantiene una deuda de: ${deuda}.")
            else:
                print(f"No puede pagar un monto superior a su deuda. Ingrese un monto igual o inferior a: {deuda}")
                while True:
                    try:
                        pago_deuda = int(input("Ingrese monto a pagar (igual o menor a su deuda): "))
                        deuda = deuda - pago_deuda
                        print("Pago recibido")
                        break
                    except ValueError:
                        print("Error. Ingrese un número entero.")
        else:
            print("Ingrese un monto de dinero positivo.")
            while True:
                    try:
                        pago_deuda = int(input("Ingrese monto a pagar (igual o menor a su deuda): "))
                        deuda = deuda - pago_deuda
                        print("Pago recibido")
                        break
                    except ValueError:
                        print("Error. Ingrese un número entero.")
    
    # inicio opcion 2:
    elif opcion_menu == 2:
        print("Realice una simulación de compra.")
        print(f"Usted tiene un cupo en su tarjeta de: ${cupo}.")
        print(f"Sólo puede usar su cupo si su deuda es cero. Deuda actual: ${deuda}.")
        
        # si la deuda NO está pagada, no puede usar su cupo ni comprar:
        if deuda > 0:
            print(f"Usted debe dinero. Pague primero su deuda de ${deuda} en la opción 1.")
       
        # si la deuda SI está pagada, puede usar cupo y comprar:
        else:
            for contador in range(cupo):
               
                # verificacion e ingreso de monto compra que sea int:
                while True:
                    try:
                        monto_compra = int(input("Ingrese monto de su compra: "))
                        break
                    except ValueError:
                        print("Error. Ingrese un valor numérico mayor a cero.")
                
                # inicio proceso compra:
                if monto_compra >= 0: # verificación error compra mayor que cero:
                    cupo = cupo - monto_compra
                    print(f"Compra realizada. Nuevo cupo: ${cupo}.")
                    if cupo <= 0:
                        break
                else:
                    print("Ingrese un monto de compra superior a cero.")

    # inicio opcion 3:
    elif opcion_menu == 3:
        print("Saliendo del programa...")
        menu = False

    # verificacion rango de opciones validas:
    else:
        print("Opción no válida. Ingrese un número del 1 al 3.")