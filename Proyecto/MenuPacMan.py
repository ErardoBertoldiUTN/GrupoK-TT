import os  #https://www.youtube.com/watch?v=ceR-MnS3QdE
import pygame
import math
from pygame import Rect
from pygame.locals import*

pygame.init()

def dibujar_botones(ventana,UnJugador, DosJugadores, Salir):
    AMARILLO=(255,255,0)
    pygame.draw.rect(ventana, AMARILLO, UnJugador)
    pygame.draw.rect(ventana, AMARILLO, DosJugadores)
    pygame.draw.rect(ventana, AMARILLO, Salir)

def pantallaMenu():
    BLANCO=(255,255,255)
    pygame.init()
    reloj=pygame.time.Clock()
    ANCHO=1270
    ALTO=640
    cantJugadores=0
    salir=False
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    miFuente=pygame.font.Font(None,30)
    FuenteTitulo=pygame.font.Font(None,100)
    FuenteDescripcion=pygame.font.Font(None,20)
    Titulo=FuenteTitulo.render("PACMAN COVID",0,(200,60,80))

    Descripcion=FuenteDescripcion.render("Bienvenidos a PacMan Covid. Se puede jugar de a uno o dos jugadores. El jugador 1 será de color azul y jugará con las teclas A,S,D,W.",0,(200,60,80))                          
    Descripcion2=FuenteDescripcion.render("El jugador 2 es de color amarillo y juega con las flechas del teclado. Cada jugador tiene una vida. Si logran recolectar todas las pildoras",0,(200,60,80))
    Descripcion3=FuenteDescripcion.render("(items colectables verdes) quien sobreviva ganara el juego. Asimismo en el laberinto hay vacunas(items colectables celestes) y en el caso",0,(200,60,80))
    Descripcion4=FuenteDescripcion.render("de que algún PacMan agarre una vacuna, gozará de inmunidad de 5 segundos en los que podrá eliminar a los COVID al chocar ellos",0,(200,60,80))
    Descripcion5=FuenteDescripcion.render("Si están jugando de a dos jugadores aunque eliminen a todos los covid deberán recolectar todos los item. Al finalizar se verán las estadísticas de cada Jugador", 0, (200,60,80))
    Descripcion6=miFuente.render("A CONTINUACION ELIJA LA CANTIDAD DE JUGADORES HACIENDO CLICK SOBRE LOS CUADROS",0,(200,60,80))
    miTexto=miFuente.render("UN JUGADOR",0,(200,60,80))
    miTexto1=miFuente.render("DOS JUGADORES",0,(200,60,80))
    textoSalir=miFuente.render("SALIR",0,(200,60,80))
    cursor=pygame.Rect(0,0,30,30)
    UnJugador=pygame.Rect(570,450,200,30)
    DosJugadores=pygame.Rect(570,500,200,30)
    Salir=pygame.Rect(570,545,200,30)
    while salir!=True:
        reloj.tick(60)
        ventana.fill(BLANCO)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                salir=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(UnJugador):
                    cantJugadores=1
                    #print("cantidad de jugadores",cantJugadores)
                    salir=True
                    break 
                if cursor.colliderect(DosJugadores):
                    cantJugadores=2
                    #print("cantidad de jugadores",cantJugadores)
                    salir=True
                    break
                if cursor.colliderect(Salir):
                    salir=True
        pos=pygame.mouse.get_pos()
        cursor.x=pos[0]
        cursor.y=pos[1]
        dibujar_botones(ventana,UnJugador,DosJugadores, Salir)
        ventana.blit(Descripcion,(200,150))
        ventana.blit(Descripcion2,(200,200))
        ventana.blit(Descripcion3,(200,250))
        ventana.blit(Descripcion4,(200,300))
        ventana.blit(Descripcion5,(200,350))
        ventana.blit(Descripcion6,(200,400))
        ventana.blit(miTexto,(590,460))
        ventana.blit(miTexto1,(590,510))
        ventana.blit(textoSalir,(590,550))
        ventana.blit(Titulo,(380,40)) 

        pygame.display.update()
    return cantJugadores
pygame.quit()



