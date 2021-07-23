import pygame, sys, time, random
from settings import Settings
from snake import Snake
from food import Food
import game_functions as gf

# Initialise game window
pygame.init()
snake_settings=Settings()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((snake_settings.frame_size_x, snake_settings.frame_size_y))
snake=Snake()
food=Food()
food.pos[0]= random.randrange(1, ((snake_settings.frame_size_x - snake_settings.margin)//10)) * 10
food.pos[1]= random.randrange(1, ((snake_settings.frame_size_y -snake_settings.margin)//10)) * 10
food.spawn = True
# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()


# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    gf.check_for_events(snake)
    gf.update_snake(snake,snake_settings,food,game_window)
    gf.create_food(food,snake_settings)
    gf.update_screen(game_window,snake,food,snake_settings)


    

    # To set the speed of the screen
    fps_controller.tick(25)