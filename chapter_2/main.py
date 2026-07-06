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
changeX = 0

def player(x,y): 
    screen.blit(playerImage, (x, y))

# Gameloop
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # überprüfen, ob eine Taste gedrückt wird
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -0.3
            if event.key == pygame.K_RIGHT:
                changeX = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0

    # RGB
    screen.fill((0, 0, 0))

    playerX = playerX + changeX
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()