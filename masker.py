from operator import truediv
import pygame

pygame.init()

print("helloooo")

screen = pygame.display.set_mode((1600, 1600))

player1 = pygame.Rect((100, 50, 50, 50))
img1 = pygame.image.load("11-2-minecraft-diamond-png.png")

run = True
while run:
    # print("23")

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (200, 10, 10), player1)
    screen.blit(img1, [10,10])

    # movements
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        print("23")
        player1.move_ip(-1, 0)
    if key[pygame.K_d] == True:
        print("25")
        player1.move_ip(1, 0)
    if key[pygame.K_s] == True:
        print("22")
        player1.move_ip(1, 0)
    if key[pygame.K_w] == True:
        print("21")
        player1.move_ip(1, 0)
    if key[pygame.K_t] == True:
        run=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

pygame.quit()