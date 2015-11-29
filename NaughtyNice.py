__author__ = 'madsens'

import pygame
import os
import Lights
#import TextFade
#Lights.setup()

pygame.display.init()
pygame.font.init()

# This runs the Naughty/Nice Gag
# Display Parchment
background = pygame.image.load ("/home/pi/Christmas-2015/Assets/brown-parchment.jpg")
screen = pygame.display.set_mode (background.get_size())
font = pygame.font.SysFont('sans-serif', 160, True)
screen.blit (background, (0,0) )
pygame.display.flip()

while True:
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
        label = font.render(name,1,(255,0,0))
        newSurf = pygame.Surface(font.size(name))
        newSurf.blit(label,(0,0))
        for x in range (225):
            newSurf.set_alpha(x - 255)
            screen.blit(newSurf, (100,100))
            pygame.display.flip()
            pygame.time.delay(20)

# Fade In Happy/Sad Claus

# Activate Naughty or Nice Pin

# Wait

# Fade Out Both

# Turn off GPIO Pin

        # Reactivate Reader
        os.system("/home/pi/Christmas-2015/Scripts/enableRFID.sh")