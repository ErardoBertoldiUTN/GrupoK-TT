#JUGADOR AZUL JUEGA CON TECLAS AWSD, JUGADOR AMARILLO JUEGA CON LAS FLECHAS
import os
import pygame
import math
from pygame import Rect
from pygame.locals import*
import MenuPacMan as menu

#inicializar
os.environ['SDL_VIDEO_CENTERED'] = '1'  #para que me aparezca centrada en el monitor la ventana pygame
pygame.init()

#medidas de la pantalla
ANCHO=1270
ALTO=640

#colores
NEGRO=(0,0,0)
AZUL=(0,0,255)
VERDE=(0,75,0)
MARRON=(150,70,10)
ROJO=(255,0,0)
AMARILLO=(255,255,0)
BLANCO=(255,255,255)
CELESTE=(0,255,255)


#Mapas
#1270/40=32 baldosas a lo ancho
#640/40=16 baldosas a lo largo
mapa=[  #las X me representan las baldosas. Este mapa se usará cuando participen dos jugadores
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                              X",
    "X     XXXX XXXXX XXXX XXXX  X  X",
    "X                           X  X",
    "X         XXX  XXXXXX  XXX     X",
    "X    X                     X   X",
    "X    X   X   XXXX XXX XXX  X   X",
    "X    X   X                 X   X",
    "X    X   X   XXXX XXX XX       X",
    "X                              X",
    "X   X  XXXX XXXXX XXXX XXXX    X",
    "X   X                          X",
    "X   X  XXX XXX XXX XXX XXXX    X",
    "X   X                          X",
    "X                              X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
mapaUnJugador=[  #Este mapa se usará cuando participe un jugador solo
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XX                            XX",
    "XX   XXXX      X              XX",
    "XX         XXX   XXXXX  XXX   XX",
    "XX    X                     X XX",
    "XX    X   XX  XXXX XXX XXX  X XX",
    "XX    X   XX                X XX",
    "XX    X   XX  XXXX XXX XX     XX",
    "XX                            XX",
    "XX   X  XXXX XXXXX XXXX XXXX  XX",
    "XX   X                        XX",
    "XX   X  XXX XXX XXX XXX XXXX  XX",
    "XX                            XX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]
################################# FUNCIONES DEL PROGRAMA ######################################################
def dibujar_muro(superficie, rectangulo):  
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_personaje(superficie, rectangulo): #dibuja al personaje1(jugadorAzul) en pantalla
    pygame.draw.rect(superficie, AZUL, rectangulo)
def dibujar_personaje2(superficie, rectangulo): #dibuja al personaje2(jugadorAmarillo) en pantalla
    pygame.draw.rect(superficie, AMARILLO, rectangulo)
def dibujar_vacunas_pildoras(superficie, listapildoras, vacunas): #dibuja las píldoras(items recolectables) y vacunas en pantalla
    for recs in listapildoras:
        pygame.draw.rect(ventana,VERDE, recs)
    for vac in vacunas:
        pygame.draw.rect(ventana,CELESTE,vac)
    
def dibujar_enemigo(superficie, rectangulo):
    pygame.draw.rect(superficie, ROJO, rectangulo)

def construir_mapa(mapa, listapildoras): #recibe como parametro el mapa y la lista que contendrá los items recolectables
    muros=[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == "X":             #cada vez que el ciclo for pase por una X del mapa, dibujará un muro. Si no hay X deja el camino vacío
                muros.append(pygame.Rect(x,y,40,40))
            else:
                listapildoras.append(pygame.Rect(x+10,y+10,15,15)) #cada vez que se pase por un lugar vacío del mapa se dibuja un item recolectable(pildora)
            x+=40
        x=0
        y+=40
    return muros      #devuelve la lista muros que contiene todas las "baldosas" del mapa

def dibujar_mapa(superficie, muros):  #recibe la lista muros 
    for muro in muros:
        dibujar_muro(superficie,muro) # llama a la funcion dibujar_muro la cual como dice su nombre, dibujará los muros en la pantalla
def movimientoEnemigo(enemigo, muertoEnemigo):  #con los siguientes if logro hacer que los enemigos me persigan
    if(muertoEnemigo==False):    #si el enemigo no está muerto, tendrá movimiento determinado por las sentencias dentro del if
        distancia1=0
        distancia2=0
        distX=0
        distY=0                                    #A continuación utilizaremos pitagoras para comparar distancias entre jugadores y enemigos
        distX=enemigo.x-personaje.x                #el enemigo va a ir en búsqueda del jugador que tenga mas cerca
        distY=enemigo.y-personaje.y                #eso lo hacemos midiendo la distancia entre cada enemigo y cada jugador
        dist2X=enemigo.x-personaje2.x              #mediante coordenadas en x y y
        dist2Y=enemigo.y-personaje2.y              #Luego en los if comparo distancias, el jugador que esté mas cerca será perseguido por el enemigo 
        distancia1=([pow(distX,2)+pow(distY,2)])  #distancia del jugador azul respecdto al enemigo
        distancia2=([pow(dist2X,2)+pow(dist2Y,2)])#distancia del jugador amarillo respecto al enemigo
        if perdioAzul==False and perdioAmarillo==False:  #si ninguno de los jugadores han perdido, estos serán perseguidos por los enemigos
            if(distancia1<distancia2):      #si el enemigo tiene al personaje1 mas cerca, lo perseguirá a este
                if enemigo.x>personaje.x:         
                    enemigo.x-=velocidadEnemigo
                    moverseizq=True
                if enemigo.x<personaje.x:
                    enemigo.x+=velocidadEnemigo
                    moverseDer=True
                if enemigo.y>personaje.y:
                    enemigo.y-=velocidadEnemigo
                    moverseArriba=True
                if enemigo.y<personaje.y:
                    enemigo.y+=velocidadEnemigo
                    moverseAbajo=True

            if(distancia1>distancia2):   #si el enemigo tiene al personaje2 mas cerca, lo perseguirá a este
                if enemigo.x>personaje2.x:         
                    enemigo.x-=velocidadEnemigo
                    moverseizq=True
                if enemigo.x<personaje2.x:
                    enemigo.x+=velocidadEnemigo
                    moverseDer=True
                if enemigo.y>personaje2.y:
                    enemigo.y-=velocidadEnemigo
                    moverseArriba=True
                if enemigo.y<personaje2.y:
                    enemigo.y+=velocidadEnemigo
                    moverseAbajo=True
        if perdioAmarillo==True:        #si el personaje2 ha perdido, valido que los COVID solo persigan al personaje1
            if enemigo.x>personaje.x:         
                enemigo.x-=velocidadEnemigo
                moverseizq=True
            if enemigo.x<personaje.x:
                enemigo.x+=velocidadEnemigo
                moverseDer=True
            if enemigo.y>personaje.y:
                enemigo.y-=velocidadEnemigo
                moverseArriba=True
            if enemigo.y<personaje.y:
                enemigo.y+=velocidadEnemigo
                moverseAbajo=True
        if perdioAzul==True:            #si el personaje1 ha perdido, valido que los COVID solo persigan al personaje2
            if enemigo.x>personaje2.x:         
                enemigo.x-=velocidadEnemigo
                moverseizq=True
            if enemigo.x<personaje2.x:
                enemigo.x+=velocidadEnemigo
                moverseDer=True
            if enemigo.y>personaje2.y:
                enemigo.y-=velocidadEnemigo
                moverseArriba=True
            if enemigo.y<personaje2.y:
                enemigo.y+=velocidadEnemigo
                moverseAbajo=True

def colisionEnemigo(enemigo, i):            #con esta funcion controlo las colisiones de enemigos con muros, para que no los atraviesen
    if enemigo.colliderect(muro):                      #si un covid ha chocado con un muro...
        if moverseDer==True and moverseArriba==True:   #si antes de chocar se venía moviendo a la derecha y hacia arriba...
            moverseDer==False                          #interrumpo su movimiento a la derecha para que pueda seguir moviendose hacia arriba si corresponde
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):              #si continúa chocando...
                moverseArriba==False                   #interrumpo su movimiento hacia arriba...
                enemigo.y=anty[i] 
                moverseDer==True                       #..y vuelvo a habilitar su movimiento a la derecha para que pueda seguir hacia la derecha si corresponde
                enemigo.x+=velocidadEnemigo
                if enemigo.colliderect(muro):          #si continúa chocando es porque el covid estaba en una esquina entonces no podía seguir ni para arriba ni para la derecha
                    moverseDer==False                  #entonces interrumpo nuevamente su movimiento a la derecha
                    enemigo.x=antx[i]                  #conservando la ubicacion que tenía al momento de chocar
                    
        elif moverseDer==True and moverseAbajo==True:  #la lógica es igual que la anterior
            moverseDer==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo.y=anty[i] 
                moverseDer==True
                enemigo.x+=velocidadEnemigo
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo.x=antx[i]
                    
        elif moverseizq==True and moverseAbajo==True:   #la lógica es igual que la anterior
            moverseizq==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo.y=anty[i] 
                moverseizq==True
                enemigo.x-=velocidadEnemigo
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo.x=antx[i] 
        elif moverseizq==True and moverseArriba==True:  #la lógica es igual que la anterior
            moverseizq==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseArriba==False
                enemigo.y=anty[i] 
                moverseizq==True
                enemigo.x-=velocidadEnemigo
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo.x=antx[i]
def ComeEnemigos(vac, jugador,i):       #esta funcion me contabiliza la cantidad de covidEliminados cuando un jugador tiene tiempo para comer
    cantComidos=0
    if(tiempo<tiempoparacomer[i]):
        for i in range (e):                 
            if jugador.colliderect(enemigo[i]): #si colisiona algun covid
                print("JUGADOR COMIO ENEMIGO")
                enemigo[i]=pygame.Rect(0,0,0,0) #saco a ese covid del juego
                muertoEnemigo[i]=True           #con este boleano saco a ese covid del juego
                cantComidos=cantComidos+1       #con esta lista controlo la cantidad de covid eliminados o "comidos"
    return cantComidos                          #devuelve la cantidad de covid eliminados
                            
###############################################################CUERPO PRINCIPAL DEL PROGRAMA######################################################

ventana=pygame.display.set_mode((ANCHO,ALTO))    #definimos una ventana de tipo Pygame para dibujar nuestro juego
reloj=pygame.time.Clock()                       #el reloj controla el tiempo del juego
pygame.time.set_timer(pygame.USEREVENT,1000)    

#datos
listapildoras = []                      #lista que contiene a todos los items recolectables por los pacman
vacunas=[]                              #esta lista guarda las vacunas que daran al pacman inmunidad para eliminar covid en caso que colecten una vacuna
enemigosEliminados=[0,0]                #Esta lista llevará el conteo de la cantidad de enemigos eliminados por el personaje1 y por el personaje2
direccion=""                            #Esta cadena tomará valores "arriba, abajo, derecha o izquierda" controlando el movimiento del personaje1
direccion2=""                           #idem para el personaje 2. Utilizaremos estas variables al momento que se produzca colisión con los muros

perdioAzul=False                        #con este boleano controlaremos si el personaje 1 a perdido el juego o no
perdioAmarillo=False                    #con este boleano controlaremos si el personaje 2 a perdido el juego o no
pildorasConsumidas=[0,0]                #Con esta lista controlamos la cantidad de item recolectados por cada pacman
#x=0

velocidad=6        #constante para controlar la velocidad de movimiento del personaje
velocidadEnemigo=3 #constante para controlar la velocidad de movimiento del enemigo, si desea menor dificultad en el juego puede aumentar el valor de esta variable o viceversa

WASD = [False, False, False, False] #con esta lista boolean se controla cuando se mantiene apretada una tecla de movimiento del jugador 1.
WASD2 = [False, False, False, False]#idem para el jugador o personaje 2

enemigo=[]          #en esta lista guardaremos la cantidad de enemigos Covid
e=5                 #variable para controlar la cantidad de enemigos
w=0              #w y z son las coordenadas de los Covid
z=0 
for i in range (e): #En este ciclo for agregamos a los Covid a la lista
    w=80
    z=z+100
    enemigo.append(pygame.Rect(w,z,30,30))
muertoEnemigo=[False, False, False, False,False] #con esta lista en caso que uno de los enemigos sea eliminado, toma valor true y lo saca del juego
antx=[0,0,0,0,0]  # lista que guardan las posiciones de los enemigos en eje x
anty=[0,0,0,0,0]  # lista que guardan las posiciones de los enemigos en eje y 
moverseizq=True   #controla desplazamiento a la izquierda de enemigo
moverseDer=True #controla desplazamiento a la derecha de enemigo
moverseArriba=True #controla desplazamiento hacia arriba de enemigo
moverseAbajo=True #controla desplazamiento hacia abajo de enemigo

jugando = True  #controla el bucle principal del juego
tiempo=0        #variable que controla el tiempo de ejecucion del programa
tiempoparacomer=[0,0]#guardará el tiempo que tiene un pacman para eliminar Covids, luego de recolectar una vacuna
cantJugadores=menu.pantallaMenu() #Llamando al Menu inicial que se encuentra en el otro módulo. Retorna el valor de la cantidad de jugadores

jugador2=False    #variable que controlará si existe el jugador 2
print("Cantidad de jugadores: ", cantJugadores) #solo para ver en la consola la cantidad de jugadores
if cantJugadores==1:   #si hay un solo jugador saco al jugador2(amarillo)
    perdioAmarillo=True
    vacunas.append(pygame.Rect(113,300,10,30))
    vacunas.append(pygame.Rect(113,300,10,30))
    personaje= pygame.Rect(1170,530,30,30)  #creamos al personaje o jugador 1. Entre paréntesis se define ubicación y tamanio
    personaje2=pygame.Rect(1170,80,30,30)   #creamos al personaje o jugador 2. Entre paréntesis se define ubicación y tamanio
    muros=construir_mapa(mapaUnJugador, listapildoras) #se llama a la función contruir_mapa y se le pasa como parametro el mapa para un solo jugador
elif cantJugadores==2: #si juegan los dos personajes hago True a la variable jugador2
    jugador2=True
    vacunas.append(pygame.Rect(193,40,10,30))
    vacunas.append(pygame.Rect(193,570,10,30))
    personaje= pygame.Rect(1210,570,30,30)  #creamos al personaje o jugador 1. Entre paréntesis se define ubicación y tamanio
    personaje2=pygame.Rect(1210,40,30,30)   #creamos al personaje o jugador 2. Entre paréntesis se define ubicación y tamanio
    muros=construir_mapa(mapa, listapildoras) #a la funcion construir mapa se le pasa el parametro mapa que es el determinado para dos jugadores
else:                                       #si no selecciona jugadores y cierra la ventana, se cierra el juego
    jugando==False
    pygame.quit()
while jugando:     #bucle principal del juego

    for event in pygame.event.get():       #event.get() detecta cuando se presiona una tecla
        if event.type==pygame.USEREVENT:    #controla el paso del tiempo en segundos
            tiempo+=1                       #En esta variable vamos guardando el tiempo transcurrido del juego en segundos
            print(tiempo)                   #imprimo en consola el tiempo solo para ver
        if event.type == pygame.QUIT: 
        
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:    #si se presiona una tecla

            if event.key==pygame.K_ESCAPE:  #ESC para salir del juego
                jugando= False
            
            if event.key == pygame.K_w:   #movimiento para el personaje1 hacia arriba presionando 'w'
                
                WASD[0] = True          #vuelve True al primer elemento de la lista asignado a 'w'. Permanece True mientras se mantenga presionada la tecla
                direccion="arriba"      #esta variable la utilizaremos para controlar la colision con los muros
            if event.key == pygame.K_s:   #abajo
                
                WASD[2] = True
                direccion="abajo"
            if event.key == pygame.K_a:   #izquierda
                
                WASD[1] = True
                direccion="izquierda"
            if event.key == pygame.K_d:   #derecha
            
                WASD[3] = True
                direccion="derecha"
                
            if event.key==pygame.K_UP:  #movimiento para el personaje2. Funciona con la misma lógica que el movimiento del personaje1
                WASD2[0] = True
                direccion2="arriba"
            if event.key==pygame.K_DOWN:
                WASD2[2] = True
                direccion2="abajo"
            if event.key==pygame.K_LEFT:
                WASD2[1] = True
                direccion2="izquierda"
            if event.key==pygame.K_RIGHT:
                WASD2[3] = True
                direccion2="derecha"
                
        if event.type == pygame.KEYUP:   #Para el personaje1.Si deja de presionar la tecla vuelvo False la lista que controla si dicha tecla está apretada             
            if event.key == pygame.K_w:  
                WASD[0] = False
            if event.key == pygame.K_s:       
                WASD[2] = False            
            if event.key == pygame.K_a:            
                WASD[1] = False                    
            if event.key == pygame.K_d:                
                WASD[3] = False
                
            if event.key==pygame.K_UP: #Idem para el personaje 2
                WASD2[0] = False                
            if event.key==pygame.K_DOWN:
                WASD2[2] = False                
            if event.key==pygame.K_LEFT:
                WASD2[1] = False
            if event.key==pygame.K_RIGHT:
                WASD2[3] = False
                
    reloj.tick(60)
    ventana.fill(NEGRO)
    if WASD[0]:                 #Para el personaje1 en caso que se mantenga apretada una tecla, el personaje experimentará un movimiento respecto...
        personaje.y-=velocidad  #a sus coordenadas en x y e, haciéndolo mover tantos pixeles según lo determine la variable velocidad
    if WASD[1]:
        personaje.x-=velocidad
    if WASD[2]:
        personaje.y+=velocidad
    if WASD[3]:
        personaje.x+=velocidad

    if WASD2[0]:            #Idem para el personaje2
        personaje2.y-=velocidad  
    if WASD2[1]:
        personaje2.x-=velocidad
    if WASD2[2]:
        personaje2.y+=velocidad
    if WASD2[3]:
        personaje2.x+=velocidad

    for i in range (e):         #con este ciclo for llamo a la funcion movimientoEnemigo que recibe como parametros los enemigos para darles movimiento
        movimientoEnemigo(enemigo[i], muertoEnemigo[i]) #el parametro muertoEnemigo será el que controle si ese enemigo se mueve o no en caso de estar vivo o muerto
    
#el siguiente ciclo for me sirve para controlar las colisiones con los muros, hubo que hacer varias pruebas
#porque me hacía errores al presionar dos teclas, por ej al llegar a una esquina presionando dos teclas
#el personaje atravesaba el muro y aparecía en cualquier lado, ya está corregido
    for muro in muros:
        if personaje.colliderect(muro):   ##CONTROLA COLISIONES CON MUROS DE PERSONAJE 1
            if direccion=="abajo" and direccion=="derecha":
                WASD[2]=False
                WASD[3]=False
            elif direccion=="abajo" and direccion=="izquierda":
                WASD[2]=False
                WASD[1]=False
            elif direccion=="arriba" and direccion=="derecha":
                WASD[0]=False
                WASD[3]=False
            elif direccion=="arriba" and direccion=="izquierda":
                WASD[0]=False
                WASD[1]=False
            elif direccion=="abajo":
                WASD[2]=False
                if direccion=="derecha":
                    if personaje.colliderect(muro):
                        WASD[3]=False
                        
                if direccion=="izquierda":
                    if personaje.colliderect(muro):
                        WASD[1]=False 
                        
            elif direccion=="arriba":
                WASD[0]=False
                if direccion=="derecha":
                    if personaje.colliderect(muro):
                        WASD[3]=False
                if direccion=="izquierda":
                    if personaje.colliderect(muro):
                        WASD[1]=False 

            elif direccion=="derecha":
                WASD[3]=False
                if direccion=="arriba":
                    if personaje.colliderect(muro):
                        WASD[0]=False
                if direccion=="abajo":
                    if personaje.colliderect(muro):
                        WASD[2]=False 
                
            elif direccion=="izquierda":
                WASD[1]=False
                if direccion=="arriba":
                    if personaje.colliderect(muro):
                        WASD[0]=False
                if direccion=="abajo":
                    if personaje.colliderect(muro):
                        WASD[2]=False 
            personaje.x=oldx 
            personaje.y=oldy
            
        if personaje2.colliderect(muro):     ### IDEM PARA PERSONAJE2
            if direccion2=="abajo" and direccion2=="derecha":
                WASD2[2]=False
                WASD2[3]=False
            elif direccion2=="abajo" and direccion2=="izquierda":
                WASD2[2]=False
                WASD2[1]=False
            elif direccion2=="arriba" and direccion2=="derecha":
                WASD2[0]=False
                WASD2[3]=False
            elif direccion2=="arriba" and direccion2=="izquierda":
                WASD2[0]=False
                WASD2[1]=False
            elif direccion2=="abajo":
                WASD2[2]=False
                if direccion2=="derecha":
                    if personaje2.colliderect(muro):
                        WASD2[3]=False
                        
                if direccion2=="izquierda":
                    if personaje2.colliderect(muro):
                        WASD2[1]=False 
                        
            elif direccion2=="arriba":
                WASD2[0]=False
                if direccion2=="derecha":
                    if personaje2.colliderect(muro):
                        WASD2[3]=False
                if direccion2=="izquierda":
                    if personaje2.colliderect(muro):
                        WASD2[1]=False 

            elif direccion2=="derecha":
                WASD2[3]=False
                if direccion2=="arriba":
                    if personaje2.colliderect(muro):
                        WASD2[0]=False
                if direccion2=="abajo":
                    if personaje2.colliderect(muro):
                        WASD2[2]=False 
                
            elif direccion2=="izquierda":
                WASD2[1]=False
                if direccion2=="arriba":
                    if personaje2.colliderect(muro):
                        WASD2[0]=False
                if direccion2=="abajo":
                    if personaje2.colliderect(muro):
                        WASD2[2]=False 
            personaje2.x=oldx2
            personaje2.y=oldy2
        for i in range (e):    
            colisionEnemigo(enemigo[i],i)

    for i in range (e):         
        anty[i]=enemigo[i].y
        antx[i]=enemigo[i].x

    oldx = personaje.x  #en las variables 'old' se guardan las coordenadas que tenia antes que colisionara con el muro para que no lo atraviese y se frene al chocar
    oldy = personaje.y
    oldx2 = personaje2.x 
    oldy2 = personaje2.y    

    for recs in listapildoras:  #ciclo for que recorre los items recolectables
        if personaje.colliderect(recs):
            if recs.width>0:   #si el item aun no ha sido recolectado tendra un tamaño mayor que cero
                pildorasConsumidas[0]=pildorasConsumidas[0]+1#si el personaje colisiona un item se le suma una unidad en la lista pildorasConsumidas
                #print("Pildoras Consumidas jugador AZUL: ", pildorasConsumidas[0])
            recs.width=0 #si recolectó un item, ese item lo reduzco a cero
            recs.height=0
        if personaje2.colliderect(recs): #idem para el personaje 2
            if recs.width>0:
                pildorasConsumidas[1]=pildorasConsumidas[1]+1
                #print("Pildoras Consumidas jugador AMARILLO: ", pildorasConsumidas[1])
            recs.width=0
            recs.height=0   
    for i in range (e): #ciclo for que recorre la lista de enemigos  
        if personaje.colliderect(vacunas[0]) or personaje.colliderect(vacunas[1]) or tiempoparacomer[0]>tiempo:
        #si el personaje colisiona una vacuna se le asigna tiempo para comer. Si ese tiempo para comer es mayor que cero
            for vac in vacunas: #recorro lista de vacunas
                if personaje.colliderect(vac): #si colisiona alguna vacuna
                    if vac.width>0: 
                        #print("Pildoras Consumidas jugador AZUL: ", pildorasConsumidas[0])
                        vac.width=0  #si colisionó vacuna la reduzco a cero ya que no puede volver a ser recolectada
                        vac.height=0
                        tiempoparacomer[0]=tiempo+5 #luego de recolectar la vacuna se le dan cinco segundos al personaje para que elimine COVIDs
                        print("tiempoparacomer",tiempoparacomer[0])
            enemigosEliminados[0]=enemigosEliminados[0]+ComeEnemigos(vac, personaje,0) #si el jugador colisionó algún COVID le sumo una unidad en la lista 
        elif personaje.colliderect(enemigo[i]): #si el personaje no recolecto vacunas y choca con algún COVID perderá
            print("Perdiste JUGADOR AZUL")
            print("Pildoras Consumidas: ", pildorasConsumidas[0])
            personaje=pygame.Rect(0,0,0,0)  #lo saco del tablero al personaje
            perdioAzul=True  #y valido que perdió
        if personaje2.colliderect(vacunas[0]) or personaje2.colliderect(vacunas[1]) or tiempoparacomer[1]>tiempo: #IDEM para el personaje2
            for vac in vacunas:
                if personaje2.colliderect(vac):
                    if vac.width>0:
                        #print("Pildoras Consumidas jugador AZUL: ", pildorasConsumidas[0])
                        vac.width=0
                        vac.height=0
                        tiempoparacomer[1]=tiempo+5
                        print("tiempoparacomer2",tiempoparacomer[1])

            enemigosEliminados[1]=enemigosEliminados[1]+ComeEnemigos(vac, personaje2,1)
        elif personaje2.colliderect(enemigo[i]): 
            print("Perdiste JUGADOR AMARILLO")
            print("Pildoras Consumidas: ", pildorasConsumidas[1])
            personaje2=pygame.Rect(0,0,0,0)
            perdioAmarillo=True

    if perdioAmarillo==True and perdioAzul==True: # si los dos jugadores perdieron muestro en pantalla las estadísticas del juego
        ventana.fill(BLANCO)
        miFuente=pygame.font.Font(None,30)
        miTexto=miFuente.render("GAME OVER :(",0,(200,60,80))
        miTexto1=miFuente.render("TE HAS CONTAGIADO COVID... INTENTALO DE NUEVO",0,(200,60,80))
        texto= "JUGADOR AZUL PILDORAS RECOLECTADAS: "+ str(pildorasConsumidas[0])+"  COVID ELIMINADOS: "+str(enemigosEliminados[0])
        miTexto2=miFuente.render(texto,0,(200,60,80))
        texto= "JUGADOR AMARILLO PILDORAS RECOLECTADAS: "+ str(pildorasConsumidas[1])+"  COVID ELIMINADOS: "+str(enemigosEliminados[1])
        miTexto3=miFuente.render(texto,0,(200,60,80))
        salir=False
        while salir!=True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    jugando=False
                    ventana.fill(BLANCO)
                    salir=True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        jugando=False
                        ventana.fill(BLANCO)
                        salir=True
                        break
            ventana.blit(miTexto,(300,50))
            ventana.blit(miTexto1,(300,100))
            ventana.blit(miTexto2,(300,200))
            if jugador2==True: #solo si el jugador2 estaba participando del juego muestro sus estadísticas
                ventana.blit(miTexto3,(300,300))
            pygame.display.update()
    if jugador2==False and muertoEnemigo==[True,True,True,True,True]:
        ventana.fill(BLANCO)    #limpia la pantalla de color blanco
        miFuente=pygame.font.Font(None,30)
        miTexto=miFuente.render("JUGADOR AZUL HAS GANADO EL JUEGO!!!",0,(200,60,80))
        miTexto1=miFuente.render("HAS LOGRADO RESISTIR AL COVID",0,(200,60,80))
        texto= "JUGADOR AZUL PILDORAS RECOLECTADAS: "+ str(pildorasConsumidas[0])+" COVID ELIMINADOS: "+str(enemigosEliminados[0])
        miTexto2=miFuente.render(texto,0,(200,60,80))
        
        salir=False
        while salir!=True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    jugando=False
                    ventana.fill(BLANCO)
                    salir=True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        jugando=False
                        ventana.fill(BLANCO)
                        salir=True
                        break
            ventana.blit(miTexto,(300,50))
            ventana.blit(miTexto1,(300,100))
            ventana.blit(miTexto2,(300,200))
            pygame.display.update()
    if pildorasConsumidas[0]+pildorasConsumidas[1]==len(listapildoras): #si los jugadores ya se comieron todos los item recolectables ganan el juego
        ventana.fill(BLANCO)    #limpia la pantalla de color blanco
        miFuente=pygame.font.Font(None,30)
        if pildorasConsumidas[0]>pildorasConsumidas[1] and perdioAzul==False:  #si no perdió el personaje1(azul) y recogió mas items muestro el mensaje
            miTexto=miFuente.render("JUGADOR AZUL HAS GANADO EL JUEGO!!!",0,(200,60,80))
        else:
            miTexto=miFuente.render("JUGADOR AMARILLO HAS GANADO EL JUEGO!!!",0,(200,60,80))
        miTexto1=miFuente.render("HAN LOGRADO RESISTIR AL COVID",0,(200,60,80))
        texto= "JUGADOR AZUL PILDORAS RECOLECTADAS: "+ str(pildorasConsumidas[0])+" COVID ELIMINADOS: "+str(enemigosEliminados[0])
        miTexto2=miFuente.render(texto,0,(200,60,80))
        texto= "JUGADOR AMARILLO PILDORAS RECOLECTADAS: "+ str(pildorasConsumidas[1])+" COVID ELIMINADOS: "+str(enemigosEliminados[1])
        miTexto3=miFuente.render(texto,0,(200,60,80))
        salir=False
        while salir!=True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    jugando=False
                    ventana.fill(BLANCO)
                    salir=True
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        jugando=False
                        ventana.fill(BLANCO)
                        salir=True
                        break
            ventana.blit(miTexto,(300,50))
            ventana.blit(miTexto1,(300,100))
            ventana.blit(miTexto2,(300,200))
            if jugador2==True:  #solo si el jugador2 estaba participando del juego muestro sus estadísticas
                ventana.blit(miTexto3,(300,300))
            pygame.display.update()

    #dibujos MAPA, JUGADORES, ENEMIGOS, PILDORAS, VACUNAS
    dibujar_mapa(ventana, muros) #llamamos a la funcion para que dibuje el mapa. Se le pasa como parametro la venana pygame, y los muros
    if perdioAzul==False:       #si no ha perdido el personaje1(azul) lo dibujamos
        dibujar_personaje(ventana,personaje)
    if perdioAmarillo==False and jugador2==True: #si no ha perdido el personaje2(amarillo) lo dibujamos
        dibujar_personaje2(ventana,personaje2)
    dibujar_vacunas_pildoras(ventana,listapildoras,vacunas)#llama a la funcion que dibuja las pildoras(items recolectables) y vacunas

    for i in range (e):
        dibujar_enemigo(ventana,enemigo[i])  #dibuja todos los enemigos
    #Actualizar Pantalla
    if tiempoparacomer[1]>tiempo: #si el personaje2(amarillo) ha comido una vacuna tiene tiempo para comer, entra en este bucle y muestra el tiempo en pantalla
        Fuente=pygame.font.Font(None,30)
        mensaje="Jugador amarillo tienes 5 segundos para eliminar COVID!!! TIEMPO RESTANTE: "+ str(tiempoparacomer[1]-tiempo)
        text=Fuente.render(mensaje,0,(0,0,0))
        ventana.blit(text,(200,600))
    if tiempoparacomer[0]>tiempo:#si el personaje1(azul) ha comido una vacuna tiene tiempo para comer, entra en este bucle y muestra el tiempo en pantalla
        Fuente=pygame.font.Font(None,30)
        mensaje="Jugador AZUL tienes 5 segundos para eliminar COVID!!! TIEMPO RESTANTE: "+ str(tiempoparacomer[0]-tiempo)
        text=Fuente.render(mensaje,0,(0,0,0))
        ventana.blit(text,(200,600))    
    
    pygame.display.update()

pygame.quit()

