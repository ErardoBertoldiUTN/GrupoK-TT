#entorno utilizado: IDLE (Python 3.8 64 bits)      Sebasti�n Garc�a
#NOTA:si quiere ver por pantalla las restas sucesivas que va haciendo el programa hasta llegar a la constante, se debe descomentar el print() dentro de la funcion Kaprekar
def main():   #http://conocepython.blogspot.com/p/la-funcion-main.html
    #programa principal. Desde aqu� inicia nuestro programa mostrando por pantalla la consigna que realizar� nuestro c�digo
    print("Constante de Kaprekar")
    print("1.Elija un n�mero de cuatro d�gitos que tenga al menos dos diferentes (es v�lido colocar el d�gito 0 al principio, por lo que el n�mero 0009 es v�lido).\nSi ingresa un n�mero con menos de cuatro cifras, se completar� con ceros para convertirlo a numero de cuatro cifras.")
    print("Si ingresa un n�mero mayor o menor a cuatro cifras, se escribir� un mensaje en pantalla al respecto")
    print("2.Se colocar�n sus d�gitos en orden ascendente y en orden descendente para formar dos nuevos n�meros")
    print("3.Se restar� el menor al mayor.\n4.Vuelve al paso 2 hasta llegar a la constante 6174.")
    casosPrueba = int(input("Ingresa el numero de casos de prueba: "))   #esta variable guardar� la cantidad de n�meros a analizar
    contador = 1
    while contador <= casosPrueba:   #Este ciclo while lo que hace es controlar que se vayan pidiendo los n�meros de a uno por vez,
                                        #y a cada uno de esos n�meros se le determinar� la cantidad de iteraciones necesarias para llegar la constate de Kaprekar

        while True:         #este ciclo while controlar� que yo ingrese si o si un dato entero, caso contrario el programa explotar�a si ingreso por error una letra
            numeroIng = str(input("Ingrese el "+str(contador)+"� n�mero\n"))
            try:
                entero = int(numeroIng)
                break  #si el numero ingresado es entero sale del bucle
            except ValueError:  #si ingreso otro tipo de datos, por ejemplo letras, me vuelve a pedir que ingrese un dato num�rico
                print ("La entrada es incorrecta: escriba un numero entero")
                          
        if len(numeroIng) < 4:   #eval�a si el n�mero tiene cuatro d�gitos. De no ser as�, pide que se ingrese un n�mero de 4 d�gitos 
            print("El n�mero tiene menos de cuatro digitos. Ingrese otro numero de cuatro digitos")
        else:
            if len(numeroIng) > 4:
                print("El n�mero tiene mas de cuatro digitos. Ingrese otro numeros de cuatro digitos")
            else:
                if numeroIng == "6174":  #este IF eval�a si mi n�mero ingresado es 6174. Si es as�, el programa me imprime un 0, seg�n lo pedido en la consigna
                    print("0")
                else:
                    NRO=numerosDiferentes(numeroIng)  #llamada a la funci�n numerosDiferentes. Regresa un bolean que guarda en NRO. Si el n�mero tiene al menos dos d�gitos distintos devuelve true
                    if NRO:   #Si NRO tiene valor true, en la siguiente l�nea llamar� a la funci�n Kaprekar
                        print("El numero: "+ str(numeroIng) + ", requiere "+str(Kaprekar(numeroIng))+" iteraciones." )
                    else:  #Si no, si NRO es false, es decir si los cuatro d�gitos son iguales, imprimir� un 8 como lo requiere la consigna
                        print("8")
                contador += 1   #este contador se va incrementando en 1 a medida que van avanzando los casos de prueba, una vez que cont sea igual a numero_casosPrueba, saldr� del while
    print("FIN DEL PROGRAMA")

def numerosDiferentes(numero): #Esta funci�n recibe como par�metro un String contenido en 'numero'
    digito_1 = int(numero[0]) #asigno a digito_1 el primer caracter de numero y lo casteo a entero
    cont = 0
    while cont < len(numero) - 1:   #con la funci�n len recorro de a un caracter la cadena contenida en 'numero'
        cont += 1                   #esta variable es un contador que me permite ir recorriendo la cadena
        digito_2 = int(numero[cont]) 
        if digito_1 != digito_2:    #con este if controlo que al menos hayan dos d�gitos diferentes en mi numero de cuatro cifras
            return True
    return False                     #si todos los digitos son iguales devuelve false

def Kaprekar(numero):    #con esta funci�n voy a ir haciendo las iteraciones necesarias para llegar hasta el n�mero 6174
    restaNumeros = 0
    numeroIteraciones = 0
    numeroMayor = 0
    numeroMenor = 0
    numMen = ""
    while restaNumeros != 6174:      #mientras restaNumeros sea distinta a 6174 se repetir� este ciclo while
        numeroMayor = numMay(numero) #aqu� llamamos a la funci�n numMay y le pasamos como par�metro el numero
        numMayor = str(numeroMayor)  #a la variable numMayor le asignamos el valor obtenido la linea anterior pero lo casteamos para que sea una cadena
        numeroMenor = int(numMayor[::-1])   #la cadena obtenida en la l�nea anterior la invertimos y la almacenamos en numeroMenor y la convertimos en un int
                                            #[::-1] devuelve los elementos de la cadena comenzando por el �ltimo y terminando por el primero,
                                            # en orden inverso a como estaban
        restaNumeros = numeroMayor - numeroMenor #ahora realizamos la resta entre el numero mayor y el menor
        #print(str(numeroMayor)+"-"+str(numeroMenor)+ "=" + str(restaNumeros)) #esta l�nea muestra en pantalla las restas sucesivas necesarias hasta llegar a la constante 6174
        numeroIteraciones += 1  #aqu� vamos controlando el numero de iteraciones
        numero = restaNumeros   #ahora a la variable numero le actualizamos el valor con lo obtenido en la resta anterior
    return numeroIteraciones    #me devuelve el n�mero de iteraciones realizadas, es decir la cantidad de restas sucesivas hasta llegar a la constante de kaprekar

def numMay(numero):     #Esta funci�n recibe la variable numero y ordenar� sus d�gitos de manera de obtener el mayor numero posible. Luego retorna dicho numero
    num = str(numero)      #convertimos el n�mero en una cadena
    if len(num) == 1:      #estos if anidados los utilizo para completar a cuatro cifras a 'numero' en caso que me llegue un par�metro con menos de cuatro cifras
                           #ya que puede suceder que en alg�n caso la funci�n Kaprekar me entregue un numero que tenga menos de cuatro cifras,
                           #resultante de las restas sucesivas
        num = '000' + num
    else:
        if len(num) == 2:
            num = '00' + num
        else:
            if len(num) == 3:
                num = '0' + num
    cifraMayor = ""         #donde guardaremos el n�mero mas grande que se pueda obtener. Lo inicializo sin nada
    cifraCompleta = False   

    while cifraCompleta == False:
        mayor = int(num[0])      #asignamos el primer caracter de la cadena num a mayor y lo transformamos en un entero
        cont = 0                 #el contador lo usamos para recorrer la cadena contenida en num
        while cont < len(num) -1:   #este ciclo while me permitir� recorrer la cadena num para ir comparando los numeros que contiene.
                                    #Sale del ciclo cuando ha recorrido todos los caracteres de la cadena
            cont += 1
            digito = int(str(num[cont]))  #asignamos el siguiente valor de la cadena num a la variable digito, tranform�ndolo en un entero
            if digito > mayor:            #si digito es mas grande que mayor, le asignamos su valor a mayor
                mayor = digito            #una vez que finalice el ciclo while, en esta variable habremos asignado el mayor d�gito de la cadena

        
        cifraMayor +=str(mayor)    #le vamos asignando a cifraMayor el valor contenido en mayor
        #print("cifraMayor"+cifraMayor)
        num = num.replace(str(mayor), "", 1)  #la funci�n replace sirve para reemplazar caracteres dentro de la cadena. El 1 indica que lo hace una sola vez
                                              #En este caso reemplazo con un caracter "" a mayor, es decir borro al digito mayor de la cadena
                                              #Cabe aclarar que ese valor borrado lo asign� anteriormente a la variable cifraMayor.
                                              #Para el siguiente ciclo la cadena num tendr� un caracter menos ya que le "borramos" al digito de mayor valor
        #print("num"+num)
        if len(cifraMayor) == 4:  #si cifraMayor posee cuatro caracteres... 
            cifraCompleta = True #se le asigna true a cifraCompleta saliendo del primer ciclo while
    return int(cifraMayor)  #retorna el valor mayor posible obtenido a partir del numero recibido en primera instancia

main()  #debo colocar el llamado a la funci�n main aqu�. No es necesario utilizar una funci�n main en python. El programa compila igual sin ella...
        #decidimos colocarla porque nos parec�a que quedaba mas prolijo el c�digo

