import random
import pygame
import sys
import  subprocess
import moviepy.editor
import subprocess


import os

from  os import  startfile



start1=pygame.image.load('start1.png')
start2=pygame.image.load('start2.png')
start3=pygame.image.load('start3.png')
# os.chdir('C:\\Users\jacek\PycharmProjects\pythonProject3\zasoby\zaso')
lista_zdjec=[]
# directory = 'C:\Users\jacek\PycharmProjects\pythonProject3\zasoby\zaso'


lista_zdjec.append(start1)
lista_zdjec.append(start2)


def fotogen():
    x = random.randrange(0, len(lista_zdjec))
    przechowaj = lista_zdjec[x]
    lista_zdjec.pop(x)
    return przechowaj





screen=pygame.display.set_mode((1550,800))
pygame.display.set_caption("Images in Pygame!f")


current_image=start2
a=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_RIGHT:
                #     if current_image==start2:
                #         current_image=start1
                #         if current_image==start1:
                #             current_image=start3
                #                     # open(filename)
                #
                # image_rect = current_image.get_rect()
                # screen.blit(current_image, image_rect)
                # pygame.display.update()
                # #

                if event.key == pygame.K_SPACE:
                    try:
                        a = fotogen()
                        a = pygame.transform.scale(a, (1550, 800))

                        foto_rect = a.get_rect(topleft=(0, 0))
                        screen.blit(a, foto_rect)
                    except:
                        video = moviepy.editor.VideoFileClip("gesty2.mp4")
                        video.preview()
                        video.preview()
                        video.preview()

                        pygame.quit()



        pygame.display.update()
        # if event.type == pygame.KEYDOWN:
        #
        #
        #
        #
        #
        #
        # image_rect = current_image.get_rect()
        # screen.blit(current_image, image_rect)
        # pygame.display.update()
        #



