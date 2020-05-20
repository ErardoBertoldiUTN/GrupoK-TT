def main():   #http://conocepython.blogspot.com/p/la-funcion-main.html
    #programa principal. Desde aquí inicia nuestro programa mostrando por pantalla la consigna que realizará nuestro código
    print("Constante de Kaprekar")
    print("1.Elija un número de cuatro dígitos que tenga al menos dos diferentes (es válido colocar el dígito 0 al principio, por lo que el número 0009 es válido).\nSi ingresa un número con menos de cuatro cifras, se completará con ceros para convertirlo a numero de cuatro cifras.")
    print("Si ingresa un número mayor o menor a cuatro cifras, se escribirá un mensaje en pantalla al respecto")
    print("2.Se colocarán sus dígitos en orden ascendente y en orden descendente para formar dos nuevos números")
    print("3.Se restará el menor al mayor.\n4.Vuelve al paso 2 hasta llegar a la constante 6174.")
    casosPrueba = int(input("Ingresa el numero de casos de prueba: "))   #esta variable guardará la cantidad de números a analizar
    contador = 1
    while contador <= casosPrueba:   #Este ciclo while lo que hace es controlar que se vayan pidiendo los números de a uno por vez,
                                        #y a cada uno de esos números se le determinará la cantidad de iteraciones necesarias para llegar la constate de Kaprekar

        while True:         #este ciclo while controlará que yo ingrese si o si un dato entero, caso contrario el programa explotaría si ingreso por error una letra

            numeroIng = str(input("Ingrese el "+str(contador)+"° número\n"))
            try:
                entero = int(numeroIng)
                break  
            except ValueError:  
                print ("La entrada es incorrecta: escriba un numero entero")
                          
        if len(numeroIng) < 4:    
            print("El nÃºmero tiene menos de cuatro dÃ­gitos. Ingrese otro nÃºmero de cuatro dÃ­gitos")
        else:
            if len(numeroIng) > 4:
                print("El nÃºmero tiene mas de cuatro dÃ­gitos. Ingrese otro nÃºmeros de cuatro dÃ­gitos")
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
def Kaprekar(numero):    #con esta función voy a ir haciendo las iteraciones necesarias para llegar hasta el número 6174
    restaNumeros = 0
    numeroIteraciones = 0
    numeroMayor = 0
    numeroMenor = 0
    numMen = ""
    while restaNumeros != 6174:     
        numeroMayor = numMay(numero) #aquí llamamos a la función numMay y le pasamos como parámetro el numero
        numMayor = str(numeroMayor)  #a la variable numMayor le asignamos el valor obtenido la linea anterior pero lo casteamos para que sea una cadena
        numeroMenor = int(numMayor[::-1])
        
        restaNumeros = numeroMayor - numeroMenor #ahora realizamos la resta entre el numero mayor y el menor
        #print(str(numeroMayor)+"-"+str(numeroMenor)+ "=" + str(restaNumeros)) #esta línea muestra en pantalla las restas sucesivas necesarias hasta llegar a la constante 6174
        numeroIteraciones += 1  #aquí vamos controlando el numero de iteraciones
        numero = restaNumeros   #ahora a la variable numero le actualizamos el valor con lo obtenido en la resta anterior
    return numeroIteraciones

def numMay(numero):    
    num = str(numero)      
    if len(num) == 1:      
        num = '000' + num
    else:
        if len(num) == 2:
            num = '00' + num
        else:
            if len(num) == 3:
                num = '0' + num
    cifraMayor = ""         #donde guardaremos el número mas grande que se pueda obtener. Lo inicializo sin nada
    cifraCompleta = False   

    while cifraCompleta == False:
        mayor = int(num[0])      #asignamos el primer caracter de la cadena num a mayor y lo transformamos en un entero
        cont = 0                 #el contador lo usamos para recorrer la cadena contenida en num
        while cont < len(num) -1:  
            cont += 1
            digito = int(str(num[cont]))  #asignamos el siguiente valor de la cadena num a la variable digito, tranformándolo en un entero
            if digito > mayor:            #si digito es mas grande que mayor, le asignamos su valor a mayor
                mayor = digito            #una vez que finalice el ciclo while, en esta variable habremos asignado el mayor dígito de la cadena

        
        cifraMayor +=str(mayor)    #le vamos asignando a cifraMayor el valor contenido en mayor
        #print("cifraMayor"+cifraMayor)
        num = num.replace(str(mayor), "", 1)  
        #print("num"+num)
        if len(cifraMayor) == 4:  #si cifraMayor posee cuatro caracteres... 
            cifraCompleta = True #se le asigna true a cifraCompleta saliendo del primer ciclo while
    return int(cifraMayor) 

main()
