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
    fullname = os.path.join('data', name) # Картинки у меня лежат в папке 'data'
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message: # Мало ли :)
        print "Cannot load image:", name
        raise SystemExit, message
    image = image.convert() # Адаптируем картинку для отображения в игре. Если на ней есть альфа-канал - тогда convert_alpha()
    return image, image.get_rect()
    
def draw_background():
    screen = pygame.display.get_surface() # Получаем поверхность, на которой будем рисовать
    background = pygame.Surface(screen.get_size()) # и ее размер
    background = background.convert()
    background.fill((0, 0, 0)) # заполняем цветом
    screen.blit(background, (0, 0)) # рисуем заполненный одним цветом бэкграунд
    back, back_rect = load_image("grass.jpg") # или загружаем картинку с травой
    screen.blit(back, (0, 0)) # и рисуем ее
    pygame.display.flip() # переключаем буфер экрана
    return back
    

def main():
    init_window()
    bk = draw_background()
    action()

print __name__
if __name__=='__main__':main()




