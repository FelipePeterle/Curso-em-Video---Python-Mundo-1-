#Faça um programa em Python que abra e
#Reproduza o áudio de um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.music.load('manga.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()