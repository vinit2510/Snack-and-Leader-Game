import random
import pygame
from pygame import mixer


# All position
pos = [(5, 545), (65, 545), (125, 545), (185, 545), (245, 545), (305, 545), (365, 545), (425, 545), (485, 545), (545, 545),
       (545, 485), (485, 485), (425, 485), (365, 485), (305,485), (245, 485), (185, 485), (125, 485), (65, 485), (5, 485),
       (5, 425), (65, 425), (125, 425), (185, 425), (245, 425), (305,425), (365, 425), (425, 425), (485, 425), (545, 425),
       (545, 365), (485, 365), (425, 365), (365, 365), (305,365), (245, 365), (185, 365), (125, 365), (65, 365), (5, 365),
       (5, 305), (65, 305), (125, 305), (185, 305), (245, 305), (305,305), (365, 305), (425, 305), (485, 305), (545, 305),
       (545, 245), (485, 245), (425, 245), (365, 245), (305,245), (245, 245), (185, 245), (125, 245), (65, 245), (5, 245),
       (5, 185), (65, 185), (125, 185), (185, 185), (245, 185), (305,185), (365, 185), (425, 185), (485, 185), (545, 185),
       (545, 125), (485, 125), (425, 125), (365, 125), (305,125), (245, 125), (185, 125), (125, 125), (65, 125), (5, 125),
       (5, 65), (65, 65), (125, 65), (185, 65), (245, 65), (305,65), (365, 65), (425, 65), (485, 65), (545, 65),
       (545, 5), (485, 5), (425, 5), (365, 5), (305,5), (245, 5), (185, 5), (125, 5), (65, 5), (5, 5)]


snakes = {35: 4, 48: 6, 55: 7, 81: 19, 86: 65, 94: 37}
ladders = {5: 34, 8: 50, 22: 41, 47: 85, 61: 82, 68: 90}


pygame.init()
mixer.init()


def play_music(file):
    mixer.music.load(file)
    mixer.music.set_volume(1)
    mixer.music.play()


x = 600
y = 684

# main window
display = pygame.display.set_mode((x, y), pygame.RESIZABLE)

# images
board_img = pygame.image.load(r'src\\board_600x600.jpg')
red_img = pygame.image.load(r'src\\red_arrow_50x50.png')
blue_img = pygame.image.load(r'src\\blue_arrow_50x50.png')
blue_turn_img = pygame.image.load(r'src\\blue_turn.png')
red_turn_img = pygame.image.load(r'src\\red_turn.png')
black_bar_img = pygame.image.load(r'src\\black_bar1.png')
black_bar_img1 = pygame.image.load(r'src\\black_bar.png')
blue_won_img = pygame.image.load(r'src\\blue_won.png')
red_won_img = pygame.image.load(r'src\\red_won.png')
icon_img = pygame.image.load(r'src\\icon.png')


pygame.display.set_icon(icon_img)
pygame.display.set_caption('src')

clock = pygame.time.Clock()

c = 0
blue_count = 0
red_count = 0
blue_old = 0
red_old = 0
temp = 0
rand_num = 0


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # for Exit
            pygame.quit()
            quit()

    pygame.event.get()
    keys = pygame.key.get_pressed()

    # Blue
    if c % 2 == 0:

        blue_old = blue_count

        display.blit(black_bar_img, (0, 600))
        display.blit(blue_turn_img, (100, 610))

        if keys[pygame.K_SPACE]:

            play_music("src\\dice.wav")

            rand_num = random.randrange(1, 7)
            display.blit(pygame.image.load(
                f'src\\dice{str(rand_num)}_70x70.jpg'), (7, 607))
            blue_count = blue_count + rand_num

            pygame.time.wait(1000)

            # if rand_num == 6:
            #    c = c - 1

            if blue_count in snakes:
                play_music("src\\snake.wav")
                blue_count = snakes[blue_count]

                for i in range(blue_old, blue_count, -1):
                    display.blit(blue_img, pos[i])
                    pygame.time.wait(10)
                    pygame.display.update()
                    display.blit(board_img, (0, 0))
                    display.blit(red_img, pos[red_count])

            if blue_count in ladders:
                play_music("src\\ladder.mp3")
                temp = blue_count
                blue_count = ladders[blue_count]
            if blue_count > 99:
                blue_count = blue_count-rand_num
            if blue_count == 99:
                play_music("src\\won.mp3")
                c = c - 1
            c = c + 1

        #
        if blue_old != blue_count:
            for i in range(blue_old, blue_count):

                display.blit(blue_img, pos[i])

                if temp in ladders:
                    pygame.time.wait(12)
                else:
                    pygame.time.wait(300)

                pygame.display.update()
                display.blit(board_img, (0, 0))
                display.blit(red_img, pos[red_count])
            temp = 0

    # Red
    if c % 2 == 1:

        red_old = red_count

        display.blit(black_bar_img, (300, 600))
        display.blit(red_turn_img, (100, 610))

        if keys[pygame.K_UP]:

            play_music("src\\dice.wav")

            rand_num = random.randrange(1, 7)
            display.blit(pygame.image.load(
                f'src\\dice{str(rand_num)}_70x70.jpg'), (523, 607))
            red_count = red_count + rand_num

            pygame.time.wait(1000)

            if red_count in snakes:
                play_music("src\\snake.wav")

                red_count = snakes[red_count]

                for i in range(red_old, red_count, -1):
                    display.blit(red_img, pos[i])
                    pygame.time.wait(10)
                    pygame.display.update()
                    display.blit(board_img, (0, 0))
                    display.blit(blue_img, pos[blue_count])

            if red_count in ladders:
                play_music("src\\ladder.mp3")
                temp = red_count
                red_count = ladders[red_count]
            if red_count > 99:
                red_count = red_count-rand_num
            if red_count == 99:
                play_music("src\\won.mp3")
                c = c - 1
            c = c + 1

        if red_old != red_count:
            for i in range(red_old, red_count):

                display.blit(red_img, pos[i])

                if temp in ladders:
                    pygame.time.wait(12)
                else:
                    pygame.time.wait(300)

                pygame.display.update()
                display.blit(board_img, (0, 0))
                display.blit(blue_img, pos[blue_count])
            temp = 0

    display.blit(board_img, (0, 0))
    display.blit(red_img, pos[red_count])
    display.blit(blue_img, pos[blue_count])

    # win
    if blue_count == 99:
        display.blit(black_bar_img1, (0, 600))
        display.blit(blue_won_img, (100, 610))
    if red_count == 99:
        display.blit(black_bar_img1, (0, 600))
        display.blit(red_won_img, (100, 610))

    pygame.display.update()
    clock.tick(60)
