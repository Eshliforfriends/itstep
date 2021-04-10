import pygame
import os

WIDTH = 400
HEIGHT = 400
BLUE = (0,0, 255)
YELLOW = (255,255,0)
FPS = 40
x = 10
y = 10

pygame.init()
pygame.mixer.init()
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame introduction')
clock = pygame.time.Clock()
my_rect = pygame.Rect(150,150,90,90)

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    game_screen.fill(BLUE)
    pygame.draw.rect(game_screen, YELLOW, my_rect)
    pygame.display.flip()

pygame.quit()