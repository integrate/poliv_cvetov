import pygame, random, time

screen = pygame.display.set_mode([100, 300])


width = random.randint(10, 30)
height = random.randint(10, 100)
x = random.randint(0, screen.get_width()-width)
y = -10
rect1 = pygame.Rect([x,y, width, height])

drop_image = pygame.image.load("images/water_drop.png")

drop_image_2 = pygame.transform.scale(drop_image, rect1.size)

flower1 = pygame.image.load("images/flower1.png")
flower2 = pygame.image.load("images/flower2.png")

flower_height = 100
flower1_changed=pygame.transform.scale(flower1, [screen.get_width()/2, flower_height])
flower2_changed=pygame.transform.scale(flower2, [screen.get_width()/2, flower_height])

grow = 0

while True:
    time.sleep(1/60)

    pygame.event.get()

    rect1.y +=3
    if grow>0:
        width = screen.get_width()
        height = screen.get_height()
        grow-=height

        flower_height+=1
        if flower_height<=height:
            pygame.display.set_mode([width + 1, height])
            flower1_changed = pygame.transform.scale(flower1, [screen.get_width() / 2, flower_height])
            flower2_changed = pygame.transform.scale(flower2, [screen.get_width() / 2, flower_height])

    height = screen.get_height()
    if rect1.bottom>height:
        grow = rect1.width * rect1.height

    if rect1.top>height:
        rect1.width = random.randint(10, 30)
        rect1.height = random.randint(10, 100)

        rect1.bottom =0
        rect1.x = random.randint(0, screen.get_width()-rect1.width)

        drop_image_2 = pygame.transform.scale(drop_image, rect1.size)

        r = random.randint(30, 255)
        g = random.randint(30, 255)
        b = random.randint(30, 255)

    screen.fill([0,0,0])
    # pygame.draw.rect(screen, [r, g, b], rect1)
    screen.blit(flower1_changed, [0, 300-flower1_changed.get_height()])
    screen.blit(flower2_changed, [flower1_changed.get_width(), 300-flower2_changed.get_height()])
    screen.blit(drop_image_2, rect1)
    pygame.display.flip()