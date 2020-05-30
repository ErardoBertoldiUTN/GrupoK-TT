import pygame
from pygame import Rect
#inicializar
pygame.init()

#medidas
ANCHO=1280
ALTO=700

#colores
NEGRO=(0,0,0)
AZUL=(0,0,255)
MARRON=(0,255,0)

#funciones
def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)

#Ventana
ventana=pygame.display.set_mode((ANCHO,ALTO))
reloj=pygame.time.Clock()

#datos
muros = [
    pygame.Rect(500,100,300,100),
    pygame.Rect(200,200,100,100),
    pygame.Rect(500,500,300,100),
    pygame.Rect(1000,200,100,300)]
                                    
personaje= pygame.Rect(600,400,50,50)
personaje_vel_x=0
personaje_vel_y=0
velocidad=17
WASD = [False, False, False, False]
#bucle ppal
jugando = True
while jugando:
    reloj.tick(60)
    #eventos
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            jugando=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                jugando= False
                
            if event.key==pygame.K_d:
                direccion="derecha"
                WASD[0]=True
                if WASD[0]==True:
                    personaje_vel_x+=velocidad
            if event.key==pygame.K_LEFT:
                direccion="izquierda"
                personaje_vel_x+=-velocidad
            if event.key==pygame.K_DOWN:
                direccion="abajo"
                personaje_vel_y=velocidad
            if event.key==pygame.K_UP:
                direccion="arriba"
                personaje_vel_y=-velocidad
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_d:
                personaje_vel_x=0
            if event.key==pygame.K_LEFT:
                personaje_vel_x=0
            if event.key==pygame.K_DOWN:
                personaje_vel_y=0
            if event.key==pygame.K_UP:
                personaje_vel_y=0
#logica
        personaje.x+=personaje_vel_x
        personaje.y+=personaje_vel_y

        if personaje.x> ANCHO - personaje.width:
            personaje.x=ANCHO - personaje.width
        if personaje.x<0:
            personaje.x=0
        if personaje.y>ALTO - personaje.height:
            personaje.y=ALTO-personaje.height
        if personaje.y<0:
            personaje.y=0

        for muro in muros:
            if personaje.colliderect(muro):
                if direccion == "derecha":
                    personaje.right = muro.left
                if direccion == "izquierda":
                    personaje.left = muro.right
                if direccion == "abajo":
                     personaje.bottom=muro.top
                if direccion=="arriba":
                    personaje.top=muro.bottom
        #dibujos
        ventana.fill(NEGRO)

        for muro in muros:
            dibujar_muro(ventana, muro)

        dibujar_personaje(ventana,personaje)

        #Actualizar
        pygame.display.update()

pygame.quit()


























            
