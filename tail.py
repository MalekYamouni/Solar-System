import pygame
import math

class Tail:
    def __init__(self,display, taillist, radius, angle, starttime, v, x, y, SCREENSIZE) -> None:
        self.taillist = taillist
        self.radius = radius
        self.angle = angle
        self.starttime = starttime
        self.v = v
        self.display = display
        self.R = 255
        self.G = 255
        self.B = 255
        self.x = x
        self.y = y
        self.SCREENSIZE =SCREENSIZE

    def brightness(self):
        if self.R> 0:
            self.R -= 0.4
            self.G -= 0.4
            self.B -= 0.4

    def getx(self):
        self.currentx = self.x*math.cos(self.angle)+self.SCREENSIZE/2
        self.angle += 0.001
        return self.currentx

    def gety(self):
        self.currenty = self.y*math.sin(self.angle)+self.SCREENSIZE/2
        self.angle += 0.001
        return self.currenty

    def drawparticle(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.getx(),self.gety()),radius=self.radius)

    def drawtail(self):
        for i in self.taillist:
            i.drawparticle()
            i.brightness()
            if i.R < 1:
                del self.taillist[0]