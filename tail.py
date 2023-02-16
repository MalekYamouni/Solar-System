import pygame
import math

class TailParticle:


    def __init__(self,display, taillist, radius, angle, SCREENSIZE, counter) -> None:
        self.taillist = taillist
        self.radius = radius
        self.angle = angle
        self.display = display
        self.R = 255
        self.G = 255
        self.B = 255
        self.center = SCREENSIZE * 0.5
        self.counter = counter
        self.calcPos()

    def reduceBrightness(self):
        if self.R > 0:
            self.R -= 0.4
            self.G -= 0.4
            self.B -= 0.4

    def calcPos(self):
        self.x = self.center*math.cos(self.angle)+self.center
        self.y = self.center*math.sin(self.angle)+self.center

    def draw(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.x,self.y),radius=self.radius)

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
                del self.particles[0]

    def newParticle(self, display, SCREENSIZE):
        particle = TailParticle(display,[],1, self.angle, SCREENSIZE, 0)
        self.particles.append(particle)
        self.updateAngle()  

    def updateAngle(self):
        self.angle += 0.01
        if self.angle >= 6.3:
            self.angle -= 6.3
