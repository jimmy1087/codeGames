import pygame, random
pygame.init()

screenWidth = 852
screenHeight = 480

walkRight = [pygame.image.load('tutorials/img/Walk1.png'), pygame.image.load('tutorials/img/Walk2.png'), pygame.image.load('tutorials/img/Walk3.png'), pygame.image.load('tutorials/img/Walk4.png'), pygame.image.load('tutorials/img/Walk5.png'), pygame.image.load('tutorials/img/Walk6.png')]
walkLeft = [pygame.image.load('tutorials/img/Walk1.png'), pygame.image.load('tutorials/img/Walk2.png'), pygame.image.load('tutorials/img/Walk3.png'), pygame.image.load('tutorials/img/Walk4.png'), pygame.image.load('tutorials/img/Walk5.png'), pygame.image.load('tutorials/img/Walk6.png')]
bg = pygame.image.load('tutorials/img/bg.jpg')
char = pygame.image.load('tutorials/img/Idle1.png')

clock = pygame.time.Clock()

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

x = 20
y = 102
width = 183
height = 378
vel = 10
color = (255,100,0)
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))

    if walkCount + 1 >= 6:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x,y))

    pygame.display.update()

#main loop
run = True
while run:
    clock.tick(18)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - vel - width:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = - 1
            y -= (jumpCount ** 2) * .5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    if keys[pygame.K_c]:
        color = (random.randint(0,255), random.randint(0,255), 0)
    if keys[pygame.K_PLUS]:
        width += 1
        height += 1
    if keys[pygame.K_MINUS]:
        width -= 1
        height -= 1
    
    redrawGameWindow()

pygame.quit()