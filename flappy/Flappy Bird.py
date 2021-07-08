import pygame, sys, time, random

#this function draws the floor
def draw_floor():
    screen.blit(floor, (floor_xpos, 550))
    screen.blit(floor, (floor_xpos + 500, 550))

#this function creates the pipes
def create_pipe():
    #choosing random height from pipe_height list
    random_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pos - 200))
    return bottom_pipe, top_pipe 

#this function moves the pipes
def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

#this function draws the pipes
def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

#this function checks if bird collides with pipes, top of the screen or with floor
def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 550:
        return False

    return True

#this function displays the score
def score_display():
    score_surface = font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (250, 100))
    screen.blit(score_surface, score_rect)

pygame.init()
#screen size 500x700
screen = pygame.display.set_mode((500, 700))
clock = pygame.time.Clock()
font = pygame.font.Font("04B_19.ttf", 40)

gravity = 0.25
bird_movement = 0
gameON = True
score = 0
high_score = 0

#background image
bg = pygame.image.load("flappytausta.png").convert()

#floor image
floor = pygame.image.load("floor.png").convert()

#bird image
bird_mid = pygame.image.load("bird_mid.png").convert_alpha()
#make rectangle around bird 
bird_rect = bird_mid.get_rect(center = (100, 350))

#pipe image
pipe_surface = pygame.image.load("pipe.png")
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
#spawn pipe every 1.2 seconds
pygame.time.set_timer(SPAWNPIPE, 1200)
#possible heights for the pipes
pipe_height = [300, 400, 500]

floor_xpos = 0

#game loop
while True:
    for event in pygame.event.get():
        #if user closes the window it actually closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #move the bird with spacebar
            if event.key == pygame.K_SPACE and gameON:
                bird_movement = 0
                bird_movement -= 8
            #if bird collides, start again by pressing spacebar
            if event.key == pygame.K_SPACE and gameON == False:
                gameON = True
                pipe_list.clear()
                bird_rect.center = (100, 350)
                bird_movement = 0
                score = 0
                
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
                
    #draw background
    screen.blit(bg, (0, 0))

    
    if gameON:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        screen.blit(bird_mid, bird_rect)
        gameON = check_collision(pipe_list)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        #plus 1 score every second
        score += 0.01
        score_display()

    #move floor
    floor_xpos -= 5
    draw_floor()
    if floor_xpos <= -500:
        floor_xpos = 0
    
    pygame.display.update()
    clock.tick(120)
    
    
