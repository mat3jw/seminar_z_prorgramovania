import pygame

#inicializacia
WIDTH = 1500
HEIGHT = 900
rect_width = 60
rect_height = 60
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
hra_pokracuje = True
x, y = 710, 390
dx, dy = 1, 1
#herna slucka
while hra_pokracuje:

    #spracovanie udalosti
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            hra_pokracuje = False
    

    #zmena stavu hry
    x += dx
    y += dy

    #rect_width = (rect_width + 1) % 100
    #rect_height = (rect_height + 1) % 30

    if not(0 <= x <= WIDTH - rect_width):
        dx = -dx

    if not(0 <= y <= HEIGHT - rect_height):
        dy = -dy


    #vykreslenie stavu hry
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 0, 255), (x , y , rect_width, rect_height))
    pygame.display.update()









pygame.quit()
