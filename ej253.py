ingreso = True
saldo = 400000
deuda = 100000

while ingreso:
    print("--Menu--")
    print("1. Pago tarjeta crédito")
    print("2. Simulació de compras")
    print("3. Salir")

    op = int(input("Ingrese su opcion: "))

    if op == 1:
        print("Pagando...")
        print("Deuda $", deuda)
        monto_pagar = int(input("Ingrese monto a pagar: "))
        if monto_pagar >= 0:
            if monto_pagar <= deuda:
                deuda = deuda - monto_pagar
                saldo = saldo + monto_pagar
                print("Pago exitoso!!, el saldo de la deuda es: ", deuda)
            else:
                print("El monto excede la deuda")

    elif op == 2:
        print("Comprando...")
        # es cantidad ilimitada de numero de compras pero esta limitado por el saldo
        print("su saldo para comprar es: $", saldo)
        for i in range(saldo): # tiene que llegar hasta que termina el saldo, el rango tiene que ser el saldo
            cont = cont + 1
            print(f"Compra {cont}")
            monto_compra = int(input("Ingrese monto de la compra: "))

            if monto_compra >= 0:
                if saldo < monto_compra:
                    saldo = saldo - monto_compra
                    print("Su saldo es: ", saldo)
                if monto_compra == 0 or saldo <= 0:
                    break # tambien funciona para el ciclo while
            else:
                print("Por favor ingrese un numero mayor a cero: ")
                cont = cont - 1
        


    elif op == 3:
        print("Saliendo...")
        # break
        ingreso = False
    else:
        print("Opcion no valida")

