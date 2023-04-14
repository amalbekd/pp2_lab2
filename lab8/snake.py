import pygame, random, sys


pygame.init()


width, hight = 600, 600

block_size = 30



font = pygame.font.SysFont("Verdana", 20)
FONT = pygame.font.SysFont("Verdana", 20)

lvl = 1

screen = pygame.display.set_mode((width, hight))

pygame.display.set_caption("Snake")


clock = pygame.time.Clock()
fps = 5



class Snake:
    def __init__(self):

        self.x = block_size
        self.y = block_size

        self.xdir, self.ydir = 1, 0

        self.head = pygame.Rect(self.x, self.y, block_size, block_size)
        self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]
        self.dead = False

    def update(self):
        global apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, width) or self.head.y not in range(0, hight):
                self.dead = True



        if self.dead:

            self.x, self.y = block_size, block_size

            self.head = pygame.Rect(self.x, self.y, block_size, block_size)
            self.body = [pygame.Rect(self.x - block_size, self.y, block_size, block_size)]

            self.xdir, self.ydir = 1, 0
            self.dead = False

            apple = Apple()


        
        self.body.append(self.head)

        for i in range(len(self.body) - 1):

            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y

        self.head.x += self.xdir * block_size
        self.head.y += self.ydir * block_size
        self.body.remove(self.head)



class Apple:
    def __init__(self):

        self.x = int(random.randint(0, width) / block_size) * block_size
        self.y = int(random.randint(0, hight) / block_size) * block_size

        self.rect = pygame.Rect(self.x, self.y, block_size, block_size)

    def update(self):
        pygame.draw.rect(screen, "Orange", self.rect)


score = FONT.render("1", True, "White")

level = font.render("level: " + str(lvl), True, (255,255,255))

score_rect = score.get_rect(center=(width / 2, hight / 20))

screen.blit(level, (150, 10))

S1 = Snake()
A1 = Apple()



while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_DOWN:
                S1.ydir = 1
                S1.xdir = 0
            elif event.key == pygame.K_UP:
                S1.ydir = -1
                S1.xdir = 0
            elif event.key == pygame.K_RIGHT:
                S1.ydir = 0
                S1.xdir = 1
            elif event.key == pygame.K_LEFT:
                S1.ydir = 0
                S1.xdir = -1


    if len(S1.body) + 1 > 0:


        S1.update()

        screen.fill('Black')

        A1.update()

        score = FONT.render(f"{len(S1.body) + 1}", True, "white")
        level = font.render("level: " + str(lvl), True, (255,255,255))
        screen.blit(level, (150, 10))

        pygame.draw.rect(screen, "Green", S1.head)
        for square in S1.body:
            pygame.draw.rect(screen, "Green", square)

        screen.blit(score, score_rect)

        if S1.head.x == A1.x and S1.head.y == A1.y:
            S1.body.append(pygame.Rect(square.x, square.y, block_size, block_size))
            A1 = Apple()

    else:
        S1.update()

        screen.fill('Black')

        apple.update()

        score = FONT.render(f"{len(S1.body) + 1}", True, "White")
        level = font.render("level: " + str(lvl), True, "White")
        screen.blit(level, (150, 10))

        pygame.draw.rect(screen, "Green", S1.head)
        for square in S1.body:
            pygame.draw.rect(screen, "Green", square)

        screen.blit(score, score_rect)


    pygame.display.update()

    
    clock.tick(fps)