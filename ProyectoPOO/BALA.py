import pygame
from pygame.sprite import Sprite
from pygame import *


class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy,ruta, pers ):
        pygame.sprite.Sprite.__init__(self)

        self.imageBala = pygame.image.load(ruta)
        self.rect = self.imageBala.get_rect()
        self.velocidadDisparo = 10
        self.rect.top = posy
        self.rect.left = posx 
        self.disparoPersonaje = pers
        
    def trayectoria(self):
        if self.disparoPersonaje == True:         
            self.rect.top = self.rect.top - self.velocidadDisparo
        else:
            self.rect.top = self.rect.top + self.velocidadDisparo
    def dibujar(self, superficie):
        superficie.blit(self.imageBala, self.rect)
