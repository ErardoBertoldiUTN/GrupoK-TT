  # Proyecto de Joaquin Roman, codificado en Visual Studio 2019.

print ("CONSTANTE DE KAPREKAR. \nPara números de cuatro dígitos que tenga al menos dos diferentes, el valor esperado es 6174")

lista = []  # esta lista contendrá todos los números de Kaprekar encontrados

def asc(n): # pone los dígitos del número en forma ascendente
    return int(''.join(sorted(str(n))))

def desc(n): # pone los dígitos del número en forma descendente
    return int(''.join(sorted(str(n))[::-1]))

while True:
    n = input("Ingrese un número entero de cuatro dígitos: ")
    try:
        n = int(n)
        break   #si el numero ingresado es entero sale del bucle
    except ValueError:  #si ingreso otro tipo de datos, por ejemplo letras, me vuelve a pedir que ingrese numeros
        print ("La entrada es incorrecta: escriba un numero entero")

while True:     # itera, asigna la nueva diferencia
    print(desc(n), "-", asc(n), "=", desc(n)-asc(n))
    n = desc(n) - asc(n)

    if n not in lista:   # comprueba si ya alcanzó ese número
        lista.append(n)
    else:
        if lista.index(n) == len(lista)-1:  # si se encuentra como el último, es una constante...
            lista = []
            lista.append(n)
        else:         # ...de lo contrario es un bucle
            lista = lista[lista.index(n):]
        break

print('Constante de Kaprekar igual a:', lista)
