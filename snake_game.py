import pygame
import random as rd
pygame.init()

#  defining colors

green = (0, 128, 0)
grass_green = (102, 141, 60)
brown = (143, 59, 27)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

#  creating game window
screen_width = 850
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game - Mini Project")
pygame.display.update()
font = pygame.font.SysFont(None, 25)
font1 = pygame.font.SysFont(None, 65)
clock = pygame.time.Clock()
image = pygame.image.load("C:\\Users\\ammt5\\OneDrive\\Desktop\\Programming\\professionalSkills4\\snake_bg.jpg")
image1 = pygame.image.load("C:\\Users\\ammt5\\OneDrive\\Desktop\\Programming\\professionalSkills4\\welcome.jpg")
image2 = pygame.image.load("C:\\Users\\ammt5\\OneDrive\\Desktop\\Programming\\professionalSkills4\\gameover.jpg")

def screen_score(text, color, x, y):
    screen_txt = font.render(text, True, color)  # True refers to antialising techniques render displays text on the screen
    gamewindow.blit(screen_txt, [x, y]) # updates game window with screen

def screen_score1(text, color, x, y):
    screen_txt = font1.render(text, True, color)  # True refers to antialising techniques render displays text on the screen
    gamewindow.blit(screen_txt, [x, y])


def plot_window(gamewindow, color, snake_list, snake_radius):
    for snake_x, snake_y in snake_list:
        pygame.draw.circle(gamewindow, brown, [snake_x, snake_y], snake_radius)

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.blit(image1, [0, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True 
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update() 
        clock.tick(30)

def game_loop():

    # creating game specefic variables

    exit_game = False
    game_over = False
    score = 0
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    velocity_increment = 4
    snake_radius = 5
    food_x = rd.randint(0, screen_width/2)
    food_y = rd.randint(0, screen_height/2)
    food_radius = 5
    fps = 30
    snake_list = []
    snake_length = 1
    

    with open("high_score.txt", "r") as f:
        high_score = f.read()

    # creating game loop

    while not exit_game:

        if game_over:

            with open("high_score.txt", "w") as f:
                f.write(str(high_score))
            gamewindow.fill(black)
            gamewindow.blit(image2,[110,80])
            # screen_score1('''GAME OVER !!''', red, screen_width/2, 130)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_loop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x += velocity_increment
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x -= velocity_increment
                        velocity_y = 0
                    
                    if event.key == pygame.K_UP:
                        velocity_y -= velocity_increment
                        velocity_x = 0
                    
                    if event.key == pygame.K_DOWN:
                        velocity_y += velocity_increment
                        velocity_x = 0
            
            snake_x += velocity_x
            snake_y += velocity_y
            if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
                score += 10
                food_x = rd.randint(0, screen_width/2)
                food_y = rd.randint(0, screen_height/2)
                snake_length += 4
            if score > int(high_score):
                high_score = score
            gamewindow.blit(image,[0,0])
            screen_score("Score : "+str(score), white, 30, 10)
            screen_score("High Score : "+str(high_score), white, 700, 10)
            # pygame.draw.rect(gamewindow, green, [snake_x, snake_y, snake_radius, snake_radius])    
            plot_window(gamewindow, black, snake_list, snake_radius) 

            head = []
            head.append(snake_x)   
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            if head in snake_list[: -1]:
                game_over = True

            pygame.draw.circle(gamewindow, red, [food_x, food_y], food_radius)    
        pygame.display.update() 
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()