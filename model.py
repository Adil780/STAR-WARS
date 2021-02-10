import pygame, settings, random, view

pygame.init()

left_bullet = None
right_bullet = None

ship = pygame.Rect(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT - 150, 101, 110)
ship.centerx = settings.SCREEN_WIDTH / 2

round = 1
basespeed = 10
speedx = basespeed
speedy = basespeed

enemy = []
bullets = []


def right_bullet_creation():
    right_bullet = pygame.Rect(ship.right, ship.top, 3, 20)
    if len(bullets) < 5:
        bullets.append(right_bullet)

def left_bullet_creation():
    left_bullet = pygame.Rect(ship.left, ship.top, 3, 20)
    if len(bullets) < 5:
        bullets.append(left_bullet)

def bullet_remove():
    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)




def bullets_movement():
    for i in bullets:
        basespeed = 15
        i.y -= basespeed

def move_ship_right():
    ship.x += 10
    if ship.right >= settings.SCREEN_WIDTH:
        ship.right = settings.SCREEN_WIDTH

def move_ship_to(posx):
    ship.centerx = posx
    if ship.right >= settings.SCREEN_WIDTH:
        ship.right = settings.SCREEN_WIDTH
    if ship.left <= 0:
        ship.left = 0

def move_ship_left():
    ship.x -= 10
    if ship.left <= 0:
        ship.left = 0


def create_enemy():
    global enemy_ship
    enemy_ship = pygame.Rect(random.randint(0, settings.SCREEN_WIDTH - 101), 5, 101, 110)
    enemy.append(enemy_ship)
    print(len(bullets))

def move_enemy_down():
    global basespeed
    for i in enemy:
        basespeed = 3
        i.y += speedy

def collide_bullet_enemy():
    for i in enemy.copy():
        a = i.collidelist(bullets)
        if a > -1:
            enemy.remove(i)
            del bullets[a]

def model():
    move_enemy_down()
    bullets_movement()
    collide_bullet_enemy()
    bullet_remove()
    print(len(bullets))
