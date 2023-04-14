import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill("White")
pygame.display.set_caption("circle")
x_circle = 250
y_circle = 250

clock = pygame.time.Clock()


while True:

    pygame.draw.circle(screen, "Red", (x_circle, y_circle), 25)

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y_circle > 30: y_circle -= 20
    if pressed[pygame.K_DOWN] and y_circle < 470: y_circle += 20
    if pressed[pygame.K_LEFT] and x_circle > 30: x_circle -= 20
    if pressed[pygame.K_RIGHT] and x_circle < 470: x_circle += 20


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            pygame.quit()

    screen.fill("White")
            
    clock.tick(60)