import pygame
import random 
import math

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

# Bullet 
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
changeXBullet = 0 
changeYBullet = 0.5
bulletState = "ready"
# bulletState ready -> man kann die Kugel nicht sehen
# bulletState fire -> man kann die Kugel sehen

# Score 
score = 0 

def player(x,y): 
    screen.blit(playerImage, (x, y))

def enemy(x,y):
    screen.blit(enemyImage, (x, y))

def fireBullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY): 
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 25: 
        return True
    else: 
        return False
 
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
            if event.key == pygame.K_SPACE and bulletState == "ready":
                bulletX = playerX
                fireBullet(bulletX, bulletY)
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

    # Bewegung der Kugel
    if bulletY < -20: 
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire": 
        fireBullet(bulletX, bulletY)
        bulletY -= changeYBullet

    # Kollision 
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision: 
        bulletY = 480
        bulletState = "ready"
        score += 1
        enemyX = random.randint(0,736)
        enemyY = random.randint(50,150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()