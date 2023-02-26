import sys, pygame, pygame_menu
import ball.floor as floor
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

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def generate_map():
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass


def start_ball():
    # Do the ball !
    print('Starting Ball...')
    main_menu.disable()
    main_menu.full_reset()

    
    speed = [1, 0.5]
    gravity = 1.02
    gravityEfficiency = 0.9
    verticalMovement = True

    black = 0,0,0

    ball = pygame.image.load('SoccerBall.png')
    ballrect = ball.get_rect()

    while True:
        floor.draw(screen)
        print(floor)
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
    pass

menu = pygame_menu.Menu('Humanity', 400, 300,
                       theme=pygame_menu.themes.THEME_GREEN)

menu.add.text_input('Colony: ', default='Adam & Eve')
#menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Generate Map', generate_map)
menu.add.button('Play', start_the_game)
menu.add.button('Play Ball', start_ball)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(screen)