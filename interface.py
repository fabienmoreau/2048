import pygame 

grey = (200,200,200)
width = 1000
edge = 250

class InterfacePy:

    def __init__(self):
        self.screen = pygame.display.set_mode((width, width))
        self.create_grid()


    def create_grid(self):
        self.rect_background = pygame.Rect((0,0),(width, width))
        self.image_background= pygame.image.load("images/background.jpg")


    def refresh(self, game):

        self.screen.blit(self.image_background, self.rect_background)
        for i in range(len(game.grid)):
            for j in range(len(game.grid)):
                if game.grid[i][j] != 0:
                    rect = pygame.Rect((j*edge,i*edge), ((j+1)*edge, (i+1)*edge))
                    image = pygame.image.load(f"images/"+str(int(game.grid[i][j]))+".jpg")
                    self.screen.blit(image, rect)
        pygame.display.update()  



    def change_direction(self, event, game):
        if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

            if event.key == pygame.K_DOWN and game.direction != 'UP':
                game.direction = 'DOWN'
            elif event.key == pygame.K_UP and game.direction != 'DOWN':
                game.direction = 'UP'
            elif event.key == pygame.K_LEFT and game.direction != 'RIGHT':
                game.direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and game.direction != 'LEFT':
                game.direction = 'RIGHT'
