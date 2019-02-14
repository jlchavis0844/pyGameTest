import pygame

SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE_COLOR = (255,255,255)
BLACK_COLOR = (0,0,0)
RED_COLOR = (255,0,0)
clock = pygame.time.Clock()

class Game:
    TICK_RATE = 60    

    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.game_screen = pygame.display.set_mode((width, height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
        
    def run_game_loop(self):
        is_game_over = False
        while not is_game_over:
    
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    is_game_over = True

            
            pygame.display.update()
            clock.tick(self.TICK_RATE)

class GameObject:
    
    def __init__(self, image_path, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        obj_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(obj_image, (width, height))
        
    def draw(self, background):
        background.blint(self.image, (self.x_pos, self.y_pos))

pygame.init()
new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()
pygame.quit()
quit()

# player_image = pygame.image.load(r'./player.png')
# background_image = pygame.image.load(r'./background.png')
# player_image = pygame.transform.scale(player_image, (50, 50))
# background_image = pygame.transform.scale(background_image, (800,800))
# pygame.draw.rect(game_screen, RED_COLOR, [350,350,100,100])
# pygame.draw.circle(game_screen, BLACK_COLOR, (400,300), 50)
# self.game_screen.blit(background_image,(0,0))
# self.game_screen.blit(player_image,(375,375))