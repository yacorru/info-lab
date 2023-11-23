import random
from random import randrange
from graphics import *
import time


def delay(t):
    """atura el programa t milisegons"""
    time.sleep(t/1000.0)

def esborraQuadreXY(x,y,midaX,altY=1,color="white"):
    """ 
    Pintem un rectangle amb l'espai que ocuparà el text (midaX)
    a la posició x i y donades
    win, ColBack al programa principal  """
    
    rec=Rectangle(Point((x-midaX/2)*18,(y-altY/2)*18),Point((x+midaX/2)*18,(y+altY/2)*18))
    rec.setFill(color)
    rec.setOutline(color)
    rec.draw(win)

def printXY(x, y, s,mida=40,fons="no"):
    """
    Utilizar min 1,1 i com a max x 68 i max y 36
    s'ha de tenir en compte la llargada del text
    win i ColBack al programa principal   """
    
    if fons!="no":
        esborraQuadreXY(x+mida/7,y,mida,color=fons)
    s=s.ljust(mida)
    t=Text(Point(x*18,y*18),s)
    t.setTextColor(ColText)
    t.setFace("courier")
    t.draw(win)

def aleatori(n):
    """retorna un valor enter aleatori entre 0 i n-1"""
    return random.randrange(n)

def pintaTaulaColor(color):
    """
    Pinta la Taula segons valor columnes del programa principal,
    BarraEsquerra, BarraDreta i files, BarraDalt i BarraBaix
    amb el color donat.
    win al programa principal """
    
    linia=Line(Point(BarraEsquerra*18-3,BarraDalt*18),Point(BarraDreta*18+3,BarraDalt*18))
    linia.setWidth(7)
    linia.setOutline(color)
    linia.draw(win)
    linia=Line(Point(BarraEsquerra*18,BarraDalt*18),Point(BarraEsquerra*18,BarraBaix*18))
    linia.setWidth(7)
    linia.setOutline(color)
    linia.draw(win)
    linia=Line(Point(BarraEsquerra*18-3,BarraBaix*18),Point(BarraDreta*18+3,BarraBaix*18))
    linia.setWidth(7)
    linia.setOutline(color)
    linia.draw(win)
    linia=Line(Point(BarraDreta*18,BarraBaix*18),Point(BarraDreta*18,BarraDalt*18))
    linia.setWidth(7)
    linia.setOutline(color)
    linia.draw(win)

def pintaTaula():
    pintaTaulaColor(ColQuadre)
    
def esborraTaula():
    #suposem white com a color de fons
    pintaTaulaColor(ColBack)
    
def esborraMobil():
    # c1,c2 al programa principal
    c1.undraw()
    c2.undraw()

def mostraMobil():
    # c1,c2 al programa principal
    c1.draw(win)
    c2.draw(win)

def mouMobil(x,y):
    # c1,c2 al programa principal
    #El mòbil són 2 cercles amb mateix centre
    c1.move(x,y)
    c2.move(x,y)

def novaPosicio(PX, PY, DX, DY):
    ''' Revisió d'on és el mòbil, cap on va i quina serà
    la propera posició i direcció.
    Rebem posició o direcció actual i retornem els nous valors'''

    # calculem nova adreça de la Mobil
    if (PX<=BarraEsquerra+1): #posició just abans de la barra esquerra
        DX=+1  #rebot esquerra
    if (PX>=BarraDreta-1): #posició just abans de la barra dreta
        DX=-1    #rebot dreta
    if (PY<=BarraDalt+1): #posició just abans de la barra de dalt
        DY=+1    #rebot dalt
    if (PY>=BarraBaix-1): #posició just abans de la barra de baix
        DY=-1   #rebot baix
        
    #Mostrem el valor de Velo a pantalla
    printXY(66,2,"Velo:"+str(Velo),mida=15,fons="white smoke")

    PX=PX+DX
    PY=PY+DY
    #movem la Mobil en direcció DirX i DirY 18 pixels en cada direcció
    mouMobil(DX*18,DY*18)
    return PX, PY, DX, DY

def mirarTeclat(Bnt, EsVeuT):
    # Mirem si hi ha tecla polsada
    Tecla = win.checkKey()
    if Tecla != "":
        # f o F: fi programa
        if Tecla == 'f' or Tecla == "F":
            Bnt = False
        # tecles + o menys mostren un + o menys per pantalla
        # tenen nom especial
        elif Tecla == "plus":
            printXY(66, 13, "Tecla +", fons=ColBack)
        elif Tecla == "minus":
            printXY(66, 13, "Tecla -", fons=ColBack)
        # tecla t: mostra o esborra linies camp
        elif Tecla == "t":
            EsVeuT = not EsVeuT
            if EsVeuT:
                pintaTaula()
            else:
                esborraTaula()
        # Número '3': enviar mòbil a la cantonada de baix a la dreta
        elif Tecla == "3":
            esborraMobil()
            PosX, PosY, DirX, DirY = BarraDreta - 2, BarraBaix - 2, -1, -1
            c1.move(PosX * 18, PosY * 18)
            c2.move(PosX * 18, PosY * 18)
            mostraMobil()
        # Número '4': enviar mòbil a la cantonada de baix a l'esquerra
        elif Tecla == "4":
            esborraMobil()
            PosX, PosY, DirX, DirY = BarraEsquerra + 2, BarraBaix - 2, 1, -1
            c1.move(PosX * 18, PosY * 18)
            c2.move(PosX * 18, PosY * 18)
            mostraMobil()
        # Si és una altra tecla, mirem valor per pantalla
        else:
            printXY(66, 17, Tecla, fons="yellow", mida=25)
    return Bnt, EsVeuT, Tecla

def menu():
    '''Per escriure el menú, comencem per
    la línia y 5 i anem incrementant a cada missatge
    la posició x serà 66 per tots els missatges '''
    
    y=5
    printXY(66,y,'f,F-fi de joc',fons="blanched almond")
    y=y+1
    printXY(66,y,'t-visibilitat taula',fons="blanched almond")

def inicialitzaPosDir():
    ''' Cerquem aleatòriament una posició del mòbil
    i la seva direcció aleatòria.'''
    
    #definim posició x,y pilota aleatòria
    PosX=randrange(BarraDreta-BarraEsquerra-1)+BarraEsquerra+1
    PosY=randrange(BarraBaix-BarraDalt-1)+BarraDalt+1
    
    # definim direcció
    DirX=randrange(2)*2-1
    DirY=randrange(2)*2-1
    return PosX,PosY,DirX,DirY                

win = GraphWin("El mòbil", 1200, 650)

# definim límits taula
BarraDalt=3
BarraBaix=20
BarraDreta=50
BarraEsquerra=10
#
Botant=True
Voltes=0
Velo=10
ColBack="white"
win.setBackground(ColBack)
ColQuadre="red"
ColText="green"

EsVeuTaula=True

PosX,PosY,DirX,DirY=inicialitzaPosDir() 
#creaMobil a PosX,PosY
def mirarTeclat(Bnt, EsVeuT):
    # Mirem si hi ha tecla polsada
    Tecla = win.checkKey()
    if Tecla != "":
        # f o F: fi programa
        if Tecla == 'f' or Tecla == "F":
            Bnt = False
        # tecles + o menys mostren un + o menys per pantalla
        # tenen nom especial
        elif Tecla == "plus":
            printXY(66, 13, "Tecla +", fons=ColBack)
        elif Tecla == "minus":
            printXY(66, 13, "Tecla -", fons=ColBack)
        # tecla t: mostra o esborra linies camp
        elif Tecla == "t":
            EsVeuT = not EsVeuT
            if EsVeuT:
                pintaTaula()
            else:
                esborraTaula()
        # Número '3': enviar mòbil a la cantonada de baix a la dreta
        elif Tecla == "3":
            esborraMobil()
            PosX, PosY, DirX, DirY = BarraDreta - 2, BarraBaix - 2, -1, -1
            c1.move(PosX * 50, PosY * 20)
            c2.move(PosX * 50, PosY * 20)
            mostraMobil()
        # Número '4': enviar mòbil a la cantonada de baix a l'esquerra
        elif Tecla == "4":
            esborraMobil()
            PosX, PosY, DirX, DirY = BarraEsquerra + 2, BarraBaix - 2, 1, -1
            c1.move(PosX * 18, PosY * 18)
            c2.move(PosX * 18, PosY * 18)
            mostraMobil()
        # Si és una altra tecla, mirem valor per pantalla
        else:
            printXY(66, 17, Tecla, fons="yellow", mida=25)
    return Bnt, EsVeuT, Tecla



c1 = Circle(Point(PosX*18,PosY*18), 16)
c1.setFill("blue")
c2 = Circle(Point(PosX*18,PosY*18), 10)
c2.setFill("yellow")
c1.draw(win)
c2.draw(win)

# Mostrem el menú
menu()

# Pintem taula
pintaTaula()

while (Botant):
    if (Voltes==0):
        PosX, PosY, DirX, DirY=novaPosicio(PosX, PosY, DirX, DirY)
    delay(25)
    Voltes=(Voltes+1) % Velo;
    Botant, EsVeuTaula, Tecla = mirarTeclat(Botant, EsVeuTaula)
    
if Tecla!="F":    
    esborraQuadreXY(40,15,30,10,"gray")
    printXY(40,14,"Fi del joc")
    printXY(40,16,"Fes clic amb ratolí per acabar")
    win.getMouse() # pausa fins que es faci clic a la finestra gràfica

win.close()



