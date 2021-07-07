import pygame, sys, time, random

def draw_floor():
    screen.blit(floor, (floor_xpos, 550))
    screen.blit(floor, (floor_xpos + 500, 550))

def create_pipe():
    random_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pos - 200))
    return bottom_pipe, top_pipe 

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 550:
        return False

    return True
        

pygame.init()
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0
gameON = True


bg = pygame.image.load("flappytausta.png").convert()

floor = pygame.image.load("floor.png").convert()

bird_mid = pygame.image.load("bird_mid.png").convert()
bird_rect = bird_mid.get_rect(center = (100, 350))

pipe_surface = pygame.image.load("pipe.png")
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [300, 400, 500]

floor_xpos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameON:
                bird_movement = 0
                bird_movement -= 8
            if event.key == pygame.K_SPACE and gameON == False:
                gameON = True
                pipe_list.clear()
                bird_rect.center = (100, 350)
                bird_movement = 0
                
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
                

    screen.blit(bg, (0, 0))

    if gameON:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_mid, bird_rect)
        gameON = check_collision(pipe_list)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    
    floor_xpos -= 1
    draw_floor()
    if floor_xpos <= -500:
        floor_xpos = 0
    
    pygame.display.update()
    clock.tick(120)
    
    
