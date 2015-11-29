__author__ = 'madsens'

import pygame
import os
import Lights
#import TextFade
#Lights.setup()

pygame.display.init()
pygame.font.init()

# This runs the Naughty/Nice Gag


while True:
    # Display Parchment
    background = pygame.image.load ("/home/pi/Christmas-2015/Assets/brown-parchment.jpg")
    screen = pygame.display.set_mode (background.get_size())
    background = pygame.image.load ("/home/pi/Christmas-2015/Assets/brown-parchment.jpg").convert()
    font = pygame.font.SysFont('sans-serif', 160, True)
    screen.blit (background, (0,0) )
    pygame.display.flip()

    # Wait for Input
    rfid = raw_input()

    # If STOP, Quit the program
    if rfid == "STOP":
        pygame.quit()
        break
    else:
        # On Input, Disable Reader
        os.system("/home/pi/Christmas-2015/Scripts/disableRFID.sh")

        # Get the Name from the Scanned ID. For now just pass ID
        name = rfid

        # Fadein Name of scanned ID
        # Display some text
        font = pygame.font.Font(None, 36)
        text = font.render(name, 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = screen.get_rect().centerx
        #screen.blit(text, textpos)
        #pygame.display.flip()

        for x in range (225):
            text.set_alpha(x)
            print x
            screen.blit(text, textpos)
            pygame.display.flip()
            pygame.time.delay(20)

# Fade In Happy/Sad Claus

# Activate Naughty or Nice Pin

# Wait

# Fade Out Both

# Turn off GPIO Pin

        # Reactivate Reader
        os.system("/home/pi/Christmas-2015/Scripts/enableRFID.sh")