import sys
import pygame



"""
Graphics


pygame.init()
window = pygame.display.set_mode((600,600))
pygame.draw.line(window,(255,255,255),(0,200),(600,200))
pygame.draw.line(window,(255,255,255),(0,400),(600,400))
pygame.draw.line(window,(255,255,255),(200,0),(200,600))
pygame.draw.line(window,(255,255,255),(400,0),(400,600))
pygame.display.flip()

while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event 
"""
pygame.init()
screen = pygame.display.set_mode([600,600])
background = pygame.Surface(screen.get_size())
b= pygame.sprite.Sprite()
b.image = pygame.image.load("circle.png").convert
b.rect = b.image.get_rect()
b.rect.topleft = [0,0]
screen.blit(b.image,b.rect)
pygame.display.update()


"""
Menace

"""








