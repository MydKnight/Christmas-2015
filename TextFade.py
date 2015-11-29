__author__ = 'madsens'
import pygame

def FadeIn(screen, text):
    myFont = pygame.font.SysFont('sans-serif', 160, True)
    textToFadeIn = text
    label = myFont.render(textToFadeIn,1,(255,0,0))
    newSurf = pygame.Surface(myFont.size(textToFadeIn))
    newSurf.blit(label,(0,0))
    for x in range (225):
        newSurf.set_alpha(x - 255)
        screen.blit(newSurf, (100,100))
        pygame.display.flip()
        pygame.time.delay(20)