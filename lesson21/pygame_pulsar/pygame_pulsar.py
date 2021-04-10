import pygame

WIDTH = 400
HEIGHT = 400
BLUE = (0,0, 255)
YELLOW = (255,255,0)
FPS = 25

class Pulsural(pygame.sprite.Sprite):
    x = 10
    y = 10
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()

    def update(self):
        if 90 > self.x > 0:
            if 90 > self.y > 0:
                self.x += 1
                self.y += 1
                self.image = pygame.Surface((self.x, self.y))
                self.image.fill(YELLOW)
                self.rect = self.image.get_rect()
                self.rect.center = (WIDTH / 2, HEIGHT / 2)
        else:
            self.x = 50
            self.y = 50

pygame.init()
pygame.mixer.init()
game_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame pulsar')
clock = pygame.time.Clock()
final = pygame.sprite.Group()
inner_rect = Pulsural()
# final.add(inner_rect)

done = False
while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    game_screen.fill(BLUE)
    final.draw(game_screen)
    final.add(inner_rect)
    final.update()
    pygame.display.flip()

pygame.quit()