import pygame
import math
import random
import sprite

pygame.init()

# Screensize
sz = 1000

display = pygame.display.set_mode((sz, sz))
clock = pygame.time.Clock()
# Titel des Fensters
pygame.display.set_caption("Sonnensystem")

FPS = 120
# Beschleunigung
ACCELERATION = 0.1

#################################################################################################################

class planeten():
    def __init__(self, x, y, velocity, radius, color, angle,angle2, radius2):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.radius = radius
        self.color = color
        self.angle = angle
        self.angle2 = angle2
        self.radius2 = radius2
    
    def drawstatic(self):
        pygame.draw.circle(display, color=self.color, center=(self.x,self.y),radius=self.radius)

    def drawmove(self):
        pygame.draw.circle(display,color=self.color, center=(self.x*math.cos(self.angle)+sz/2,self.y*math.sin(self.angle)+sz/2), radius=self.radius)
        self.angle += 0.001+self.velocity

    def getx(self):
        self.currentx = self.x*math.cos(self.angle)+sz/2
        self.angle += 0.001
        return self.currentx
    def gety(self):
        self.currenty = self.y*math.sin(self.angle)+sz/2
        self.angle += 0.001
        return self.currenty
        
#################################################################################################################

class stars:
    def __init__(self, x, y, radius, angle,starttime,v):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.time = starttime
        self.R = 0
        self.G = 0
        self.B = 0
        self.R1 = 255
        self.G1 = 255
        self.B1 = 255
        self.v = v
        self.devider = 1*self.v*255*2

    def drawline(self):
        pygame.draw.circle(display, color=(self.R1,self.G1,self.B1), center=(self.x,self.y),radius=self.radius)
        

    def drawstar(self):
        pygame.draw.circle(display, color=(self.R,self.G,self.B), center=(self.x,self.y),radius=self.radius)

    def timer(self):
        if self.time>=0:
            self.time -= self.v

        else:
            self.time = 1
            self.x = random.randint(1,1000)
            self.y = random.randint(1,1000)

    def bright(self):
        if self.time > 0.5 and self.R< 250:
            self.R += self.devider
            self.G += self.devider
            self.B += self.devider
        elif self.R > 5:
            self.R -= self.devider
            self.G -= self.devider
            self.B -= self.devider

    def bright2(self):
        if self.R1> 0:
            self.R1 -= 0.4
            self.G1 -= 0.4
            self.B1 -= 0.4

#################################################################################################################

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self,image) -> None:
        super().__init__()
        self.sheet = image
        

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        # bild, Koordinaten, area vom Sheet Koordinaten
        image.blit(self.sheet, (0,0), (0,frame*height, width, height))
        #größe ändern
        image = pygame.transform.scale(image,(width/scale, height/scale))
        #transparenz
        image.set_colorkey(colour) 
        return image
        
#################################################################################################################

def main():
    # Werte der Sonne
    SR = 200
    SG = 100
    SB = 0
    Ssize = 70
    Sunparts = []
    # 10 RGB Schichten um die Sonne besser darzustellen / wird noch geändert
    for i in range(10):
        Sonne = planeten(sz/2,sz/2, 0, Ssize, (SR, SG, SB),0,0,0)
        Sunparts.append(Sonne)
        SR += 5
        SG += 5
        SB += 10
        Ssize -= 7

    # Image wird geladen und in eine Variable gepackt
    sprite_sheet_image = pygame.image.load('earth.png').convert_alpha()
    sprite_sheet = Spritesheet(sprite_sheet_image)

    # Hintergrund
    BLACK = (0,0,0)

    #create animation list
    animation_list = []
    animation_steps = 48
    last_update = pygame.time.get_ticks()
    animation_cooldown = 50
    frame = 0

    for x in range(animation_steps):
       animation_list.append(sprite_sheet.get_image(x, 96, 96, 2, BLACK))

    # Erde Objekt
    Erde = planeten(sz/2-50, sz/2-50, 0.001, 15, "green", 23.5, 23.5, 1)

    # Sterneliste
    starsi = []
    # Sternedelay Zähler
    waitcounter = 0
    # Schweifliste
    starchain = []
    # Hintergrund des Mainfensters
    BG = (0,0,0)
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update background
        display.fill(BG)

        
        #update animation
        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0


       
        # Anzahl der Sterne die Random erzeugt werden
        if len(starsi)<200:
            if waitcounter>20:
                star = stars(random.randint(1,1000),random.randint(1,1000), random.randint(1,3),random.randint(1,360),random.randint(0,1),0.001)
                starsi.append(star)
                waitcounter = 0
            else:
                waitcounter += 1

        # Sterne werden gezeichnet haben einen timer, wenn timer 0 erreicht wird das Objekt gelöscht
        for star in starsi:
            star.drawstar()
            star.timer()
            star.bright()

        
        # Schweif hat die Werte des Erde2 Objekt
        Erde2 = stars(Erde.getx(), Erde.gety(), 1, 30, 5,5)
        starchain.append(Erde2)

        # Schweif wird gezeichnet, Helligkeit sinkt auf 0 und Objekt wird gelöscht
        for i in starchain:
            
            i.drawline()
            i.bright2()
            if i.R1 < 1:
                del starchain[0]

         # show frame image
        display.blit(animation_list[frame],(Erde.getx()-24,Erde.gety()-24))

        # Sonnenschichten werden gezeichnet
        for i in Sunparts:
            i.drawstatic()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()