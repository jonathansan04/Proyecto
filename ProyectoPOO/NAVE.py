import pygame
from pygame.sprite import Sprite
from pygame import *
from BALA import *
class nave(pygame.sprite.Sprite):
    def __init__(self):
        self.ImagenNave = pygame.image.load('Imagenes/rocket.png')
        self.rect = self.ImagenNave.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 450
        self.listaDisparo = []
        self.vida = 100
        self.velocidad = 20

    def movimiento(self):
        if self.vida == True:
            if self.rect.left <=0:
                self.rect.left =0
            elif self.rect.right>640:
                self.rect.right = 620 
    def disparar(self, x, y):
        bala = Bala(x,y,'Imagenes/bullet.png',True)
        self.listaDisparo.append(bala)
    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave, self.rect)
