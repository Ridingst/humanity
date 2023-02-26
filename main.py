import sys, pygame
from ball.floor import Floor
pygame.init()

size = width, height = 512, 512
black = 0,0,0
speed = (1,1)

screen = pygame.display.set_mode(size)
print(f'Screen Size: {width}, {height}')

pygame.display.set_caption("Humanity")
screen.fill(black)

floor = Floor(20)
floor.draw(screen)
pygame.display.flip()


game = pygame.Surface((width, height - floor.height))
ball = pygame.image.load('SoccerBall.png')
ballrect = ball.get_rect()
game.blit(ball, ballrect)
screen.blit(game, game.get_rect())





## Screen setup
#  Game - Ball
#  Game - Ball
#  Game - Ball
#  Game - Ball
#  Floor



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    game.blit(ball, ballrect)
    screen.blit(game, game.get_rect())
    ballrect = ballrect.move(speed)

    
    
    pygame.display.flip()
    #pygame.display.update(ballrect)