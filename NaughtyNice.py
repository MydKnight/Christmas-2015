__author__ = 'madsens'

import pygame
import Lights
#import TextFade
Lights.setup()

pygame.init()
clock = pygame.time.Clock()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('serif', 160, True)
fps_font = pygame.font.SysFont('serif', 20, True)
bg = pygame.image.load("/home/pi/Christmas-2015/Assets/brown-parchment.jpg")

while 1:
    screen.blit(bg,(0,0))
# This runs the Naughty/Nice Gag
# Display Parchment

# Wait for Input

# On Input, Disable Reader

# Get the Name from the Scanned ID. For now just pass ID

# Fadein Name of scanned ID

# Fade In Happy/Sad Claus

# Activate Naughty or Nice Pin

# Wait

# Fade Out Both

# Turn off GPIO Pin

# Reactivate Reader