__author__ = 'madsens'

import pygame
import Lights
#import TextFade
#Lights.setup()

pygame.init()
clock = pygame.time.Clock()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont('serif', 160, True)
fps_font = pygame.font.SysFont('serif', 20, True)

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('/home/pi/Christmas-2015/Assets/brown-parchment.jpg', [0,0])

while 1:
    screen.fill([0, 0, 0])
    screen.blit(BackGround.image, BackGround.rect)
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