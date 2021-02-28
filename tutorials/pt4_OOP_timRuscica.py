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

class Player(object):

    def __init__(self, x, y, width, height):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.color = (255,100,0)
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):

        if self.walkCount + 1 >= 6:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x,self.y))


def redrawGameWindow():
    win.blit(bg, (0,0))
    billy.draw(win)    
    pygame.display.update()

#main loop
billy = Player(20,102,183,378)
run = True
while run:
    clock.tick(18)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and billy.x > billy.vel:
        billy.x -= billy.vel
        billy.left = True
        billy.right = False
    elif keys[pygame.K_RIGHT] and billy.x < screenWidth - billy.vel - billy.width:
        billy.x += billy.vel
        billy.left = False
        billy.right = True
    else:
        billy.left = False
        billy.right = False
        billy.walkCount = 0

    if not billy.isJump:
        if keys[pygame.K_SPACE]:
            billy.isJump = True
            billy.left = False
            billy.right = False
            billy.walkCount = 0
    else:
        if billy.jumpCount >= -10:
            neg = 1
            if billy.jumpCount < 0:
                neg = - 1
            billy.y -= (billy.jumpCount ** 2) * .5 * neg
            billy.jumpCount -= 1
        else:
            billy.isJump = False
            billy.jumpCount = 10

    if keys[pygame.K_c]:
        color = (random.randint(0,255), random.randint(0,255), 0)
    if keys[pygame.K_PLUS]:
        billy.width += 1
        billy.height += 1
    if keys[pygame.K_MINUS]:
        billy.width -= 1
        billy.height -= 1
    
    redrawGameWindow()

pygame.quit()