import pygame, random
pygame.init()
win = pygame.display.set_mode((800,700))
pygame.display.set_caption("First Game")

x = 50
y = 50 
width = 3
height = 3
vel = 1

color = (255,100,0)

run = True
while run:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_SPACE]:
        color = (random.randint(0,255), random.randint(0,255), 0)
    if keys[pygame.K_PLUS]:
        width += 1
        height += 1
    if keys[pygame.K_MINUS]:
        width -= 1
        height -= 1
    
    #win.fill((0,0,0))
    pygame.draw.rect(win, color, (x, y, width, height) )
    pygame.display.update()

pygame.quit()