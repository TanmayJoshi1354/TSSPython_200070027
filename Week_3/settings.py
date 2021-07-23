import pygame

class Settings():
    def __init__(self):
        #initial game variables

        # Window size
        self.frame_size_x = 720
        self.frame_size_y = 480
        self.margin = 30
        self.snake_color = (0,255,0)
        self.food_color = (240,230,140)
        self.score = 0

