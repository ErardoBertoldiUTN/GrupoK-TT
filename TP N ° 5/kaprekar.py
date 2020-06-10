#https://github.com/ErardoBertoldiUTN/GrupoK-TT/tree/master/TP%20N%C2%B0%205
#entorno utilizado: IDLE (Python 3.8 64 bits)   GRUPO K
#NOTA:si quiere ver por pantalla las restas sucesivas que va haciendo el programa hasta llegar a la constante, se debe descomentar el print() dentro de la funcion Kaprekar
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
                break  #si el numero ingresado es entero sale del bucle
            except ValueError:  #si ingreso otro tipo de datos, por ejemplo letras, me vuelve a pedir que ingrese un dato numérico
                print ("La entrada es incorrecta: escriba un numero entero")
                         
                   
        if len(numeroIng) < 4:   #evalúa si el número tiene cuatro dígitos. De no ser así, pide que se ingrese un número de 4 dígitos 
            print("El número tiene menos de cuatro digitos. Ingrese otro numero de cuatro digitos")
        else:
            if len(numeroIng) > 4:
                print("El número tiene mas de cuatro digitos. Ingrese otro numeros de cuatro digitos")
            else:
                if numeroIng == "6174":  #este IF evalúa si mi número ingresado es 6174. Si es así, el programa me imprime un 0, según lo pedido en la consigna
                    print("0")
                else:
                    NRO=numerosDiferentes(numeroIng)  #llamada a la función numerosDiferentes. Regresa un bolean que guarda en NRO. Si el número tiene al menos dos dígitos distintos devuelve true
                    if NRO:   #Si NRO tiene valor true, en la siguiente línea llamará a la función Kaprekar
                        print("El numero: "+ str(numeroIng) + ", requiere "+str(Kaprekar(numeroIng))+" iteraciones." )
                    else:  #Si no, si NRO es false, es decir si los cuatro dígitos son iguales, imprimirá un 8 como lo requiere la consigna
                        print("8")
                contador += 1   #este contador se va incrementando en 1 a medida que van avanzando los casos de prueba, una vez que cont sea igual a numero_casosPrueba, saldrá del while
    print("FIN DEL PROGRAMA")

def numerosDiferentes(numero): #Esta función recibe como parámetro un String contenido en 'numero'
    digito_1 = int(numero[0]) #asigno a digito_1 el primer caracter de numero y lo casteo a entero
    cont = 0
    while cont < len(numero) - 1:   #con la función len recorro de a un caracter la cadena contenida en 'numero'
        cont += 1                   #esta variable es un contador que me permite ir recorriendo la cadena
        digito_2 = int(numero[cont]) 
        if digito_1 != digito_2:    #con este if controlo que al menos hayan dos dígitos diferentes en mi numero de cuatro cifras
            return True
    return False                     #si todos los digitos son iguales devuelve false

def Kaprekar(numero):    #con esta función voy a ir haciendo las iteraciones necesarias para llegar hasta el número 6174
    restaNumeros = 0
    numeroIteraciones = 0
    numeroMayor = 0
    numeroMenor = 0
    numMen = ""
    while restaNumeros != 6174:      #mientras restaNumeros sea distinta a 6174 se repetirá este ciclo while
        numeroMayor = numMay(numero) #aquí llamamos a la función numMay y le pasamos como parámetro el numero
        numMayor = str(numeroMayor)  #a la variable numMayor le asignamos el valor obtenido la linea anterior pero lo casteamos para que sea una cadena
        numeroMenor = int(numMayor[::-1])   #la cadena obtenida en la línea anterior la invertimos y la almacenamos en numeroMenor y la convertimos en un int
                                            #[::-1] devuelve los elementos de la cadena comenzando por el último y terminando por el primero,
                                            # en orden inverso a como estaban
        restaNumeros = numeroMayor - numeroMenor #ahora realizamos la resta entre el numero mayor y el menor
        #print(str(numeroMayor)+"-"+str(numeroMenor)+ "=" + str(restaNumeros)) #esta línea muestra en pantalla las restas sucesivas necesarias hasta llegar a la constante 6174
        numeroIteraciones += 1  #aquí vamos controlando el numero de iteraciones
        numero = restaNumeros   #ahora a la variable numero le actualizamos el valor con lo obtenido en la resta anterior
    return numeroIteraciones    #me devuelve el número de iteraciones realizadas, es decir la cantidad de restas sucesivas hasta llegar a la constante de kaprekar

def numMay(numero):     #Esta función recibe la variable numero y ordenará sus dígitos de manera de obtener el mayor numero posible. Luego retorna dicho numero
    num = str(numero)      #convertimos el número en una cadena
    if len(num) == 1:      #estos if anidados los utilizo para completar a cuatro cifras a 'numero' en caso que me llegue un parámetro con menos de cuatro cifras
                           #ya que puede suceder que en algún caso la función Kaprekar me entregue un numero que tenga menos de cuatro cifras,
                           #resultante de las restas sucesivas
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
        while cont < len(num) -1:   #este ciclo while me permitirá recorrer la cadena num para ir comparando los numeros que contiene.
                                    #Sale del ciclo cuando ha recorrido todos los caracteres de la cadena
            cont += 1
            digito = int(str(num[cont]))  #asignamos el siguiente valor de la cadena num a la variable digito, tranformándolo en un entero
            if digito > mayor:            #si digito es mas grande que mayor, le asignamos su valor a mayor
                mayor = digito            #una vez que finalice el ciclo while, en esta variable habremos asignado el mayor dígito de la cadena

        
        cifraMayor +=str(mayor)    #le vamos asignando a cifraMayor el valor contenido en mayor
        #print("cifraMayor"+cifraMayor)
        num = num.replace(str(mayor), "", 1)  #la función replace sirve para reemplazar caracteres dentro de la cadena. El 1 indica que lo hace una sola vez
                                              #En este caso reemplazo con un caracter "" a mayor, es decir borro al digito mayor de la cadena
                                              #Cabe aclarar que ese valor borrado lo asigné anteriormente a la variable cifraMayor.
                                              #Para el siguiente ciclo la cadena num tendrá un caracter menos ya que le "borramos" al digito de mayor valor
        #print("num"+num)
        if len(cifraMayor) == 4:  #si cifraMayor posee cuatro caracteres... 
            cifraCompleta = True #se le asigna true a cifraCompleta saliendo del primer ciclo while
    return int(cifraMayor)  #retorna el valor mayor posible obtenido a partir del numero recibido en primera instancia

main()  #debo colocar el llamado a la función main aquí. No es necesario utilizar una función main en python. El programa compila igual sin ella...
        #decidimos colocarla porque nos parecía que quedaba mas prolijo el código
#https://github.com/ErardoBertoldiUTN/GrupoK-TT/tree/master/TP%20N%C2%B0%205
