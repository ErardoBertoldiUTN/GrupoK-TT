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
VERDE=(0,255,0)
MARRON=(150,70,10)
ROJO=(255,0,0)
AMARILLO=(255,255,0)
BLANCO=(255,255,255)
CELESTE=(0,255,255)


#Mapas
#1270/40=32 baldosas a lo ancho
#640/40=16 baldosas a lo largo
mapa=[  #las X me representan las baldosas
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
mapaUnJugador=[
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
############################## FUNCIONES DEL PROGRAMA ######################################################
def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, MARRON, rectangulo)

def dibujar_personaje(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)
def dibujar_personaje2(superficie, rectangulo):
    pygame.draw.rect(superficie, AMARILLO, rectangulo)
def dibujar_vacunas_pildoras(superficie, listapildoras, vacunas):
    for recs in listapildoras:
        pygame.draw.rect(ventana,VERDE, recs)
    for vac in vacunas:
        pygame.draw.rect(ventana,CELESTE,vac)
    
def dibujar_enemigo(superficie, rectangulo):
    pygame.draw.rect(superficie, ROJO, rectangulo)

def construir_mapa(mapa, listapildoras):
    muros=[]
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == "X":
                muros.append(pygame.Rect(x,y,40,40))
            else:
                listapildoras.append(pygame.Rect(x+10,y+10,15,15))
            x+=40
        x=0
        y+=40
    return muros

def dibujar_mapa(superficie, muros):
    for muro in muros:
        dibujar_muro(superficie,muro)
def movimientoEnemigo(enemigo, muertoEnemigo):  #con los siguientes if logro hacer que los enemigos me persigan
    if(muertoEnemigo==False):
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
        if perdioAzul==False and perdioAmarillo==False:
            if(distancia1<distancia2):
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

            if(distancia1>distancia2):
                if enemigo.x>personaje2.x:         
                    enemigo.x-=1
                    moverseizq=True
                if enemigo.x<personaje2.x:
                    enemigo.x+=1
                    moverseDer=True
                if enemigo.y>personaje2.y:
                    enemigo.y-=1
                    moverseArriba=True
                if enemigo.y<personaje2.y:
                    enemigo.y+=1
                    moverseAbajo=True
        if perdioAmarillo==True:
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
        if perdioAzul==True:
            if enemigo.x>personaje2.x:         
                enemigo.x-=1
                moverseizq=True
            if enemigo.x<personaje2.x:
                enemigo.x+=1
                moverseDer=True
            if enemigo.y>personaje2.y:
                enemigo.y-=1
                moverseArriba=True
            if enemigo.y<personaje2.y:
                enemigo.y+=1
                moverseAbajo=True

def colisionEnemigo(enemigo, i):
    if enemigo.colliderect(muro):
        if moverseDer==True and moverseArriba==True:
            moverseDer==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseArriba==False
                enemigo.y=anty[i] 
                moverseDer==True
                enemigo.x+=1
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo.x=antx[i] 
                    
        elif moverseDer==True and moverseAbajo==True:
            moverseDer==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo.y=anty[i] 
                moverseDer==True
                enemigo.x+=1
                if enemigo.colliderect(muro):
                    moverseDer==False
                    enemigo.x=antx[i]
                    
        elif moverseizq==True and moverseAbajo==True:
            moverseizq==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseAbajo==False
                enemigo.y=anty[i] 
                moverseizq==True
                enemigo.x-=1
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo.x=antx[i] 
        elif moverseizq==True and moverseArriba==True:
            moverseizq==False
            enemigo.x=antx[i] 
            if enemigo.colliderect(muro):
                moverseArriba==False
                enemigo.y=anty[i] 
                moverseizq==True
                enemigo.x-=1
                if enemigo.colliderect(muro):
                    moverseizq==False
                    enemigo.x=antx[i]
def ComeEnemigos(vac, jugador,i):
    cantComidos=0
    if(tiempo<tiempoparacomer[i]):

        for i in range (e):
            if jugador.colliderect(enemigo[i]):
                print("JUGADOR COMIO ENEMIGO")
                enemigo[i]=pygame.Rect(0,0,0,0)
                muertoEnemigo[i]=True
                cantComidos=cantComidos+1
    return cantComidos
                            
###############################################################CUERPO PRINCIPAL DEL PROGRAMA######################################################

ventana=pygame.display.set_mode((ANCHO,ALTO))
reloj=pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT,1000)

#datos
listapildoras = []
vacunas=[]
enemigosEliminados=[0,0]
direccion=""
direccion2=""
personaje= pygame.Rect(1170,530,30,30)  #los primeros dos números son la posición en la que aparecerá una vez ejecutado el programa, las siguientes dos numeros refieren al tamaño
personaje2=pygame.Rect(1170,80,30,30)
perdioAzul=False
perdioAmarillo=False
pildorasConsumidas=[0,0]
x=0

velocidad=7                         #constante para controlar la velocidad de movimiento del personaje
#con la siguiente lista boolean se controla cuando se mantiene apretada una tecla de movimiento.
#Después vi que existía una función getpressed que me lo hubiese hecho mas facil, pero igual con esta forma funciona
WASD = [False, False, False, False]
WASD2 = [False, False, False, False]

enemigo=[]
e=5 #cantidad de enemigos
w=0
z=0 
for i in range (e):
    w=80
    z=z+100
    enemigo.append(pygame.Rect(w,z,30,30))
muertoEnemigo=[False, False, False, False,False]
antx=[0,0,0,0,0]  # listas que guardan las posiciones de los enemigos
anty=[0,0,0,0,0]
moverseizq=True
moverseDer=True
moverseArriba=True
moverseAbajo=True
#bucle ppal
jugando = True
tiempo=0
tiempoparacomer=[0,0]
cantJugadores=menu.pantallaMenu() #Llamando al Menu inicial
jugador2=False
print("Cantidad de jugadores: ", cantJugadores)
if cantJugadores==1:
    perdioAmarillo=True
    vacunas.append(pygame.Rect(100,300,10,20))
    vacunas.append(pygame.Rect(100,300,10,20))
    muros=construir_mapa(mapaUnJugador, listapildoras)
elif cantJugadores==2:
    jugador2=True
    vacunas.append(pygame.Rect(200,40,10,20))
    vacunas.append(pygame.Rect(200,570,10,20))
    muros=construir_mapa(mapa, listapildoras)
while jugando:

    for event in pygame.event.get():       #event.get() detecta cuando se presiona una tecla
        if event.type==pygame.USEREVENT:
            tiempo+=1
            print(tiempo) 
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

    for i in range (e):
        movimientoEnemigo(enemigo[i], muertoEnemigo[i])
    
#el siguiente ciclo for me sirve para controlar las colisiones con los muros, hubo que hacer varias pruebas
#porque me hacía errores al presionar dos teclas, por ej al llegar a una esquina presionando dos teclas
#el personaje atravesaba el muro y aparecía en cualquier lado, ya está corregido
    for muro in muros:
        if personaje.colliderect(muro):   ##JUGADOR 1
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
            
        if personaje2.colliderect(muro):     ### JUGADOR 2
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

    oldx = personaje.x 
    oldy = personaje.y
    oldx2 = personaje2.x 
    oldy2 = personaje2.y    

    for recs in listapildoras:
        if personaje.colliderect(recs):
            if recs.width>0:
                pildorasConsumidas[0]=pildorasConsumidas[0]+1
                #print("Pildoras Consumidas jugador AZUL: ", pildorasConsumidas[0])
            recs.width=0
            recs.height=0
        if personaje2.colliderect(recs):
            if recs.width>0:
                pildorasConsumidas[1]=pildorasConsumidas[1]+1
                #print("Pildoras Consumidas jugador AMARILLO: ", pildorasConsumidas[1])
            recs.width=0
            recs.height=0   
    for i in range (e):
        if personaje.colliderect(vacunas[0]) or personaje.colliderect(vacunas[1]) or tiempoparacomer[0]>tiempo:
            for vac in vacunas:
                if personaje.colliderect(vac):
                    if vac.width>0:
                        #print("Pildoras Consumidas jugador AZUL: ", pildorasConsumidas[0])
                        vac.width=0
                        vac.height=0
                        tiempoparacomer[0]=tiempo+5
                        print("tiempoparacomer",tiempoparacomer[0])
            enemigosEliminados[0]=enemigosEliminados[0]+ComeEnemigos(vac, personaje,0)
        elif personaje.colliderect(enemigo[i]):
            print("Perdiste JUGADOR AZUL")
            print("Pildoras Consumidas: ", pildorasConsumidas[0])
            personaje=pygame.Rect(0,0,0,0)
            perdioAzul=True
        if personaje2.colliderect(vacunas[0]) or personaje2.colliderect(vacunas[1]) or tiempoparacomer[1]>tiempo:
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
              
    if perdioAmarillo==True and perdioAzul==True:
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
            if jugador2==True:
                ventana.blit(miTexto3,(300,300))
            pygame.display.update()

    if pildorasConsumidas[0]+pildorasConsumidas[1]==len(listapildoras):
        ventana.fill(BLANCO)
        miFuente=pygame.font.Font(None,30)
        if pildorasConsumidas[0]>pildorasConsumidas[1] and perdioAzul==False:
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
            if jugador2==True:
                ventana.blit(miTexto3,(300,300))
            pygame.display.update()

    #dibujos MAPA, JUGADORES, ENEMIGOS, PILDORAS, VACUNAS
    dibujar_mapa(ventana, muros)
    if perdioAzul==False:
        dibujar_personaje(ventana,personaje)
    if perdioAmarillo==False and jugador2==True:
        dibujar_personaje2(ventana,personaje2)
    dibujar_vacunas_pildoras(ventana,listapildoras,vacunas)

    for i in range (e):
        dibujar_enemigo(ventana,enemigo[i])
    #Actualizar Pantalla
    pygame.display.update()

pygame.quit()

