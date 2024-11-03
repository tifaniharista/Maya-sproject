import pygame
import sys
import random
import time

print(pygame.version.ver)

# Initialize Pygame
pygame.init()

class GameObject:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self, game_window):
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.position[0], self.position[1], 10, 10))

class Snake(GameObject):
    def __init__(self, position):
        super().__init__(pygame.Color(0, 255, 0), position)
        self.body = [list(position), [position[0] - 10, position[1]], [position[0] - 20, position[1]]]
        self.direction = 'RIGHT'
        self.change_to = self.direction

    def change_direction(self, direction):
        if direction == 'UP' and self.direction != 'DOWN':
            self.change_to = 'UP'
        if direction == 'DOWN' and self.direction != 'UP':
            self.change_to = 'DOWN'
        if direction == 'LEFT' and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def move(self):
        self.direction = self.change_to
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10
        self.body.insert(0, list(self.position))

    def shrink(self):
        self.body.pop()

    def draw(self, game_window):
        for pos in self.body:
            pygame.draw.rect(game_window, self.color, pygame.Rect(pos[0], pos[1], 10, 10))

    def check_collision(self, frame_size_x, frame_size_y):
        if self.position[0] < 0 or self.position[0] > frame_size_x - 10 or self.position[1] < 0 or self.position[1] > frame_size_y - 10:
            return True
        
        for block in self.body[1:]:
            if self.position[0] == block[0] and self.position[1] == block[1]:
                return True
        return False

class Apple(GameObject):
    def __init__(self, frame_size_x, frame_size_y, color):
        position = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]
        super().__init__(color, position)

    def respawn(self, frame_size_x, frame_size_y):
        self.position = [random.randrange(1, (frame_size_x // 10)) * 10, random.randrange(1, (frame_size_y // 10)) * 10]

class Game:
    def __init__(self):
        self.frame_size_x = 720
        self.frame_size_y = 480
        self.game_window = pygame.display.set_mode((self.frame_size_x, self.frame_size_y))
        pygame.display.set_caption('Snake Game')
        self.fps_controller = pygame.time.Clock()
        self.snake = Snake([100, 50])
        self.appleku = Apple(self.frame_size_x, self.frame_size_y, pygame.Color(255, 0, 0))  
        self.applemu = Apple(self.frame_size_x, self.frame_size_y, pygame.Color(0, 0, 255))
        self.score = 0
    
    def game_over(self):
        my_font = pygame.font.SysFont('Times New Roman', 50)
        game_over_surface = my_font.render('HAHAHA GA JAGOO', True, pygame.Color(255, 0, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.frame_size_x / 2, self.frame_size_y / 4)
        self.game_window.fill(pygame.Color(0, 0, 0))
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        sys.exit()

    def show_score(self):
        score_font = pygame.font.SysFont('Arial', 20)
        score_surface = score_font.render('Score : ' + str(self.score), True, pygame.Color(0, 0, 0))
        score_rect = score_surface.get_rect()
        score_rect.midtop = (72, 15)
        self.game_window.blit(score_surface, score_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction('UP')
                    if event.key == pygame.K_DOWN:
                        self.snake.change_direction('DOWN')
                    if event.key == pygame.K_LEFT:
                        self.snake.change_direction('LEFT')
                    if event.key == pygame.K_RIGHT:
                        self.snake.change_direction('RIGHT')
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))
                
            self.snake.move()

            if self.snake.position == self.appleku.position:
                self.score += 1
                self.appleku.respawn(self.frame_size_x, self.frame_size_y)

            elif self.snake.position == self.applemu.position:
                self.score += 1
                self.applemu.respawn(self.frame_size_x, self.frame_size_y)
            else:
                self.snake.shrink()

            self.game_window.fill(pygame.Color(255, 255, 255))

            self.snake.draw(self.game_window)
            self.appleku.draw(self.game_window)
            self.applemu.draw(self.game_window)
            self.show_score()

            if self.snake.check_collision(self.frame_size_x, self.frame_size_y):
                self.game_over()

            pygame.display.update()
            self.fps_controller.tick(10)

# run the game
if __name__ == "__main__":
    game = Game()
    game.run()