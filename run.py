import pygame
import random
from ball import ball
from j1 import j1
from j2 import j2

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.pause = False
        self.running = True
        self.j1 = j1(0, 0)
        self.j2 = j2(0, 0)
        self.ball = ball(0, 0)
        self.j1.x = 0
        self.j1.y = 540
        self.j2.x = 1915
        self.j2.y = 540
        self.ball.x = random.randrange(680, 1240, 1)
        self.ball.y = random.randrange(440, 640, 1)
        while self.ball.x == 960:
            self.ball.x = random.randrange(30, 1240, 1)
        if self.ball.x > 960:
            self.ball_x = 1
        else :
            self.ball_x = 2
        self.score_j1 = 0
        self.score_j2 = 0
        self.f = open('./option.txt', "r")
        self.best = int(self.f.read())
        self.f.close()
        self.rotate = 0

    def handling_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys= pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.j1.y += 3
        if keys[pygame.K_z]:
            self.j1.y -= 3
        if keys[pygame.K_UP]:
            self.j2.y -= 3
        if keys[pygame.K_DOWN]:
            self.j2.y += 3
        if keys[pygame.K_SPACE]:
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
        if self.ball_x == 1:
            self.ball.x += 2
        elif self.ball_x == 2:
            self.ball.x -= 2

        if self.ball_y == 1:
            self.ball

        if self.ball.x > 1920 or self.ball.x < 0:
            self.__init__(screen)

        self.color = screen.get_at((self.ball.x, self.ball.y))

        if self.color == (255, 255, 255):
            print(self.color)
            print(self.ball.angle)
            pygame.mixer.music.load('./sound/touch.mp3')
            pygame.mixer.music.play()

    def display(self):
        self.screen.fill("#000000")
        self.create_message('big', 'Score :{}'.format(str(self.score_j1)), (430, 10, 100, 50), (255,255,255))
        self.create_message('big', 'Score :{}'.format(str(self.score_j2)), (1310, 10, 100, 50), (255,255,255))
        self.create_message('big', 'Best score :{}'.format(str(self.best)), (860, 50, 100, 50), (255, 255, 255))
        self.ball.draw(screen)
        self.j1.draw(screen)
        self.j2.draw(screen)
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