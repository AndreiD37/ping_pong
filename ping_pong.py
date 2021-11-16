import pygame

window = pygame.display.set_mode((700, 300))


class Gameobject():
    def __init__(self, name):
        self.picture = pygame.image.load(name)
    def draw(self):
        window.blit(self.picture, self.rect)

class Ball(Gameobject):
    def __init__(self, name, speedx, speedy):
        Gameobject.__init__(self, name)
        self.speedx = speedx
        self.speedy = speedy
    def move(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.collide()
    def size(self):
        self.picture = pygame.transform.scale(self.picture, (30, 30))
        self.rect = self.picture.get_rect(center = (350, 150))
    def collide(self):
        if self.rect.bottom >= window.get_rect().bottom:
            self.speedy *= -1
        if self.rect.right >= window.get_rect().right:
            self.rect.center = window.get_rect().center
            self.speedx *= -1
        if self.rect.top <= window.get_rect().top:
            self.speedy *= -1
        if self.rect.left <= window.get_rect().left:
            self.rect.center = window.get_rect().center
            self.speedx *= -1



ball = Ball("ball.png", 2, 2)
ball.size()
clock = pygame.time.Clock()
FPS = 60

game = True
while game:
    window.fill((200, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
    ball.draw()
    ball.move()
    pygame.display.update()
    clock.tick(FPS)