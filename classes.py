import pygame
from sys import exit
import random

pygame.init()
pygame.display.set_caption("Realoba")

# xem xashi xetqa saxetqelshi

class Global:
    def __init__(self, width, height, fps):
        self.width = width
        self.height = height
        self.fps = fps


class Art:
    def __init__(self, width, height, x, y, color, image):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.image = image

    def global_vars(self):
        back = pygame.surface.Surface((800, 400))
        back.fill(self.color)
        return back

    def rects(self):
        r = pygame.surface.Surface((self.width, self.height))
        r.fill(self.color)
        return r

    def images(self):
        elem = pygame.image.load(self.image)
        return elem


glob = Global(800, 400, 60)

WIDTH, HEIGHT = glob.width, glob.height
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = glob.fps

background = Art(800, 400, 0, 0, "Black", False)
player = Art(50, 50, 25, 175, "pink", False)
target = Art(100, 100, 650, 175, "purple", False)

line = Art(4, 400, 100, 0, "white", False)
bullet = Art(16, 4, player.x + 25, player.y + 23, "Red", False)
bullet_rect = bullet.rects().get_rect(midleft=(bullet.x, bullet.y))

shoot = False
missed = 0
recx, recy = WIDTH / 2, HEIGHT / 2

color_list = [(123, 42, 240), "Yellow", "Blue", (54, 240, 17), (200, 100, 200),
              (190, 56, 78), (100, 100, 100), (255, 0, 100), (255, 0, 255), (10, 200, 250)]

while True:
    target_rect = target.rects().get_rect(center=(recx, recy))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    display.blit(background.global_vars(), (background.x, background.y))

    # shooting bullet
    if shoot:
        display.blit(bullet.rects(), bullet_rect)
        bullet_rect.x += 16
        if bullet_rect.x >= WIDTH:
            missed += 1
            shoot = False
    else:
        if keys[pygame.K_SPACE]:
            bullet_rect.x = player.x + 25
            bullet_rect.y = player.y + 23
            shoot = True

    display.blit(player.rects(), (player.x, player.y))
    display.blit(target.rects(), target_rect)

    if target_rect.colliderect(bullet_rect):
        recx = random.randrange(200, 700)
        recy = random.randrange(25, 300)
        if target.width >= 10:
            target.width -= 2
            target.height -= 2
        bullet_rect.x = player.x + 25
        bullet_rect.y = player.y + 23
        target.color = (random.choice(color_list))

        shoot = False

    display.blit(line.rects(), (line.x, line.y))

    if player.y >= 0:
        if keys[pygame.K_UP]:
            player.y -= 5
    if player.y <= 350:
        if keys[pygame.K_DOWN]:
            player.y += 5

    if missed == 5:
        pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(FPS)