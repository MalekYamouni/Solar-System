import pygame
from random import randint

class stars:
    def __init__(self,display, x, y, radius, angle, time, v, counter):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.time = time
        self.R = 0
        self.G = 0
        self.B = 0
        self.v = v
        self.display = display
        self.liste = []
        self.counter = counter

    def drawstar(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.x,self.y),radius=self.radius)

    # timer wird runtergezählt und wenn er 0 erreicht reset auf 1.
    def timer(self):
        if self.time>=0:
            self.time -= self.v

        else:
            self.time = 1
            self.x = randint(1,1000)
            self.y = randint(1,1000)
    
    def calcBrightness(self):
        # f(x) = -1020x² + 255
        self.brightness = -1020 *((self.time-0.5) *(self.time-0.5)) +255 #  <= Quadtratische Funktion
        self.R = self.brightness
        self.G = self.brightness
        self.B = self.brightness

    # Sternobjekte werden in Liste Konstant wieder eingefügt nachdem sie gelöscht werden wenn deren RGB Wert auf 0 sinkt
    def addStarIfNotEnough(self):
        if len(self.liste) < 200:
            if self.counter > 20:
                star = stars(self.display, randint(1,1000), randint(1,1000), randint(1,3), randint(1,360), 1, 0.001, 0)
                self.liste.append(star)
                self.counter = 0
            else:
                self.counter += 1
                
    def update(self):
        # Sterne werden gezeichnet haben einen timer, wenn timer 0 erreicht wird das Objekt 
        for star in self.liste:
            star.drawstar()
            star.timer()
            star.calcBrightness()
