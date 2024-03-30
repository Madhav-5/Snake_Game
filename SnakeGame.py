import pygame
import random
import os
pygame.init()
pygame.mixer.init()


white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
green=(0,100,0)

width=400
height=400

wn=pygame.display.set_mode((width,height))
pygame.display.set_caption("GAME")
pygame.display.update()
img=pygame.image.load("snakegame.jpg")
img=pygame.transform.scale(img,(width,height)).convert_alpha()





snake_size=12


clock = pygame.time.Clock()


font=pygame.font.SysFont(None,40)
def screen_score(Text,Color,x,y):
    scr=font.render(Text,True,Color)
    
    wn.blit(scr, [x,y])
def plot_snake(wn,color,snake_list,snake_size):
    for x,y in snake_list:
     pygame.draw.rect(wn,color,[x,y,snake_size,snake_size])
     
     
def gameloop():
    
    fps=30
    exit_game=False
    game_over=False
    snake_x=40
    snake_y=50
    velocity_x=0
    velocity_y=0
    snake_list=[]
    snake_len=1
    food_x=random.randint(10,390)
    food_y=random.randint(10,390)
    score=0
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play()

    if (not os.path.exists("HighScore.txt")):
        with open("HighScore.txt","w") as f:
            f.write("0")

    with open("HighScore.txt","r") as f:
        Highscore=f.read()
    
        
        
        
    

    while not exit_game:
        
        if game_over:
            
            wn.fill(white)
            screen_score("GaMe OvEr!",black,120,150)
            screen_score("press ENTER if continue.",black,40,200)
            for event in pygame.event.get():    
                if event.type==pygame.QUIT:
                   exit_game==True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
            
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game==True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=3
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-3
                        velocity_y=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=3
                        velocity_x=0
                    if event.key==pygame.K_UP:
                        velocity_y=-3
                        velocity_x=0
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
                
                score=score+1
                food_x=random.randint(10,390)
                food_y=random.randint(10,390)
                snake_len+=3
                
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            wn.fill(white)
            wn.blit(img,(0,0))
            if score>int(Highscore):
               with open("HighScore.txt","w") as f:
                  f.write(str(score))
                  pygame.display.update()
        
            screen_score("score : "+str(score)+"   HighScore : "+str(Highscore),red,5,5)
            pygame.draw.rect(wn,red,[food_x,food_y,snake_size,snake_size])
            plot_snake(wn,green,snake_list,snake_size)
            if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                game_over=True
            
            if len(snake_list)>snake_len:
              del snake_list[0]
            if head in snake_list[:-1]:
              game_over=True
            if game_over==True:
               pygame.mixer.music.load("gameover.mp3")
               pygame.mixer.music.play()
            if abs(snake_x-food_x)<7 and abs(snake_y-food_y)<7:
                pygame.mixer.music.load("food.mp3")
                pygame.mixer.music.play()
               

            
        a=pygame.display.update()
        clock.tick(30)
    
    pygame.quit()
    quit()
    
    
gameloop()
