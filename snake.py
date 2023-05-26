import pygame
import random

pygame.init()

yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)

white = (255, 255, 255)

dis = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Snake Game by Pythonist')
clock = pygame.time.Clock()
game_over = False

x1 = 391
y1 = 289

x1_change = 0
y1_change = 0

List = []  # для хранения координат всех квадратов змейки
Length_of_snake = 1  # для счёта

# задаём рандомные координаты для еды
x2 = random.randrange(51, 595, 17)
y2 = random.randrange(51, 340, 17)

while not game_over:
    background_image = pygame.image.load('static/img/background-image.jpg')
    # отображение счёта
    schet = pygame.font.SysFont("calibri", 35).render("Счёт: " + str(Length_of_snake - 1), True, yellow)
    dis.blit(background_image,  [0, 0])
    dis.blit(schet, [0, 0])  # копирование текста на экран
    pygame.display.update()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -17
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 17
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -17
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 17
                x1_change = 0

    if x1 >= 800 or x1 < 0 or y1 >= 500 or y1 < 0:
        game_over = True
    x1 += x1_change
    y1 += y1_change
    pygame.draw.rect(dis, red, [x2, y2, 17, 17])
    snake_Head = [] # для хранения координат змейки
    snake_Head.append(x1)
    snake_Head.append(y1)
    List.append(snake_Head)

    if len(List) > Length_of_snake:
        del List[0]  # удаляет не нужные координаты

    # когда змейка проходит прикасается к себе игра заканчивается
    for x in List[:-1]:
        if x == snake_Head:
            game_over = True

    for x in List:
        pygame.draw.rect(dis, black, [x[0], x[1], 17, 17])  # появляется змейка

    pygame.display.update()

    # когда змейка прикасается к еде еда меняет своё местоположение и плюс увеличивается счёт
    if x1 == x2 and y1 == y2:
        x2 = random.randrange(51, 595, 17)
        y2 = random.randrange(51, 340, 17)
        Length_of_snake += 1

    clock.tick(15)

pygame.quit()
quit()