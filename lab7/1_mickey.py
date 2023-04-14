import pygame, datetime

pygame.init()

width = 650
hight = 650

screen = pygame.display.set_mode((width, hight))

mickey = pygame.image.load("lab7/images/mickey.jpg")
hand_m = pygame.image.load("lab7/images/hand_m.png").convert_alpha()
hand_s = pygame.image.load("lab7/images/hand_s.png").convert_alpha()


hand_m_rect = hand_m.get_rect()
hand_m_rect.center = screen.get_rect().center


hand_s_rect = hand_s.get_rect()
hand_s_rect.center = screen.get_rect().center


mickey = pygame.transform.scale(mickey, (width, hight))
hand_m = pygame.transform.scale(hand_m, (width - 300, hight - 400))
hand_s = pygame.transform.scale(hand_s, (width - 200, hight - 400))






angle = 0

fps = pygame.time.Clock()






font = pygame.font.Font(None, 36)








while True:

    now = datetime.datetime.now()

    minute = now.minute
    second = now.second

    second_angle = -second * 6
    minute_anlge = -minute * 6


    hand_m_rotated = pygame.transform.rotate(hand_m, minute_anlge + 82)
    hand_m_rotated_rect = hand_m_rotated.get_rect(center = hand_m_rect.center)

    hand_s_rotated = pygame.transform.rotate(hand_s, second_angle + 84)
    hand_s_rotated_rect = hand_s_rotated.get_rect(center = hand_s_rect.center)



    screen.blit(mickey, (0, 0))
    screen.blit(hand_m_rotated, hand_m_rotated_rect)
    screen.blit(hand_s_rotated, hand_s_rotated_rect)


    txt = str(minute) + " : " + str(second)

    time_text = font.render(txt, True, (0, 0, 0))

    screen.blit(time_text, (0, 0))




    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            False
            pygame.quit()

    fps.tick(60)