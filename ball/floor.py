import os
import pygame

class Floor(pygame.sprite.Sprite):
    '''Class to keep players location'''
    def __init__(self, height=100, image_tile=os.path.dirname(os.path.realpath(__file__))+'/tileplanks.png'):

        self.width = pygame.display.get_surface().get_size()[0]
        self.height = height

        #self.image = pygame.Surface(pygame.display.get_surface().get_size())
        self.background_tile = pygame.image.load(image_tile)
        self.rect = self.background_tile.get_rect()

        print(image_tile)


    def draw(self, surface):
        top = surface.get_size()[1] - self.height 
        width = surface.get_size()[0]

        floor_surface = pygame.Surface((width, self.height))
        
        floor = self.background_tile

        l, t, w, h = floor.get_rect()

        # Loop through the tile to draw the floor. 
        ii = 0
        while(ii*h<self.height):
            i=0
            while(i*w<width):
                floor_surface.blit(floor, (i*w, ii*h))
                i=i+1
            ii=ii+1

        surface.blit(floor_surface, (0, top, width, self.height))
