import pygame, random, time

screen = pygame.display.set_mode([500, 300])

x = random.randint(0, 500)
y = -10
rect1 = pygame.Rect([x,y, random.randint(10, 30), random.randint(10, 100)])

r = random.randint(30, 255)
g = random.randint(30, 255)
b = random.randint(30, 255)

grow = 0

while True:
    time.sleep(1/60)

    pygame.event.get()

    rect1.y +=3

    height = screen.get_height()
    if rect1.bottom>height:
        r = 255
        g = 0
        b = 0

    if rect1.top>height:
        grow=rect1.width*rect1.height

        rect1.width = random.randint(10, 30)
        rect1.height = random.randint(10, 100)

        rect1.bottom =0
        rect1.x = random.randint(0, screen.get_width()-rect1.width)

        r = random.randint(30, 255)
        g = random.randint(30, 255)
        b = random.randint(30, 255)

    screen.fill([0,0,0])
    pygame.draw.rect(screen, [r, g, b], rect1)
    pygame.display.flip()