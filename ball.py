import sys, pygame
pygame.init()

size = width, height = 512, 512
speed = [1, 0.5]
gravity = 1.02
gravityEfficiency = 0.9
verticalMovement = True

black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load('SoccerBall.png')
ballrect = ball.get_rect()

print(f'Screen Size: {width}, {height}')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        print(f'Speed: {speed}' )
        if(abs(speed[1]) < 5 ):
            verticalMovement = False

    if speed[1] > 0: # ball is falling so increase speed
        speed[1] = speed[1] + (gravity * gravityEfficiency)
    elif speed[1] < 0: # ball is increasing height so decrease speed
        speed[1] = speed[1] + gravity


    if(not verticalMovement):
       speed[1] = 0

    ballrect = ballrect.move(speed)


    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()