import pygame
import math

class TailParticle:
    def __init__(self,display, taillist, radius, angle, x, y, SCREENSIZE, counter) -> None:
        self.taillist = taillist
        self.radius = radius
        self.angle = angle
        self.display = display
        self.R = 255
        self.G = 255
        self.B = 255
        self.x = x
        self.y = y
        self.SCREENSIZE =SCREENSIZE
        self.counter = counter

    def reduceBrightness(self):
        if self.R > 0:
            self.R -= 0.4
            self.G -= 0.4
            self.B -= 0.4

    def getx(self):
        self.currentx = self.x*math.cos(self.angle)+self.SCREENSIZE/2
        return self.currentx

    def gety(self):
        self.currenty = self.y*math.sin(self.angle)+self.SCREENSIZE/2
        return self.currenty


    def draw(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.getx(),self.gety()),radius=self.radius)

    def update(self):
        self.draw()
        self.reduceBrightness()

class Tail:


    def __init__(self):
        self.particles = []
        self.angle = 0

    def update(self):
        for i in self.particles:
            i.update()
            if i.R < 1:
                del i

    def newParticle(self, display, SCREENSIZE):
        particle = TailParticle(display,[],1, self.angle, SCREENSIZE/2, SCREENSIZE/2, SCREENSIZE, 0)
        self.particles.append(particle)
        self.updateAngle()
    
    def updateAngle(self):
        self.angle += 0.001
        if self.angle >= 6.3:
            self.angle = 0

