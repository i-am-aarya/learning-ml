import random
import pygame
from enum import Enum

pygame.init()

# Colors:
RED = (200,0,0)
GREEN = (0,255,0)
DARK_GREEN = (0, 150, 0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)



class Snake :

    class Directions(Enum) :
        UP = [0, -1]
        DOWN = [0, 1]
        LEFT = [-1, 0]
        RIGHT = [1, 0]
    
    def __init__(self, speed=15, screen_width = 1000, screen_height = 600) :

        # Setup pygame
        self.swidth = screen_width
        self.sheight = screen_height
        self.screen = pygame.display.set_mode((self.swidth, self.sheight))
        self.clock = pygame.time.Clock()
        self.game_speed = speed

        # Game details
        self.score = 0
        self.highest_score = 0

        # Snake Details
        self.snake_length = 1
        self.snake_size = 20
        self.snake_speed = self.snake_size
        
        # self.snake_speed = 25
        self.snake_spawn = [self.swidth // 2, self. sheight // 2]   # snake spawn position
        self.snake_pos = self.snake_spawn           # will be used for storing snake position at certain time
        self.snake_body = [self.snake_pos]

        # Snake direction, left by default 
        self.direction = self.Directions.LEFT

        self.snake_color = [DARK_GREEN, GREEN]

        # Food Details
        self.food_pos = [random.randint(0,self.swidth - self.snake_size)//self.snake_size * self.snake_size, random.randint(0,self.sheight - self.snake_size)//self.snake_size * self.snake_size]
        
        self.food_size = self.snake_size
        self.food_color = RED
        
    def draw_snake(self):
        for pos in self.snake_body :
            pygame.draw.rect(self.screen, DARK_GREEN, pygame.Rect(pos[0], pos[1], self.snake_size, self.snake_size))
            pygame.draw.rect(self.screen, GREEN, pygame.Rect(pos[0]+4, pos[1]+4, self.snake_size-8, self.snake_size-8))

    def spawn_food(self) :
        pygame.draw.rect(self.screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], self.snake_size, self.snake_size))

    def get_direction(self, frl) :
        # frl: front, right, left
        # 0 : front
        # 1 : right
        # 2 : left

        if frl == 0 :
            pass
        elif frl == 1 :
            if self.direction == self.Directions.UP :
                self.direction = self.Directions.RIGHT
            elif self.direction == self.Directions.DOWN :
                self.direction = self.Directions.LEFT
            elif self.direction == self.Directions.RIGHT :
                self.direction = self.Directions.DOWN
            else :
            # self.direction = self.Directions.LEFT :
                self.direction = self.Directions.UP

        elif frl == 2 :
            if self.direction == self.Directions.UP :
                self.direction = self.Directions.LEFT
            elif self.direction == self.Directions.DOWN :
                self.direction = self.Directions.RIGHT
            elif self.direction == self.Directions.RIGHT :
                self.direction = self.Directions.UP
            else :
                self.direction = self.Directions.DOWN

        else :
            print("Unknown Direction Given!")
                
    def move_snake(self) :
        if (self.snake_pos[0] >= 0 and self.snake_pos[1] >= 0 and self.snake_pos[0] <= self.swidth - self.snake_size and self.snake_pos[1] <= self.sheight - self.snake_size and self.snake_pos not in self.snake_body[1:]) :
            self.snake_pos[0] += self.snake_speed*self.direction.value[0]
            self.snake_pos[1] += self.snake_speed*self.direction.value[1]
        else :
            print("Game Over! Restarting the game...")
            self.__init__(speed=15, screen_width = 1000, screen_height = 600)

    def check_food_eaten(self) :
        if self.snake_pos == self.food_pos :
            self.snake_length += 1
            self.score += 1
            self.food_pos = [random.randint(0,self.swidth - self.snake_size)//self.snake_size * self.snake_size, random.randint(0,self.sheight - self.snake_size)//self.snake_size * self.snake_size]
        self.spawn_food()
        return True
    
    def update_snake_body(self) :
        self.snake_body.insert(0, [self.snake_pos[0], self.snake_pos[1]])
        if len(self.snake_body) > self.snake_length :
            self.snake_body.pop()

    def game_loop(self) :
        self.screen.fill(BLACK)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()

            """
            if event.type == pygame.KEYDOWN :
                self.direction = self.get_direction()
            """
                    
#         self.get_direction()
        self.move_snake()
        self.check_food_eaten()
        self.update_snake_body()
        self.draw_snake()

        pygame.display.update()
        self.clock.tick(self.game_speed)
