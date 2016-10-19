import sys
import pygame
from pygame.locals import *
import os

def init_window():
    pygame.init()
    window=pygame.display.set_mode((640,480))
    pygame.display.set_caption('My game window')

def input(events):
    for event in events:
        if(event.type==QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            sys.exit(0)
        else:
            pass

def action():
    while 1:
        input(pygame.event.get())

def load_image(name):
    fullname = os.path.join('data', name) # �������� � ���� ����� � ����� 'data'
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message: # ���� �� :)
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert() # ���������� �������� ��� ����������� � ����. ���� �� ��� ���� �����-����� - ����� convert_alpha()
    return image, image.get_rect()
    
def draw_background():
    screen = pygame.display.get_surface() # �������� �����������, �� ������� ����� ��������
    background = pygame.Surface(screen.get_size()) # � �� ������
    background = background.convert()
    background.fill((0, 0, 0)) # ��������� ������
    screen.blit(background, (0, 0)) # ������ ����������� ����� ������ ���������
    back, back_rect = load_image("grass.jpg") # ��� ��������� �������� � ������
    screen.blit(back, (0, 0)) # � ������ ��
    pygame.display.flip() # ����������� ����� ������
    return back
    

def main():
    init_window()
    bk = draw_background()
    action()

print __name__
if __name__=='__main__':main()




