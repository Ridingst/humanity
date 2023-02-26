import os
import pygame

class Ball(pygame.sprite.Sprite):
    '''Class to keep ball'''
    def __init__(self,
                 x=20, y=20,
                 prev_x = 0, prev_y = 0,
                 gravity = 1.1,
                 gravity_efficieny = 0.7,
                 speed = [10,1],
                 prev_speed = [1,1],
                 image=os.path.dirname(os.path.realpath(__file__))+'/SoccerBall.png'):

        self.position = (x,y)
        self.previous_position = (prev_x, prev_y)
        self.gravity = gravity
        self.gravity_efficieny = gravity_efficieny
        self.vertical_momentum = True
        self.speed = speed
        self.previous_speed = prev_speed
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        
        self.surface = pygame.Surface(self.image.get_rect()[2:])
        self.surface.blit(self.image, self.rect)


    def move(self, surface):
        # set previous x,y and speed
        if(not self.vertical_momentum):
           return

        self.previous_position = self.position
        self.previous_speed = self.speed

        if(self.speed[1] > 0 and self.vertical_momentum):
            self.speed[1] = (self.speed[1] + self.gravity)
        if(self.speed[1] < 0 and self.vertical_momentum):
            self.speed[1] = (self.speed[1] + (self.gravity * (1/self.gravity_efficieny)))

        if(self.rect.right >= surface.get_width() or self.rect.left < 0):
            confirm_wall_bounce = False
            if(self.rect.right >= surface.get_width()):
                if(self.speed[0] > 0):
                    confirm_wall_bounce = True
            if(self.rect.left < 0 ):
                if(self.speed[0] < 0):
                    confirm_wall_bounce = True
            
            if(confirm_wall_bounce):
                print(f'Wall bounce ({self.rect})')
                self.speed[0] = -self.speed[0]
                if(abs(self.speed[0]) > 5): 
                    self.speed[0] = self.speed[0]*0.9
                else:
                    self.speed[0] = self.speed[0]*0.5

        if(self.rect.bottom >= surface.get_height()): # then we hit bottom
            # if it's bottom we always want a negative number (upwards) else
            # it could be a second itter in the bounce zone

            if(self.speed[1] < 0):
                print("Already moving up")
            else:
                print(f'Bounce ({self.speed})')
                self.speed[1] = -self.speed[1]
                if(abs(self.speed[1]) < 13.5):
                    self.speed[1] = self.speed[1]*0.7
                
            if(abs(self.speed[1]) < 6.1 ):
                self.speed[1] = 0
                self.vertical_momentum = False
                
        # update position
        self.rect[0] += self.speed[0]
        self.rect[1] += self.speed[1]
        #self.rect.move(self.speed)
        print(self.speed)


    def draw(self, surface):
        #print(f'Vertical Momentum: {self.vertical_momentum} ({abs(self.speed[1])})' )
        surface.blit(self.image, self.rect)

