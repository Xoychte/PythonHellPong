import pygame
from pygame.locals import*
from random import randint

FPS = 60
(windowWidth, windowHeight) = (1300, 900)

GREY = (30,30,30)
lightGREY = (100,100,100)
BLACK = (0,0,0)

ballX = windowWidth/2
ballY = windowHeight/2
ballRadius = 10
ballSpeedX = randint(5,10)
ballSpeedY = 5
ballColor = lightGREY
maxBallSpeed = 23

wallMovement = 0
wallX = windowWidth - 100

paddleX = 5
paddleY = windowHeight/2
momentum = 0

newScore = 0
score = 0
cheat = True
fontSize = 12
newFontSize= 12

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((windowWidth, windowHeight), RESIZABLE)
window.fill(GREY)
font_obj = pygame.font.Font('freesansbold.ttf', fontSize)
paddle = pygame.image.load("paddle32_100.png").convert_alpha()


continuer = True
pygame.key.set_repeat(10,10)
def update_momentum(momentum):
    if momentum > 0:
        return momentum - 1
    if momentum < 0:
        return momentum + 1
    return 0

def place_elements(windowWidth, windowHeight, lightGREY, ballX, ballY, ballRadius, ballColor, wallX, paddleX, paddleY, fontSize, window, paddle, text1_obj):
    window.blit(paddle, (paddleX,paddleY))
    pygame.draw.circle(window, ballColor, (ballX, ballY), ballRadius)
    pygame.draw.rect(window, lightGREY, (wallX, 0, windowWidth-wallX, windowHeight))
    window.blit(text1_obj, (windowWidth-((windowWidth - wallX)/2)-fontSize,windowHeight/2-fontSize/2))

while continuer == True:
    clock.tick(FPS)
    window.fill(GREY)
    
    font_obj = pygame.font.Font('freesansbold.ttf', fontSize)
    text1_obj = font_obj.render(str(score), True, BLACK, lightGREY)
    
    for event in pygame.event.get() :
        if event.type == QUIT:
            continuer = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and paddleY >0:
            paddleY -=5
            momentum = -10
        elif keys[pygame.K_DOWN] and paddleY + 100 < windowHeight:
            paddleY +=5
            momentum = 10
        elif keys[pygame.K_RIGHT] and cheat == True:
            paddleY = ballY-50
            
    
    momentum = update_momentum(momentum)
    ballX += ballSpeedX
    ballY += ballSpeedY
    
    if ballX < paddleX+35 and  paddleY<ballY<paddleY+100:
        print("hit paddle")
        ballSpeedX *= -1
        newScore+=abs(ballSpeedX)
        newFontSize = abs(ballSpeedX)*2
        ballSpeedY +=int(momentum/2)
        print("hit ball with", momentum, "momentum")

    
    
    if ballX > wallX-ballRadius:        
        wallMovement = 15
        if ballSpeedY == 0:
            ballSpeedY = randint(-5,5)       
        if abs(ballSpeedX) >= maxBallSpeed:
            ballSpeedX = maxBallSpeed
            print("max speed reached")
            ballSpeedY = randint(-4,4)
        else:  
            ballSpeedX += randint(0,2)      
            print("new ball speed=", ballSpeedX)
        ballSpeedX *= -1
    if  ballX < ballRadius :
        print("lost")
        pygame.quit()
    if ballY < ballRadius:       
        if ballSpeedY < 0:
            ballSpeedY = ballSpeedY / abs(ballSpeedY) * randint(1,5)
            ballSpeedY *= -1
            print("new vertical speed=", ballSpeedY)
        print("hit upper wall")
    if ballY > windowHeight - ballRadius:
        if ballSpeedY > 0:
            ballSpeedY = ballSpeedY / abs(ballSpeedY) * randint(1,5)
            ballSpeedY *= -1
            print("new vertical speed=", ballSpeedY)
        print("hit lower wall")

    
    if wallMovement > 0 and wallMovement <= 12:
        wallX -= 1
        wallMovement -=1
    if score < newScore:
        score+=1
    if wallMovement > 12:
        wallMovement -=1
    if fontSize < newFontSize:
        fontSize +=1
    
    place_elements(windowWidth, windowHeight, lightGREY, ballX, ballY, ballRadius, ballColor, wallX, paddleX, paddleY, fontSize, window, paddle, text1_obj)
    pygame.display.flip()
pygame.quit()
    