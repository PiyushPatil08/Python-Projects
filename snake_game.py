# import pygame
# import time
# import random
#
# pygame.init()
#
# black = (0,0,0)
# white = (255,255,255)
# green = (41,240,26)
# red = (201, 18, 18)
# yellow = (239,250,32)
#
# dis_width = 600
# dis_height = 400
#
# dis = pygame.display.set_mode((dis_width,dis_height))
# pygame.display.set_caption("Snake game")
#
# clock = pygame.time.Clock()
#
# snake_block = 10
# snake_speed = 15
#
# font_style = pygame.font.SysFont("calibri",25)
# score_font = pygame.font.SysFont("comicsans",34)
# # print(pygame.font.get_fonts())
#
# def my_score(score):
#     value = score_font.render("Score: "+str(score),True,yellow)
#     dis.blit(value, [0,0])
#
# def message(msg,color):
#     mssg = font_style.render(msg,True,color)
#     dis.blit(mssg,[0,dis_height/2])
#
#
# def my_snake(snake_block,snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis,green,[x[0],x[1],snake_block,snake_block])
#
#
#
# def main_game():
#     game_over = False
#     game_close = False
#
#     x1 = dis_width/2
#     y1 = dis_height/2
#
#     x1_change = 0
#     y1_change = 0
#
#     snake_list =[]
#     length_snake = 1
#
#     foodx = round(random.randrange(0,dis_width- snake_block)/10.0)*10.0
#     foody = round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
#
#     while not game_over:
#
#         while game_close == True:
#             dis.fill(white)
#             message("You lost! press p to play again q to quit",red)
#             my_score(length_snake - 1)
#             pygame.display.update()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_p:
#                         main_game()
#
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#
#                 elif event.key == pygame.K_UP:
#                     x1_change = 0
#                     y1_change = -snake_block
#
#                 elif event.key == pygame.K_DOWN:
#                     x1_change = 0
#                     y1_change = snake_block
#
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(black)
#
#         pygame.draw.rect(dis,red, [foodx,foody,snake_block,snake_block] )
#         snake_size = []
#         snake_size.append(x1)
#         snake_size.append(y1)
#         snake_list.append(snake_size)
#         if len(snake_list) > length_snake:
#             del snake_list[0]
#
#         my_snake(snake_block,snake_list)
#         my_score(length_snake - 1)
#
#         pygame.display.update()
#
#
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width-snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height-snake_block) / 10.0) * 10.0
#             length_snake +=1
#
#         clock.tick(snake_speed)
#
#     pygame.quit()
#     quit()
#
# main_game()




import pygame
import random
import os

pygame.mixer.init()

pygame.init()


# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))



# Game Title
pygame.display.set_caption("SnakesWithHarry")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    fps = 60
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score +=10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            # gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
