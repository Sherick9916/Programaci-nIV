cliente_VIP= input("¿Es cliente VIP? (si/no): ")
rifa= input("Se va a realizar una rifa en el supermercado? (si/no): ")
nombre_producto1= input("Ingrese el nombre del primer producto: ")
precio_producto1= float(input("Ingrese el precio del primer producto: "))

if(rifa == "si"):
    if(cliente_VIP == "si"):
        if (precio_producto1 < 0):
            print("El precio no puede ser negativo.")
        else:
            cantidad_producto1= int(input("Ingrese la cantidad del primer producto: "))
            
            if (cantidad_producto1 < 0):
                print("La cantidad no puede ser negativa.")
            else:
                presenta_descuento1= input("¿El primer producto presenta descuento? (si/no): ")
                if(presenta_descuento1 == "si"):
                    descuento1 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                    total_producto1= precio_producto1 * cantidad_producto1 * (1 - descuento1 / 100)

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo produc: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                            
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)
                                Total_compra= total_producto1 + total_producto2

                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = total_final / cantidad_cuotas
                                            print(f"El total de la compra es: {total_final}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")

                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")
                            
                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = Total_compra / cantidad_cuotas
                                            print(f"El total de la compra es: {Total_compra}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2
                                Total_compra= total_producto1 + total_producto2
                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = total_final / cantidad_cuotas
                                            print(f"El total de la compra es: {total_final}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")

                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = Total_compra / cantidad_cuotas
                                            print(f"El total de la compra es: {Total_compra}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                else:

                    total_producto1= precio_producto1 * cantidad_producto1

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)
                                Total_compra= total_producto1 + total_producto2
                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = total_final / cantidad_cuotas
                                            print(f"El total de la compra es: {total_final}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")

                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = Total_compra / cantidad_cuotas
                                            print(f"El total de la compra es: {Total_compra}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2
                                Total_compra= total_producto1 + total_producto2
                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = total_final / cantidad_cuotas
                                            print(f"El total de la compra es: {total_final}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")

                                    cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                    if(cuotas_contado == "si"):
                                        cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                        if(cantidad_cuotas <= 0):
                                            print("La cantidad de cuotas debe ser mayor a 0.")
                                        else:
                                            res_valor_cuotas = Total_compra / cantidad_cuotas
                                            print(f"El total de la compra es: {Total_compra}")
                                            print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
    else:

        if (precio_producto1 < 0):
            print("El precio no puede ser negativo.")
        else:
            cantidad_producto1= int(input("Ingrese la cantidad del primer producto: "))
            
            if (cantidad_producto1 < 0):
                print("La cantidad no puede ser negativa.")
            else:
                presenta_descuento1= input("¿El primer producto presenta descuento? (si/no): ")
                if(presenta_descuento1 == "si"):
                    descuento1 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                    total_producto1= precio_producto1 * cantidad_producto1 * (1 - descuento1 / 100)

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)

                                Total_compra= total_producto1 + total_producto2

                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")
                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2

                                Total_compra= total_producto1 + total_producto2
                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")
                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")
                else:

                    total_producto1= precio_producto1 * cantidad_producto1

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)

                                Total_compra= total_producto1 + total_producto2

                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")
                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2

                                Total_compra= total_producto1 + total_producto2

                                x = int(input("Ingrese el valor mínimo del rango para la rifa: "))
                                y = int(input("Ingrese el valor máximo del rango para la rifa: "))
                                numero_ganador = int(input(f"Cajero, escriba el número ganador (entre {x} y {y}): "))
                                numero_cliente = int(input(f"Cliente, ingrese un número entre {x} y {y}: "))
                                if numero_cliente == numero_ganador:
                                    descuento_rifa = Total_compra * 0.9
                                    total_final = Total_compra - descuento_rifa
                                    print(f"¡Felicidades! Ganó la rifa. Se ahorró ${descuento_rifa} y debe pagar ${total_final}")
                                else:
                                    print(f"No ganó la rifa. El número ganador era {numero_ganador}. Debe pagar ${Total_compra}")
else:
    if(cliente_VIP == "si"):
        if (precio_producto1 < 0):
            print("El precio no puede ser negativo.")
        else:
            cantidad_producto1= int(input("Ingrese la cantidad del primer producto: "))
            
            if (cantidad_producto1 < 0):
                print("La cantidad no puede ser negativa.")
            else:
                presenta_descuento1= input("¿El primer producto presenta descuento? (si/no): ")
                if(presenta_descuento1 == "si"):
                    descuento1 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                    total_producto1= precio_producto1 * cantidad_producto1 * (1 - descuento1 / 100)

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                            
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)
                                Total_compra= total_producto1 + total_producto2
                                print(f"El total de la compra es: {Total_compra}")

                                cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                if(cuotas_contado == "si"):
                                    cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                    if(cantidad_cuotas <= 0):
                                        print("La cantidad de cuotas debe ser mayor a 0.")
                                    else:
                                        res_valor_cuotas = Total_compra / cantidad_cuotas
                                        print(f"El total de la compra es: {Total_compra}")
                                        print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2
                                Total_compra= total_producto1 + total_producto2
                                print(f"El total de la compra es: {Total_compra}")

                                cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                if(cuotas_contado == "si"):
                                    cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                    if(cantidad_cuotas <= 0):
                                        print("La cantidad de cuotas debe ser mayor a 0.")
                                    else:
                                        res_valor_cuotas = Total_compra / cantidad_cuotas
                                        print(f"El total de la compra es: {Total_compra}")
                                        print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                else:

                    total_producto1= precio_producto1 * cantidad_producto1

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)
                                Total_compra= total_producto1 + total_producto2
                                print(f"El total de la compra es: {Total_compra}")

                                cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                if(cuotas_contado == "si"):
                                    cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                    if(cantidad_cuotas <= 0):
                                        print("La cantidad de cuotas debe ser mayor a 0.")
                                    else:
                                        res_valor_cuotas = Total_compra / cantidad_cuotas
                                        print(f"El total de la compra es: {Total_compra}")
                                        print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2
                                Total_compra= total_producto1 + total_producto2
                                print(f"El total de la compra es: {Total_compra}")

                                cuotas_contado = input("¿Desea pagar a cuotas? (si/no): ")
                                if(cuotas_contado == "si"):
                                    cantidad_cuotas = int(input("Ingrese la cantidad de cuotas: "))
                                    if(cantidad_cuotas <= 0):
                                        print("La cantidad de cuotas debe ser mayor a 0.")
                                    else:
                                        res_valor_cuotas = Total_compra / cantidad_cuotas
                                        print(f"El total de la compra es: {Total_compra}")
                                        print(f"El pago por cuota a realizar es: {res_valor_cuotas}")
    else:

        if (precio_producto1 < 0):
            print("El precio no puede ser negativo.")
        else:
            cantidad_producto1= int(input("Ingrese la cantidad del primer producto: "))
            
            if (cantidad_producto1 < 0):
                print("La cantidad no puede ser negativa.")
            else:
                presenta_descuento1= input("¿El primer producto presenta descuento? (si/no): ")
                if(presenta_descuento1 == "si"):
                    descuento1 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                    total_producto1= precio_producto1 * cantidad_producto1 * (1 - descuento1 / 100)

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)

                                Total_compra= total_producto1 + total_producto2

                                print(f"El total de la compra es: {Total_compra}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2

                                Total_compra= total_producto1 + total_producto2
                                print(f"El total de la compra es: {Total_compra}")
                else:

                    total_producto1= precio_producto1 * cantidad_producto1

                    nombre_producto2= input("Ingrese el nombre del segundo producto: ")
                    precio_producto2= float(input("Ingrese el precio del segundo producto: "))

                    if (precio_producto2 < 0):
                        print("El precio no puede ser negativo.")
                    else:
                        cantidad_producto2= int(input("Ingrese la cantidad del segundo producto: "))

                        if (cantidad_producto2 < 0):
                            print("La cantidad no puede ser negativa.")
                        else:
                            presenta_descuento2= input("¿El segundo producto presenta descuento? (si/no): ")
                            if(presenta_descuento2 == "si"):
                                descuento2 = float(input("Ingrese el porcentaje de descuento (por ejemplo, para 20% ingrese 20): "))
                                total_producto2= precio_producto2 * cantidad_producto2 * (1 - descuento2 / 100)

                                Total_compra= total_producto1 + total_producto2

                                print(f"El total de la compra es: {Total_compra}")
                            else:
                                                
                                total_producto2= precio_producto2 * cantidad_producto2

                                Total_compra= total_producto1 + total_producto2

                                print(f"El total de la compra es: {Total_compra}")