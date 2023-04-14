import pygame

pygame.init()


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music player")



sounds = [  "lab7/music/V $ X V PRiNCE - Модная подруга.mp3",
            "lab7/music/V $ X V PRiNCE - Суета.mp3",
            "lab7/music/V $ X V PRiNCE feat. De lacure - Су.mp3",
            "lab7/music/V $ X V PRiNCE feat. Tony Tonite - Карусель.mp3",
            "lab7/music/V $ X V PRiNCE feat. Кисло-Сладкий & Bonah - Дом 50 (Imanbek Remix).mp3",
            "lab7/music/V $ X V PRiNCE, De lacure - Жүрегімді.mp3",
            "lab7/music/V $ X V PRiNCE, Taspay - Ойлаш.mp3"
]



cnt_sounds = 0

pygame.mixer.music.load(sounds[cnt_sounds])


while True:

    

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()

                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_RETURN:
                pygame.mixer.music.play()


            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()


            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                cnt_sounds = (cnt_sounds + 1) % len(sounds)
                pygame.mixer.music.load(sounds[cnt_sounds])
                pygame.mixer.music.play()


            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                cnt_sounds = (cnt_sounds - 1) % len(sounds)
                if cnt_sounds < 0:
                    cnt_sounds == len(sounds) - 1 
                pygame.mixer.music.load(sounds[cnt_sounds])
                pygame.mixer.music.play()




    pygame.display.update()