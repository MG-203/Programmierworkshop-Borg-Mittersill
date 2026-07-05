import pygame
import random
import math
from pygame import mixer

# wir initialisieren (erstellen) das Spiel.
pygame.init()

# erstellen des Bildschirms
screen = pygame.display.set_mode((800,600))

# Hintergrund
background = pygame.image.load('background.png')

# Hintergrundmusik
mixer.music.load('background.mp3')
mixer.music.play(-1)

# Titel and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
changeX = 0

# Enemy
enemyX = []
enemyY = []
changeXenemy = []
changeYenemy = []
NumberOfEnemies = 8

for i in range(NumberOfEnemies):
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    changeXenemy.append(0.3)
    changeYenemy.append(40)

enemyImage = pygame.image.load('alien.png')

# Bullet
bulletImage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
changeXbullet = 0
changeYbullet = 0.5
bulletState = "ready"
# bulletState ready -> man kann die Kugel nicht sehen
# bulletState fire -> man kann die Kugel sehen

# Score
score = 0
highscore = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
gameOverFont = pygame.font.Font('freesansbold.ttf', 64)
gameOverState = False

def player(x, y): 
    screen.blit(playerImage, (x, y))

def enemy(x, y): 
    screen.blit(enemyImage, (x, y))

def fireBullet(x,y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImage, (x + 16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 25:
        return True
    else: 
        return False
    
def showScore(x,y):
    scorePicture = font.render("Score: "+ str(score), True, (255,255,255))
    screen.blit(scorePicture, (x,y))

def showHighScore(x,y):
    scorePicture = font.render("HighScore: "+ str(highscore), True, (255,255,255))
    screen.blit(scorePicture, (x,y))

def gameOverText(): 
    gameOverPicture = gameOverFont.render("GAME OVER!", True, (255,0,0))
    screen.blit(gameOverPicture, (200,250))

def resetGame():
    global playerX, playerY, changeX, enemyX, enemyY, changeXenemy, changeYenemy, NumberOfEnemies, bulletX, bulletY, changeXbullet, changeYbullet, bulletState, gameOverState, score
    playerX = 370
    playerY = 480
    changeX = 0

    # Enemy
    enemyX = []
    enemyY = []
    changeXenemy = []
    changeYenemy = []
    NumberOfEnemies = 8

    for i in range(NumberOfEnemies):
        enemyX.append(random.randint(0,736))
        enemyY.append(random.randint(50,150))
        changeXenemy.append(0.3)
        changeYenemy.append(40)

    gameOverState = False

    # Bullet
    bulletX = 0
    bulletY = 480
    changeXbullet = 0
    changeYbullet = 0.5
    bulletState = "ready"

    score = 0


# Gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # uberprufe, ob beim Drucken der Tastatur die Linkspfeiltaste oder Rechtspfeiltaste gedruckt wird
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -0.3
            if event.key == pygame.K_RIGHT:
                changeX = 0.3
            if event.key == pygame.K_SPACE and bulletState is "ready":
                bulletSound = mixer.Sound('shot.mp3')
                bulletSound.play()
                bulletX = playerX
                fireBullet(bulletX, bulletY) 
            if event.key == pygame.K_SPACE and gameOverState == True: 
                resetGame()

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                changeX = 0

    # RGB
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background,(0,0))

	# Anderung der x-Koordinate ubernehmen
    playerX = playerX + changeX
    
    # Grenzen uberprufen
    if playerX <= 0: 
        playerX = 0
    elif playerX > 736:
        playerX = 736

    # Highscore aktualisieren
    if score > highscore:
        highscore = score
    # Bewegung des Gegners
    for i in range(NumberOfEnemies):

        # Gameover 
        if enemyY[i] > 420: 
            for j in range(NumberOfEnemies):
                enemyY[j] = 2000
            gameOverText()
            gameOverState = True
            break

        enemyX[i] = enemyX[i] + changeXenemy[i]
        if enemyX[i] <= 0:
            changeXenemy[i] = 0.3
            enemyY[i] += changeYenemy[i]
        elif enemyX[i] > 736:
            changeXenemy[i] = -0.3
            enemyY[i] += changeYenemy[i]
        
        # Kollision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound('explosion.mp3')
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
        bulletY -= changeYbullet

        
    player(playerX, playerY)
    showScore(textX, textY)
    showHighScore(10,45)
    pygame.display.update()