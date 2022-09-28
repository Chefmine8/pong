import pygame
import random
from ball import ball

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.pause = False
        self.running = True
        self.ball = ball(0, 0)
        self.ball.x = random.randrange(30, 1240, 30)
        self.ball.y = random.randrange(30, 680, 30)
        self.score = 0
        self.f = open('./option.txt', "r")
        self.best = int(self.f.read())
        self.f.close()

    def handling_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys= pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pass
        if keys[pygame.K_RIGHT]:
            pass
        if keys[pygame.K_UP]:
            pass
        if keys[pygame.K_DOWN]:
            pass
        if keys[pygame.K_SPACE]:
            time.sleep(self.snake.speed)
            self.pause = True
            while self.pause == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.pause = False
                            self.move = 0
                            self.yep = 1
                            self.running = True
                self.screen.fill((0,0,0))

                pygame.display.flip()

    def update(self):
        pass


    def display(self):
        self.screen.fill("#000000")
        self.create_message('big', 'Score :{}'.format(str(self.score)), (10, 10, 100, 50), (255,255,255))
        self.create_message('big', 'Best score :{}'.format(str(self.best)), (10, 50, 100, 50), (255, 255, 255))
        self.ball.draw(screen)
        pygame.display.flip()

    def create_message(self, font, message, message_rectangle, color):
        if font == "small":
            font = pygame.font.SysFont('Lato', 20, False)

        if font == "moyen":
            font = pygame.font.SysFont('Lato', 30, False)

        if font == "big":
            font = pygame.font.SysFont('Lato', 40, True)

        self.message = font.render(message, True, color)

        self.screen.blit(self.message, message_rectangle)

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            #self.create_message()

pygame.init()
screen = pygame.display.set_mode((0, 0))
game = Game(screen)
game.run()

pygame.quit()