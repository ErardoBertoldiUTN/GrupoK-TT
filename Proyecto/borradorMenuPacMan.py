import os  #https://www.youtube.com/watch?v=ceR-MnS3QdE
import pygame
import math
from pygame import Rect
from pygame.locals import*
#inicializar
os.environ['SDL_VIDEO_CENTERED'] = '1'  #para que me aparezca centrada en el monitor la ventana pygame
pygame.init()
ANCHO=1270
ALTO=640

def dibujar_botones(ventana,UnJugador, DosJugadores):
    pygame.draw.rect(ventana, AMARILLO, UnJugador)
    pygame.draw.rect(ventana, AMARILLO, DosJugadores)
#colores
NEGRO=(0,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)
MARRON=(150,70,10)
ROJO=(255,0,0)
AMARILLO=(255,255,0)
BLANCO=(255,255,255)
ventana=pygame.display.set_mode((ANCHO,ALTO))
reloj=pygame.time.Clock()
cantJugadores=0
salir=False
cursor=pygame.Rect(0,0,30,30)
UnJugador=pygame.Rect(570,450,200,30)
DosJugadores=pygame.Rect(570,500,200,30)
while salir!=True:
    reloj.tick(60)
    ventana.fill(BLANCO)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            salir=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if cursor.colliderect(UnJugador):
                cantJugadores=1
                print("cantidad de jugadores",cantJugadores)
                salir=True
                break 
            if cursor.colliderect(DosJugadores):
                cantJugadores=2
                print("cantidad de jugadores",cantJugadores)
                salir=True
                break
    pos=pygame.mouse.get_pos()
    cursor.x=pos[0]
    cursor.y=pos[1]
    dibujar_botones(ventana,UnJugador,DosJugadores)     
    pygame.display.update()
    
pygame.quit()



