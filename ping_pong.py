import pygame

window = pygame.display.set_mode((700, 300))
window.fill((200, 255, 255))

clock = pygame.time.Clock()
FPS = 60

game = True
while game:
    for e in pygame.event.get():
        if e.type == pygame.quit:
            game = False
    pygame.display.update()
    clock.tick(FPS)