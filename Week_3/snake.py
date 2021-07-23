class Snake():
    def __init__(self):
        #Parameters for Snake
        self.pos = [100, 50]
        self.body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
        self.direction = 'RIGHT'
        self.change_to = self.direction