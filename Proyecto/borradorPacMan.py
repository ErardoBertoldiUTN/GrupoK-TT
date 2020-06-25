#ya se logró el movimiento continuo, cambié las teclas de movimiento por letras porq son más cómodas de usar en el teclado de las flechas
#movimiento de enemigo corregido funcionando bien!!
import os
import pygame

from pygame import Rect
#inicializar
os.environ['SDL_VIDEO_CENTERED'] = '1'  #para que me aparezca centrada en el monitor la ventana pygame
pygame.init()

#medidas
ANCHO=1270
ALTO=640

#colores
NEGRO=(0,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
MARRON=(150,70,10)
ROJO=(255,0,0)
AMARILLO=(255,255,0)
#Mapas
#1270/40=32 baldosas a lo ancho
#640/40=16 baldosas a lo largo
mapa=[
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                              X",
    "X     XXXXXXXXXXXXXXXXXXXX  X  X",
    "X                           X  X",
    "X         XXX  XXXXXX  XXX     X",
    "X   X                      X   X",
    "X    X       XXXXXXXXXXXX  X   X",
    "X     X                    X   X",
    "X      X     XXXXXXXXXX        X",
    "X                              X",
    "X   X  XXXXXXXXXXXXXXXXXXXX    X",
    "X   X                          X",
    "X   X  XXXXXXXXXXXXXXXXXXXX    X",
    "X   X                          X",
    "X                              X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    ]

#funciones
def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)
def dibujar_personaje2(superficie, rectangulo):
    pygame.draw.rect(superficie, AMARILLO, rectangulo)
def dibujar_pildoras(superficie, rectangulo):
    for recs in listapildoras:
        pygame.draw.rect(ventana,VERDE, recs)
    
def dibujar_enemigo(superficie, rectangulo):
    pygame.draw.rect(superficie, ROJO, rectangulo)

def construir_mapa(mapa):
    muros=[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                muros.append(pygame.Rect(x,y,40,40))
            x+=40
        x=0
        y+=40
    return muros

def dibujar_mapa(superficie, muros):
    for muro in muros:
        dibujar_muro(superficie,muro)
def movimientoEnemigo(enemigo):
    if enemigo.x>personaje.x:         
        enemigo.x-=1
        moverseizq=True
    if enemigo.x<personaje.x:
        enemigo.x+=1
        moverseDer=True
    if enemigo.y>personaje.y:
        enemigo.y-=1
        moverseArriba=True
    if enemigo.y<personaje.y:
        enemigo.y+=1
        moverseAbajo=True
    return enemigo
def colisionEnemigo(enemigo):
    if enemigo.colliderect(muro):
        if moverseDer==True and moverseArriba==True:
            moverseDer==False
            enemigo.x=antx 
            if enemigo.colliderect(muro):
                moverseArriba==False
                enemigo.y=anty
                moverseDer==True
                enemigo.x+=1
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo.x=antx
                
        elif moverseDer==True and moverseAbajo==True:
            moverseDer==False
            enemigo.x=antx
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo.y=anty
                moverseDer==True
                enemigo.x+=1
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo.x=antx
        elif moverseizq==True and moverseAbajo==True:
            moverseizq==False
            enemigo.x=antx
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo.y=anty
                moverseizq==True
                enemigo.x-=1
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo.x=antx
        elif moverseizq==True and moverseArriba==True:
            moverseizq==False
            enemigo.x=antx
            if enemigo.colliderect(muro):
                moverseArriba==False
                enemigo.y=anty
                moverseizq==True
                enemigo.x-=1
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo.x=antx
    return enemigo
def colisionEnemigo2(enemigo2):
    if enemigo2.colliderect(muro):
        if moverseDer==True and moverseArriba==True:
            moverseDer==False
            enemigo2.x=antx2 
            if enemigo2.colliderect(muro):
                moverseArriba==False
                enemigo2.y=anty2
                moverseDer==True
                enemigo2.x+=1
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo2.x=antx2
                
        elif moverseDer==True and moverseAbajo==True:
            moverseDer==False
            enemigo2.x=antx2
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo2.y=anty2
                moverseDer==True
                enemigo2.x+=1
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo2.x=antx2
        elif moverseizq==True and moverseAbajo==True:
            moverseizq==False
            enemigo2.x=antx2
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo2.y=anty2
                moverseizq==True
                enemigo2.x-=1
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo2.x=antx2
        elif moverseizq==True and moverseArriba==True:
            moverseizq==False
            enemigo2.x=antx2
            if enemigo.colliderect(muro):
                moverseArriba==False
                enemigo2.y=anty2
                moverseizq==True
                enemigo2.x-=1
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo2.x=antx2
    return enemigo2
##Ventana
ventana=pygame.display.set_mode((ANCHO,ALTO))
reloj=pygame.time.Clock()

#datos
muros=construir_mapa(mapa)
direccion=""

personaje= pygame.Rect(1190,560,30,30)  #los primeros dos números son la posición en la que aparecerá una vez ejecutado el programa, las siguientes dos numeros refieren al tamaño
personaje2=pygame.Rect(40,560,30,30)
listapildoras = []
pildorasConsumidas=0
x=0
for i in range (30):
    y=50
    x=x+40
    listapildoras.append(pygame.Rect(x,y,15,15))

velocidad=10                         #constante para controlar la velocidad de movimiento del personaje
#con la siguiente lista boolean se controla cuando se mantiene apretada una tecla de movimiento.
#Después vi que existía una función getpressed que me lo hubiese hecho mas facil, pero igual con esta forma funciona
WASD = [False, False, False, False]
WASD2 = [False, False, False, False]
enemigo=pygame.Rect(40,40,30,30)  #inicialmente creamos un enemigo para que nos persiga, después agregaremos mas enemigos
enemigo2=pygame.Rect(40,200,30,30)
moverseizq=True
moverseDer=True
moverseArriba=True
moverseAbajo=True
#bucle ppal
jugando = True
while jugando:

    for event in pygame.event.get():       #event.get() detecta cuando se presiona una tecla
    
        if event.type == pygame.QUIT: 
        
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:

            if event.key==pygame.K_ESCAPE:
                jugando= False
            
            if event.key == pygame.K_w:   #arriba
                
                WASD[0] = True
                direccion="arriba"
            if event.key == pygame.K_s:   #abajo
                
                WASD[2] = True
                direccion="abajo"
            if event.key == pygame.K_a:   #izquierda
                
                WASD[1] = True
                direccion="izquierda"
            if event.key == pygame.K_d:   #derecha
            
                WASD[3] = True
                direccion="derecha"
                
            if event.key==pygame.K_UP:
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

                
        if event.type == pygame.KEYUP:                
            if event.key == pygame.K_w:  
                WASD[0] = False
            if event.key == pygame.K_s:       
                WASD[2] = False            
            if event.key == pygame.K_a:            
                WASD[1] = False                    
            if event.key == pygame.K_d:                
                WASD[3] = False
                
            if event.key==pygame.K_UP:
                WASD2[0] = False                
            if event.key==pygame.K_DOWN:
                WASD2[2] = False                
            if event.key==pygame.K_LEFT:
                WASD2[1] = False
            if event.key==pygame.K_RIGHT:
                WASD2[3] = False
                

    reloj.tick(60)
    ventana.fill(NEGRO)
    if WASD[0]:
        personaje.y-=velocidad  
    if WASD[1]:
        personaje.x-=velocidad
    if WASD[2]:
        personaje.y+=velocidad
    if WASD[3]:
        personaje.x+=velocidad

    if WASD2[0]:
        personaje2.y-=velocidad  
    if WASD2[1]:
        personaje2.x-=velocidad
    if WASD2[2]:
        personaje2.y+=velocidad
    if WASD2[3]:
        personaje2.x+=velocidad

#con los siguientes if logro hacer que el enemigo me persiga
    enemigo2=movimientoEnemigo(enemigo2)
    enemigo=movimientoEnemigo(enemigo)
    
#el siguiente ciclo for me sirve para controlar las colisiones con los muros, hubo que hacer varias pruebas
#porque me hacía errores al presionar dos teclas, por ej al llegar a una esquina presionando dos teclas
#el personaje atravesaba el muro y aparecía en cualquier lado
    for muro in muros:
        if personaje.colliderect(muro):
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
#                personaje.x=oldx
                WASD[2]=False
                if direccion=="derecha":
                    if personaje.colliderect(muro):
                        WASD[3]=False
                        
                if direccion=="izquierda":
                    if personaje.colliderect(muro):
                        WASD[1]=False 
                        
            elif direccion=="arriba":
#                personaje.x=oldx
                WASD[0]=False
                if direccion=="derecha":
                    if personaje.colliderect(muro):
                        WASD[3]=False
                if direccion=="izquierda":
                    if personaje.colliderect(muro):
                        WASD[1]=False 

            elif direccion=="derecha":
#                personaje.y=oldy
                WASD[3]=False
                if direccion=="arriba":
                    if personaje.colliderect(muro):
                        WASD[0]=False
                if direccion=="abajo":
                    if personaje.colliderect(muro):
                        WASD[2]=False 
                
            elif direccion=="izquierda":
#                personaje.y=oldy
                WASD[1]=False
                if direccion=="arriba":
                    if personaje.colliderect(muro):
                        WASD[0]=False
                if direccion=="abajo":
                    if personaje.colliderect(muro):
                        WASD[2]=False 
            personaje.x=oldx
            personaje.y=oldy

        enemigo2=colisionEnemigo2(enemigo2)
        enemigo=colisionEnemigo(enemigo)
             
    anty=enemigo.y
    antx=enemigo.x
    antx2=enemigo2.x
    anty2=enemigo2.y
    oldx = personaje.x 
    oldy = personaje.y
    

    for recs in listapildoras:
        if personaje.colliderect(recs):
            if recs.width>0:
                pildorasConsumidas=pildorasConsumidas+1
                print("Pildoras Consumidas: ", pildorasConsumidas)
            recs.width=0
            recs.height=0
            
    
    if personaje.colliderect(enemigo) or personaje.colliderect(enemigo2):
        print("Perdiste")
        print("Pildoras Consumidas: ", pildorasConsumidas)
        jugando=False

    
    #dibujos
    dibujar_mapa(ventana, muros)
    dibujar_personaje(ventana,personaje)
    dibujar_personaje2(ventana,personaje2)
    dibujar_pildoras(ventana,listapildoras)
    dibujar_enemigo(ventana,enemigo)
    dibujar_enemigo(ventana,enemigo2)
    #Actualizar
    pygame.display.update()

pygame.quit()


























            
