import pygame

# Wir initialisieren das Spiel
pygame.init()

# erstellen des Bildschirms
screen = pygame.display.set_mode((800,600))

# Titel und Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480

def player(): 
    screen.blit(playerImage, (playerX, playerY))

# Gameloop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB
    screen.fill((0, 0, 0))

    player()
    pygame.display.update()