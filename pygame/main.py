import pygame, sys, time

pygame.init()

width = 500
height = 500
x = width/2
y = height/2
x_change = 0
y_change = 0

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 50)
game_over = False

def message(msg, color):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [width/2-50, height/2-5])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0
    
    if x >= width or x <= 0 or y >= height or y <= 0:
        game_over = True
    x += x_change
    y += y_change
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (51, 51, 51), [x, y, 10, 10])
    pygame.display.update()
    clock.tick(30)


message("You lost!", (51, 51, 51))
pygame.display.update()
time.sleep(2)
pygame.quit()
sys.exit()