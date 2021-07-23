import pygame
import random
from time import sleep
import sys
from pygame import mixer

def game_over(game_window, snake_settings):
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    gameover_text = pygame.font.SysFont('Glitch',50).render("GAME OVER",True,(255,255,0))
    gameover_rect= gameover_text.get_rect()
    gameover_rect.centerx = (snake_settings.frame_size_x)/2
    gameover_rect.centery = (snake_settings.frame_size_y)/2
    
    score_text = pygame.font.SysFont('Glitch',40).render("Score :" + str(snake_settings.score),True,(255,255,0))
    score_rect = score_text.get_rect()
    score_rect.centerx = (snake_settings.frame_size_x)/2
    score_rect.centery = (3*(snake_settings.frame_size_y))/4


    game_window.blit(gameover_text,gameover_rect)
    game_window.blit(score_text,score_rect)
    
    mixer.init()
    mixer.music.load("game_over.wav")
    mixer.music.set_volume(0.8)
    mixer.music.play()
    pygame.display.flip()
    sleep(5)
    sys.exit(0)

def show_score(pos, color, font, size,snake_settings,game_window):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    score_text = pygame.font.SysFont(font,size).render("Score :  " + str(snake_settings.score),True,color)
    score_rect=score_text.get_rect()
    score_rect.centerx= pos[0]
    score_rect.centery= pos[1]

    game_window.blit(score_text,score_rect)

def create_food(food,game_settings):
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    if (food.spawn == False):
        food.pos[0]= random.randrange(1, ((game_settings.frame_size_x - game_settings.margin)//10)) * 10
        food.pos[1]= random.randrange(1, ((game_settings.frame_size_y -game_settings.margin)//10)) * 10
    food.spawn = True

def check_for_events(snake):
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                snake.change_to = 'LEFT'
            elif event.key == pygame.K_UP:
                snake.change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                snake.change_to = 'DOWN'
    
    if snake.change_to == 'UP' and snake.direction != 'DOWN':
        snake.direction = 'UP'
    if snake.change_to == 'DOWN' and snake.direction != 'UP':
        snake.direction = 'DOWN'
    if snake.change_to == 'LEFT' and snake.direction != 'RIGHT':
        snake.direction = 'LEFT'
    if snake.change_to == 'RIGHT' and snake.direction != 'LEFT':
        snake.direction = 'RIGHT'


def update_snake(snake,snake_settings,food,game_window):
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    if snake.direction == 'UP':
        snake.pos[1] -= 10
    if snake.direction == 'DOWN':
        snake.pos[1] += 10
    if snake.direction == 'RIGHT':
        snake.pos[0] += 10      
    if snake.direction == 'LEFT':
        snake.pos[0] -= 10

    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    
    snake.body.insert(0,list(snake.pos))
    
    if snake.pos[0] == food.pos[0]  and snake.pos[1] == food.pos[1]:
        snake_settings.score+=20
        food.spawn=False
        mixer.init()
        mixer.music.load("collect.wav")
        mixer.music.set_volume(0.8)
        mixer.music.play()
    else: 
        snake.body.pop()
        


    # End the game if the snake collides with the wall or with itself. 
    if snake.pos[0] <= 0 or snake.pos[0] >= snake_settings.frame_size_x or snake.pos[1] <=0 or snake.pos[1] >= snake_settings.frame_size_y:
        game_over(game_window,snake_settings)  
   
    for i in range(1,len(snake.body)):
        if ((snake.body[i][0] == snake.pos[0]) and (snake.body[i][1] ==snake.pos[1])):
            game_over(game_window,snake_settings)  


def update_screen(game_window,snake,food,snake_settings):
    """
    Draw the snake, food, background, score on the screen
    """
    game_window.fill((0,0,0))
    for bodypart in snake.body:
        bodypart_rect = pygame.Rect(bodypart[0],bodypart[1],10,10)
        pygame.draw.rect(game_window,snake_settings.snake_color,bodypart_rect)

    food_rect = pygame.Rect(food.pos[0],food.pos[1],10,10)
    pygame.draw.rect(game_window,snake_settings.food_color,food_rect)    

    show_score([150,40],(255,255,255),'Comic Sans MS',20,snake_settings,game_window)

    pygame.display.flip()

