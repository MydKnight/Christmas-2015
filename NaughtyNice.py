__author__ = 'madsens'

import pygame
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

# Wait for Input
rfid = raw_input()
# On Input, Disable Reader
pygame.quit()
# Get the Name from the Scanned ID. For now just pass ID

# Fadein Name of scanned ID

# Fade In Happy/Sad Claus

# Activate Naughty or Nice Pin

# Wait

# Fade Out Both

# Turn off GPIO Pin

# Reactivate Reader