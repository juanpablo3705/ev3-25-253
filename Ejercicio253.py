ingreso = True
saldo = 400000
deuda = 100000
while ingreso:
    print("--Menu--")
    print("1. Pago Tarjeta de Crédito")
    print("2. Simulación de compras")
    print("3. Salir")
    while True:
        try:
            op = int(input("Ingrese su opción: "))
            break
        except ValueError:
            print("Ingrese un valor numerico del 1 al 3")

    if op == 1:
        print("Pagando...")
        print("Deuda $",deuda)
        montoPagar = int(input("Ingrese monto a pagar: "))
        if montoPagar >= 0 :
            if montoPagar <= deuda :
                deuda = deuda - montoPagar
                saldo = saldo + montoPagar
                print("Pago exitoso!! , El saldo de la deuda es: $",deuda)
            else:
                print("El monto excede la deuda")
    elif op == 2: 
        print("Comprando...")
        print("Su saldo para comprar es $",saldo)
        cont = 0
        for i in range(saldo):
            
            cont = cont + 1
            print(f"Compra {cont}")
            while True:
                try:
                    montoCompra = int(input("Ingrese monto de la compra: $"))
                    break
                except ValueError:
                    print("Error!, Ingrese un monto válido!!, Ingrese nuevamente")

            if montoCompra >=0 :
                if saldo > montoCompra:
                    saldo  = saldo - montoCompra
                    deuda = deuda + montoCompra
                    print("Su saldo es: $",saldo)
                    if montoCompra == 0 or saldo <= 0 :
                        break
                else:
                    print("El saldo es insuficiente")
                    break
            else:
                print("Por favor ingrese un numero mayor a cero")
                cont= cont-1

    elif op == 3:
        print("Saliendo...")
        #break
        ingreso = False
    else:
        print("Opción no válida!")
