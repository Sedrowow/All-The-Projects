from sys import displayhook
from time import sleep
import pygame
numb = int(input("please put in the number that has to be converted:"))

screen_width = 400
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
screen1 = pygame.draw.line(surface=screen, color="white", start_pos=(0,100) , end_pos=(0,100))
test = input("done?")