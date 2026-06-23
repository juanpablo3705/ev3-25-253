print("¡Bienvenido al programa para gestionar su tarjeta!")

deuda = 100000
saldo = 200000
suma_compras = 0

# menu principal
while True:

    print("----- MENÚ -----")
    print("1. Pago de Tarjeta de Crédito")
    print("2. Simulación de compras")
    print("3. Salir")
    print(f"Su saldo actual es de: ${saldo}.")
    print(f"Su deuda actual es de: ${deuda}.")
    
    while True:

        try:
            opcion = int(input("Ingrese una opción del menú: "))
            break
        except ValueError:
            print("Error. Ingrese sólo numeros enteros positivos, no letras.")

    match opcion:

        case 1: 

            while True:
                try:
                    pago = int(input(f"Ingrese un monto para pagar: "))
                    if (pago > 0) and (pago <= deuda):
                        deuda = deuda - pago
                        saldo = saldo + pago
                        print(f"Pago exitoso. Deuda: ${deuda}. Saldo: ${saldo}.")
                        break
                    else:
                        print(f"Error. El monto debe ser positivo, no exceder su deuda de: ${deuda} ni el saldo de su tarjeta de: ${saldo}: ")
                except ValueError:
                    print("Error. El monto debe ser numérico, no letras.")
            
        case 2:

            while True:
                try:
                    numero_compras = int(input("Ingrese el número de compras que desea simular: "))
                    if numero_compras > 0:
                        break
                    else:
                        print("Error. Debe ingresar un valor positivo.")
                except ValueError:
                    print("Error. Debe ingresar sólo números, no letras.")

            for index in range(numero_compras):
                while True:
                    try:
                        monto_compra = int(input(f"Ingrese el monto de la compra número {index + 1}: "))
                        if (monto_compra >= 0) and (monto_compra <= saldo):
                            suma_compras = suma_compras + monto_compra
                            saldo = saldo - monto_compra
                            print(f"Su compra de ${monto_compra} ha sido registrada.")
                            print(f"Nuevo saldo tarjeta: ${saldo}.")
                            break
                        else:
                            print(f"Error. Debe ingresar un valor positivo y menor o igual a su saldo de ${saldo}.")
                    except ValueError:
                        print("Error. debe ingresar sólo números, no letras.")

        case 3:

            print("Saliendo...")
            break

        case _:

            print("Error. Debe ingresar una opción del menú (1 a 3).")