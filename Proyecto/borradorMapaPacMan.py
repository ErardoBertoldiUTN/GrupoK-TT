#ya se logró el movimiento continuo, cambié las teclas de movimiento por letras porq son más cómodas de usar en el teclado de las flechas
#debo corregir que ahora si el personaje se desplaza en diagonal al tocar un muro se frena y yo quiero que continúe deslizándose por el muro según la teclas teclas de movimiento que esté presionando

import pygame
from pygame import Rect
#inicializar
pygame.init()

#medidas
ANCHO=1270
ALTO=640

#colores
NEGRO=(0,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
MARRON=(150,70,10)
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

#Ventana
ventana=pygame.display.set_mode((ANCHO,ALTO))
reloj=pygame.time.Clock()

#datos
muros=construir_mapa(mapa)
direccion=""
personaje= pygame.Rect(40,40,30,30)  #los primeros dos números son la posición en la que aparecerá una vez ejecutado el programa, las siguientes dos numeros refieren al tamaño
personaje_vel_x=0                   #coordenadas de ubicacion del personaje
personaje_vel_y=0
velocidad=10                         #constante para controlar la velocidad de movimiento del personaje
WASD = [False, False, False, False]#con esta lista boolean se controla cuando se mantiene apretada una tecla de movimiento
#bucle ppal
jugando = True
while jugando:
    
    #eventos
##    for event in pygame.event.get():
##        if event.type==pygame.QUIT:
##            jugando=False
##        if event.type==pygame.KEYDOWN:
##            if event.key==pygame.K_ESCAPE:
##                jugando= False
##                
##            if event.key==pygame.K_d:
##                direccion="derecha"
##                WASD[0]=True
##                if WASD[0]==True:
##                    personaje_vel_x+=velocidad
##            if event.key==pygame.K_LEFT:
##                direccion="izquierda"
##                personaje_vel_x+=-velocidad
##            if event.key==pygame.K_DOWN:
##                direccion="abajo"
##                personaje_vel_y=velocidad
##            if event.key==pygame.K_UP:
##                direccion="arriba"
##                personaje_vel_y=-velocidad
##        if event.type==pygame.KEYUP:
##            if event.key==pygame.K_d:
##                personaje_vel_x=0
##            if event.key==pygame.K_LEFT:
##                personaje_vel_x=0
##            if event.key==pygame.K_DOWN:
##                personaje_vel_y=0
##            if event.key==pygame.K_UP:
##                personaje_vel_y=0
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT: 
        
            pygame.quit()
        
        if event.type == pygame.KEYDOWN: 
            if event.key==pygame.K_ESCAPE:
                jugando= False
            
            if event.key == pygame.K_w: 
                
                WASD[0] = True
                direccion="arriba"
            if event.key == pygame.K_s: 
                
                WASD[2] = True
                direccion="abajo"
            if event.key == pygame.K_a: 
                
                WASD[1] = True
                direccion="izquierda"
            if event.key == pygame.K_d: 
            
                WASD[3] = True
                direccion="derecha"
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_w:
            
                WASD[0] = False
            
            if event.key == pygame.K_s:
            
                WASD[2] = False
            
            if event.key == pygame.K_a:
            
                WASD[1] = False
                    
            if event.key == pygame.K_d:
                
                WASD[3] = False
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
##    if event.type == pygame.QUIT: 
##            pygame.quit()
##    if personaje.x> ANCHO - personaje.width:
##        personaje.x=ANCHO - personaje.width
##    if personaje.x<0:
##        personaje.x=0
##    if personaje.y>ALTO - personaje.height:
##        personaje.y=ALTO-personaje.height
##    if personaje.y<0:
##        personaje.y=0
##
##    if personaje.x> ANCHO - personaje.width:
##        personaje.x=ANCHO - personaje.width
##    if personaje.x<0:
##        personaje.x=0
##    if personaje.y>ALTO - personaje.height:
##        personaje.y=ALTO-personaje.height
##    if personaje.y<0:
##        personaje.y=0

##    for muro in muros:
##        if personaje.colliderect(muro):
##            if direccion == "abajo":
##                personaje.bottom=muro.top
##            if direccion=="arriba":
##                personaje.top=muro.bottom
##            if direccion == "derecha":
##                personaje.right = muro.left
##            if direccion == "izquierda":
##                personaje.left = muro.right
    for muro in muros:
        if personaje.colliderect(muro):
            personaje.left=oldx
            personaje.top=oldy
##            if direccion=="abajo" and direccion=="derecha":
##                personaje.x = oldx
##                personaje.y = oldy
##            if direccion=="abajo" and direccion=="izquierda":
##                personaje.x = oldx
##                personaje.y = oldy
##            if direccion=="arriba" and direccion=="derecha":
##                personaje.x = oldx
##                personaje.y = oldy
##            if direccion=="arriba" and direccion=="izquierda":
##                personaje.x = oldx
##                personaje.y = oldy
##            if direccion=="abajo":
##                personaje.y = oldy
##            if direccion=="arriba":
##                personaje.y = oldy
##            if direccion=="derecha":
##                personaje.x=oldx
##            if direccion=="izquierda":
##                personaje.x=oldx
    oldx = personaje.x
    oldy = personaje.y

    #dibujos
    
    dibujar_mapa(ventana, muros)
    dibujar_personaje(ventana,personaje)

    #Actualizar
    pygame.display.update()

pygame.quit()


























            
