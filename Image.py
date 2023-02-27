import pygame

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self,image) -> None:
        super().__init__()
        self.sheet = image
    # Bild Defintion    
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        # bild, Koordinaten, area vom Sheet Koordinaten
        image.blit(self.sheet, (0,0), (0,frame*height, width, height))
        #größe ändern
        image = pygame.transform.scale(image,(width/scale, height/scale))
        #transparenz
        image.set_colorkey(colour) 
        return image