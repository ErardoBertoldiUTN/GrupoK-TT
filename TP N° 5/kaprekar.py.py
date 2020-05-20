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

def numerosDiferentes(numero): 
    digito_1 = int(numero[0])
    cont = 0
    while cont < len(numero) - 1:  
        cont += 1                  
        digito_2 = int(numero[cont]) 
        if digito_1 != digito_2:    
            return True
    return False
def Kaprekar(numero):    #con esta funci�n voy a ir haciendo las iteraciones necesarias para llegar hasta el n�mero 6174
    restaNumeros = 0
    numeroIteraciones = 0
    numeroMayor = 0
    numeroMenor = 0
    numMen = ""
    while restaNumeros != 6174:     
        numeroMayor = numMay(numero) #aqu� llamamos a la funci�n numMay y le pasamos como par�metro el numero
        numMayor = str(numeroMayor)  #a la variable numMayor le asignamos el valor obtenido la linea anterior pero lo casteamos para que sea una cadena
        numeroMenor = int(numMayor[::-1])
        
        restaNumeros = numeroMayor - numeroMenor #ahora realizamos la resta entre el numero mayor y el menor
        #print(str(numeroMayor)+"-"+str(numeroMenor)+ "=" + str(restaNumeros)) #esta l�nea muestra en pantalla las restas sucesivas necesarias hasta llegar a la constante 6174
        numeroIteraciones += 1  #aqu� vamos controlando el numero de iteraciones
        numero = restaNumeros   #ahora a la variable numero le actualizamos el valor con lo obtenido en la resta anterior
    return numeroIteraciones

def numMay(numero):    
        
    return 

main()

