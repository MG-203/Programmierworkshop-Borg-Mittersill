import pygame
import random 

# Wir initialisieren das Spiel
pygame.init()

# erstellen des Bildschirms
screen = pygame.display.set_mode((800,600))

# Hintergrund
background = pygame.image.load("background.png")

# Titel und Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
changeX = 0

# Enemy
enemyImage = pygame.image.load("alien.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
changeEnemyX = 0.3
changeEnemyY = 40

def player(x,y): 
    screen.blit(playerImage, (x, y))

def enemy(x,y):
    screen.blit(enemyImage, (x, y))

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

    # Hintergrund
    screen.blit(background, (0, 0))

    # Spielerbewegung
    # Änderung der x-Achse übernehmen
    playerX = playerX + changeX

    # Grenzen überprüfen 
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Gegnerbewegung
    enemyX = enemyX + changeEnemyX
    if enemyX <= 0:
        changeEnemyX = 0.3
        enemyY = enemyY + changeEnemyY
    elif enemyX >= 736:
        changeEnemyX = -0.3
        enemyY = enemyY + changeEnemyY


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()