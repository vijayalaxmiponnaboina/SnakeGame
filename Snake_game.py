import pygame
import random
pygame.init()
width,height=600,600
gamescreen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")
snake_x,snake_y=width//2,height//2
change_x,change_y=0 , 0

food_x,food_y=random.randrange(0,width)//15*15,random.randrange(0,height)//15*15
clock=pygame.time.Clock()

snake_body=[(snake_x,snake_y)]
def display_snake_and_food():
    global snake_x,snake_y,food_x,food_y

    snake_x=(snake_x+change_x) % width
    snake_y=(snake_y+change_y) % height

    if((snake_x,snake_y) in snake_body[1:]):
        print("GAME OVER!!!!")
        quit()
    snake_body.append((snake_x,snake_y))

    if(food_x == snake_x and food_y == snake_y):
        food_x = random.randrange(0, width // 15) * 15
        food_y = random.randrange(0, height // 15) * 15
    else:
        del snake_body[0]
    gamescreen.fill((0,0,0))
    pygame.draw.rect(gamescreen,(0,255,0),[food_x,food_y,15,15])
    for (x,y) in snake_body:
        pygame.draw.rect(gamescreen,(255,255,255),[x,y,15,15])
    pygame.display.update()
while True:
    events=pygame.event.get()
    for event in events:
        if(event.type==pygame.QUIT):
            pygame.quit()
            quit()
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                change_x=-15
                change_y=0
            elif(event.key==pygame.K_RIGHT):
                change_x=15
                change_y=0
            elif(event.key==pygame.K_UP):
                change_x=0
                change_y=-15
            elif(event.key==pygame.K_DOWN):
                change_x=0
                change_y=15
    display_snake_and_food()
    clock.tick(10)