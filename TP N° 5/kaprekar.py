def main():   #http://conocepython.blogspot.com/p/la-funcion-main.html
    #programa principal. Desde aqui inicia nuestro programa mostrando por pantalla el enunciado que realizará nuestro código
    print("Constante de Kaprekar")
    print("1.Elija un número de cuatro dígitos que tenga al menos dos diferentes (es válido colocar el dígito 0 al principio, por lo que el número 0009 es válido).\nSi ingresa un número con menos de cuatro cifras, se completará con ceros para convertirlo a numero de cuatro cifras.")
    print("Si ingresa un número mayor o menor a cuatro cifras, se escribirá un mensaje en pantalla al respecto")
    print("2.Se colocarán sus dígitos en orden ascendente y en orden descendente para formar dos nuevos números")
    print("3.Se restará el menor al mayor.\n4.Vuelve al paso 2 hasta llegar a la constante 6174.")
    casosPrueba = int(input("Ingresa el numero de casos de prueba: "))   #esta variable guardar� la cantidad de n�meros a analizar
    contador = 1
    while contador <= casosPrueba:   

        while True:         

            numeroIng = str(input("Ingrese el "+str(contador)+"° número\n"))
            try:
                entero = int(numeroIng)
                break  
            except ValueError:  
                print ("La entrada es incorrecta: escriba un numero entero")
                          
        if len(numeroIng) < 4:    
            print("El número tiene menos de cuatro dígitos. Ingrese otro número de cuatro dígitos")
        else:
            if len(numeroIng) > 4:
                print("El número tiene mas de cuatro dígitos. Ingrese otro números de cuatro dígitos")
            else:
                if numeroIng == "6174": 
                    print("0")
                '''else:
                    NRO=numerosDiferentes(numeroIng)  

                    if NRO:  
                        print("El numero: "+ str(numeroIng) + ", requiere "+str(Kaprekar(numeroIng))+" iteraciones." )
                    else:  
                        print("8")
                contador += 1   '''
    print("FIN DEL PROGRAMA")

... luego las funciones
