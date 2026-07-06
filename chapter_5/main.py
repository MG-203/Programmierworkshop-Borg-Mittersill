import pygame
import random 
import math
from pygame import mixer

# Wir initialisieren das Spiel
pygame.init()

# erstellen des Bildschirms
screen = pygame.display.set_mode((800,600))

# Hintergrund
background = pygame.image.load("background.png")

# Hintergrundmusik 
mixer.music.load("background.mp3")
mixer.music.play(-1)

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
enemyX = []
enemyY = []
changeEnemyX = []
changeEnemyY = []
NumberOfEnemies = 6

for i in range(NumberOfEnemies):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    changeEnemyX.append(0.3)
    changeEnemyY.append(40)
enemyImage = pygame.image.load("alien.png")

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
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10 
textY = 10

# Game Over Text
gameOverFont = pygame.font.Font("freesansbold.ttf", 64)
gameOverState = False

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
 
def showScore(x,y):
    scorePicture = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(scorePicture, (x, y))

def gameOverText(): 
    gameOverPicture = gameOverFont.render("GAME OVER!", True, (255,0,0))
    screen.blit(gameOverPicture, (200,250))

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
                bulletSound = mixer.Sound("shot.mp3")
                bulletSound.play()
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
    for i in range(NumberOfEnemies):
        enemyX[i] = enemyX[i] + changeEnemyX[i]  

        # Game Over
        if enemyY[i] > 420: 
            for j in range(NumberOfEnemies): 
                enemyY[j] = 2000
            gameOverText()
            break

        if enemyX[i] <= 0:
            changeEnemyX[i] = 0.3
            enemyY[i] = enemyY[i] + changeEnemyY[i]
        elif enemyX[i] >= 736:
            changeEnemyX[i] = -0.3
            enemyY[i] = enemyY[i] + changeEnemyY[i]

        # Kollision 
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision: 
            explosionSound = mixer.Sound("explosion.mp3")
            explosionSound.play()
            bulletY = 480
            bulletState = "ready"
            score += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i])   

    # Bewegung der Kugel
    if bulletY < -20: 
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire": 
        fireBullet(bulletX, bulletY)
        bulletY -= changeYBullet

    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()