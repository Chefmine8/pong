import pygame

class ball:
    def __init__(self, x, y):
        self.image = pygame.image.load("./image/ball.jpg")
        self.angle = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 1
        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.angle, (self.x, self.y))