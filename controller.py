import pygame, model
pygame.init()

pygame.key.set_repeat(20)
def events():
    t = pygame.event.get()
    for i in t:
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_d:
                model.move_ship_right()
            if i.key == pygame.K_a:
                model.move_ship_left()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                model.left_bullet_creation()

                model.right_bullet_creation()


