import random
import sys
import pygame
from pygame.locals import *

# Global variable for game
FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = 0.8 * SCREENHEIGHT
BACKGROUND = 'gallery/sprites/background.png'
PLAYER = 'gallery/sprites/bird.jpg'
PIPE = 'gallery/spites/pipe.png'
GAMESPRITE = {}
GAMESOUND = {}

def welcomeScreen():
    # Configuration of welcome screen after strating game
    while True:
        for event in pygame.event.get():  #Event from the user
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit() 
            
            if (event.type == KEYDOWN and event.key == K_UP) or (event.type == KEYDOWN and event.key == K_SPACE):
            
                return

            else:
               SCREEN.blit(GAMESPRITE['background'],(0,0))
               SCREEN.blit(GAMESPRITE['player'],((SCREENWIDTH-GAMESPRITE['player'].get_width())/2,(SCREENHEIGHT-GAMESPRITE['player'].get_height())/2))
               SCREEN.blit(GAMESPRITE['message'],((SCREENWIDTH-GAMESPRITE['message'].get_width())/2,SCREENHEIGHT*0.1))
               SCREEN.blit(GAMESPRITE['base'],(0,SCREENHEIGHT-GAMESPRITE['base'].get_height()))
               pygame.display.update()
               FPSCLOCK.tick(FPS)

def getRandomPipe():  # Generates one set of placement points of pipe one above and one bottom
    pipeHeight = GAMESPRITE['pipe'][0].get_height()   #320
    offset = SCREENHEIGHT/3 # player height 24 offset= 102
    #y1 = int(random.randrange(0,SCREENHEIGHT-GAMESPRITE['base'].get_height()-pipeHeight))
    #y2 = y1 - offset - pipeHeight

    y2 = offset + random.randrange(0, int(SCREENHEIGHT-GAMESPRITE['base'].get_height() - 1.2*offset))
    pipeX = SCREENWIDTH + 20
    y1 = pipeHeight - y2 + offset
    pipecordi = [
        {'x' : pipeX, 'y' : -y1},  # Upper pipe cordinate
        {'x' : pipeX, 'y' : y2}  # Bottom pipe cordinate
    ]
    return pipecordi

def isCollide(playerx, playery, upperPipes, lowerPipes):
    #if playery> GROUNDY - 25  or playery<0:
     #   GAMESOUND['hit'].play()
      #  return True
    
    for pipe in upperPipes:
        pipeHeight = GAMESPRITE['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAMESPRITE['pipe'][0].get_width()):
            GAMESOUND['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAMESPRITE['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAMESPRITE['pipe'][0].get_width():
            GAMESOUND['hit'].play()
            return True

    return False



def mainGame():
     score = 0
     playery = int(SCREENWIDTH/2)
     playerx = int(SCREENWIDTH/5)
     baseX = 0

     pipeSet_1 = getRandomPipe()
     pipeSet_2 = getRandomPipe()

     upperPipes = [                                               # Set of upper pipes cordinate
         {'x' : SCREENWIDTH + 200, 'y' : pipeSet_1[0]['y']},
         {'x' : SCREENWIDTH + 200 + (SCREENWIDTH/2) , 'y' : pipeSet_2[0]['y']}
    ]

     lowerPipes = [                                               # Set of lower pipes cordinate    
         {'x' : SCREENWIDTH + 200, 'y' : pipeSet_1[1]['y']},
         {'x' : SCREENWIDTH + 200 + (SCREENWIDTH/2), 'y' : pipeSet_2[1]['y']}
    ]
    
    # Velocities

     pipeVelX = -4

     playerVelocityY = -9
     playerMaxVelocityY = 10
     playerAccelaration = 1

     playerFlappedVelocity = -8 # While Flapping
     playerFlapped = False

  

     while True:

        # If user press any button
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            if (event.type == KEYDOWN and event.key == K_SPACE) or (event.type == KEYDOWN and event.key == K_UP):
                if playery > 0:
                    playerVelocityY = playerFlappedVelocity
                    playerFlapped = True
                    GAMESOUND['wing'].play()
        
        # While user is not pressing anything

        # Crashing
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            return

        # Score
        playerMidPosition = playerx + (GAMESPRITE['player'].get_width()/2)

        for pipe in upperPipes:
            pipeMidPosition = pipe['x'] + GAMESPRITE['pipe'][0].get_width()/2
            if pipeMidPosition <= playerMidPosition < (pipeMidPosition + 4):
                score += 1
                print(f"Score:{score}")
                GAMESOUND['point'].play()
        
        if playerVelocityY < playerMaxVelocityY and not playerFlapped:
            playerVelocityY += playerAccelaration
        
        if playerFlapped:
            playerFlapped = False
        
        # New position of player
        playery = playery + min(playerVelocityY,GROUNDY-playery-GAMESPRITE['player'].get_height())
        
        # Moveing pipe
        for upperPipe , lowerPipe in zip(upperPipes , lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX
        
        # Adding new pipe
        if 0<upperPipes[0]['x']<5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])
        
        # Remove old passed pipe from list
        if upperPipes[0]['x'] < -GAMESPRITE['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
          # Bliting of pictures
        SCREEN.blit(GAMESPRITE['background'] , (0 , 0))
        for upperPipe ,lowerPipe in zip(upperPipes,lowerPipes):
            SCREEN.blit(GAMESPRITE['pipe'][0], (upperPipe['x'],upperPipe['y']))
            SCREEN.blit(GAMESPRITE['pipe'][1], (lowerPipe['x'],lowerPipe['y']))
    
        SCREEN.blit(GAMESPRITE['base'],(0,GROUNDY))
        SCREEN.blit(GAMESPRITE['player'],(playerx,playery))

        width = 0
        digits = [int(x) for x in list(str(score))]
        for digit in digits:
            width += GAMESPRITE['numbers'][digit].get_width()
        xoffset = (SCREENWIDTH-width)/2

        for digit in digits:
            SCREEN.blit(GAMESPRITE['numbers'][digit],(xoffset,SCREENHEIGHT*0.1))
            xoffset += GAMESPRITE['numbers'][digit].get_width()
    
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        


            


if __name__ == "__main__":
    # From this point our game will start
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption("Flapp with marvik")
    GAMESPRITE['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    GAMESPRITE['message'] = pygame.image.load('gallery/sprites/message.png').convert_alpha()
    GAMESPRITE['base'] = pygame.image.load('gallery/sprites/base.png').convert_alpha()
    GAMESPRITE['pipe'] = (pygame.transform.rotate(pygame.image.load('gallery/sprites/pipe.png').convert_alpha(),180),pygame.image.load('gallery/sprites/pipe.png').convert_alpha())
    GAMESPRITE['background'] = pygame.image.load(BACKGROUND).convert()
    GAMESPRITE['player'] = pygame.image.load(PLAYER).convert_alpha()

    # Game sound
    GAMESOUND['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAMESOUND['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAMESOUND['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAMESOUND['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAMESOUND['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    while True:
        welcomeScreen()
        mainGame()

