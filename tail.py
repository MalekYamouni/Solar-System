import pygame
import math

class TailParticle:
    def __init__(self, display, radius, angle, SCREENSIZE):
        self.radius = radius
        self.angle = angle
        self.display = display
        self.R = 255
        self.G = 255
        self.B = 255
        self.center = SCREENSIZE * 0.5
        self.calcPos()

    def reduceBrightness(self):
        if self.R > 0:
            self.R -= 0.5
            self.G -= 0.5
            self.B -= 0.5

    def calcPos(self):
        self.x = self.radius*math.cos(self.angle)+self.center
        self.y = self.radius*math.sin(self.angle)+self.center

    def draw(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.x,self.y),radius=1)

    def update(self):
        self.draw()
        self.reduceBrightness()


class Tail:
    def __init__(self, angle2):
        self.particles = []
        self.angle2 = angle2

    def update(self):
        for particle in self.particles:
            particle.update()
            if particle.R < 1:
                del self.particles[0]

    def newParticle(self, display, radius, angle, SCREENSIZE):
        particle = TailParticle(display, radius, self.angle2, SCREENSIZE)
        self.particles.append(particle)
        self.updateAngle() 

    def updateAngle(self):
        self.angle2 += 0.003
        if self.angle2 >= math.pi*2:
            self.angle2 -= math.pi*2
            
