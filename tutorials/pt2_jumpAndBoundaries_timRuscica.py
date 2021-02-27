import pygame, random
pygame.init()

screenWidth = 800
screenHeight = 700

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

x = 50
y = 50 
width = 5
height = 3
vel = 10

color = (255,100,0)

isJump = False
jumpCount = 5

run = True
while run:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < screenWidth - vel - width:
        x += vel

    if not isJump:
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screenHeight - vel - height:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
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
    
    win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height) )
    pygame.display.update()

pygame.quit()