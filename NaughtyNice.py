__author__ = 'madsens'

import pygame
import os
import Lights
#import TextFade
#Lights.setup()

pygame.display.init()

# This runs the Naughty/Nice Gag
# Display Parchment
background = pygame.image.load ("/home/pi/Christmas-2015/Assets/brown-parchment.jpg")
screen = pygame.display.set_mode (background.get_size())
screen.blit (background, (0,0) )
pygame.display.flip()

while True:
    # Wait for Input
    rfid = raw_input()

    # If STOP, Quit the program
    if rfid == "STOP":
        pygame.quit()
    else:
        # On Input, Disable Reader
        os.system("/home/pi/Christmas-2015/Scripts/disableRFID.sh")

# Get the Name from the Scanned ID. For now just pass ID

# Fadein Name of scanned ID

# Fade In Happy/Sad Claus

# Activate Naughty or Nice Pin

# Wait

# Fade Out Both

# Turn off GPIO Pin

        # Reactivate Reader
        os.system("/home/pi/Christmas-2015/Scripts/enableRFID.sh")