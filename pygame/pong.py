import pygame

#inicializacia
WIDTH = 1500
HEIGHT = 900
ball_width = 30
ball_height = 30
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
hra_pokracuje = True
x, y = 710, 390
dx, dy = 2, 2
ball = pygame.Rect(x , y , ball_width, ball_height)
font = pygame.font.Font(None, 72)
score_left, score_right = 0, 0



clock = pygame.time.Clock()
racket1 = pygame.Rect(1/50*WIDTH, 1/3*HEIGHT, ball_width, 4*ball_height )
racket2 = pygame.Rect(WIDTH - 1/50*WIDTH - ball_width, HEIGHT - 1/3*HEIGHT, ball_width, 4*ball_height)



#herna slucka
while hra_pokracuje:

    #spracovanie udalosti
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            hra_pokracuje = False

    keys = pygame.key.get_pressed()
    #right
    if keys[pygame.K_w] and racket1.y > 0:
        racket1.y -= 2
    if keys[pygame.K_s] and racket1.y < HEIGHT - 4*ball_height:
        racket1.y += 2
    #left
    if keys[pygame.K_UP] and racket2.y > 0:
        racket2.y -= 2
    if keys[pygame.K_DOWN] and racket2.y < HEIGHT - 4*ball_height:
        racket2.y += 2

    

    #zmena stavu hry
    ball.x += dx
    ball.y += dy

        #odraz lopty
    if ball.colliderect(racket1) or ball.colliderect(racket2):
        dx = -dx

    if not(0 <= ball.x <= WIDTH - ball_width):
        ball.x = x
        ball.y = y

    if not(0 <= ball.y <= HEIGHT - ball_height):   
        dy = -dy

    if ball.x < 0:
        ball.x = WIDTH/2
        ball.y = HEIGHT/2
        score_right += 1

    if ball.x > WIDTH:
        ball.x = WIDTH/2
        ball.y = HEIGHT/2
        score_left += 1

    #vykreslenie stavu hry
    screen.fill((0, 0, 0))

    #line
    for i in range(0, HEIGHT, 70):
        pygame.draw.rect(screen, "white", (WIDTH // 2 - 5, i, 10, 30))

    #score

    text_left = font.render(str(score_left), True, "white")
    text_right = font.render(str(score_right), True, "white")
                             


    pygame.draw.rect(screen, "white", ball)
    pygame.draw.rect(screen, "palegreen", racket1)
    pygame.draw.rect(screen, "palegreen", racket2)
    screen.blit(text_left, (WIDTH // 4, 50))
    screen.blit(text_right, (WIDTH * 3 // 4, 50))
    pygame.display.update()
    





pygame.quit()
