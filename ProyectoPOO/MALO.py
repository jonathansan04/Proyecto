import pygame
from pygame.sprite import Sprite
from pygame import *
from BALA import *
class malo(pygame.sprite.Sprite):
    def __init__(self):
        self.ImagenMalo = pygame.image.load('Imagenes/spaceship.png')
        self.rect = self.ImagenMalo.get_rect()
        self.rect.centerx = 20
        self.rect.centery = 20
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
        bala = Bala(x,y,'Imagenes/favorite.png',False)
        self.listaDisparo.append(bala)
    def dibujar(self, superficie):
        superficie.blit(self.ImagenMalo, self.rect)
