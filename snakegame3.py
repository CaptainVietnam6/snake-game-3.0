'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#7932
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: ACTIVE
'''

import pygame
import random

pygame.init() #initialises all imported modules

screen_size_x = 950 #define x-axis screen size in pixels
screen_size_y = 525 #define y-axis screen size in pixels

half_screen_size_x = screen_size_x / 2 #defines HALF of x screen size in pixels
half_screen_size_y = screen_size_y / 2 #defines HALF of y screen size in pixels 

clock = pygame.time.Clock()
dis = pygame.display.set_mode((screen_size_x, screen_size_y)) #sets display size in pixels, keep at 16:9 aspect ratio
pygame.display.update()
pygame.display.set_caption("Snake game made by Kiet P.! :D")

#define colors that will be used in the game
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
pink = (255, 192, 203)
light_red = (204, 0, 0)

#define snake speed and size
snake_size = 25

#define fonts that will be used in the game
font_style = pygame.font.SysFont(None, 25) #this is to define the font that will be used normally for menu and others
score_font = pygame.font.SysFont(None, 50) #this font will be used for the score board
youdied_font = pygame.font.SysFont(None, 70) #this font will be used to display the you died message

def death_message(msg, color): #defines the death message in the death screen
    mesg = youdied_font.render(msg, True, color)
    dis.blit(mesg, [350, 185])

def directory_menu(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [270, 260])

def menu_message(msg, color): #define the upper message in the speed menu
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [380, 200])

def menu_message2(msg, color): #define the lower message in the speed menu
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [350, 240])

def total_score(score): #define the score message in topleft corner
    value = score_font.render("Score: " + str(score), True, green)
    dis.blit(value, [10, 10])

def snake_body(snake_size, snake_list): #body of the snake
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_size, snake_size])

def gameLoop():
    '''
    this function is the first to run when the player starts up the game. gameLoop() has the code to prompt the player to select their speed, while gameLoop2() does not. this will allow the player to only have to select game speed once, unless they chose to go back to the speed menu, which will bring them back to gameLoop()
    '''
    game_over = False
    close_game = False
    inmenu = True #inmenu true at first to make player go into the speed menu as soon as app runs

    x1 = 400
    y1 = 225

    x1_movement_change = 0
    y1_movement_change = 0

    snake_list = []
    snake_length = 1

    '''start of global define function thingys'''#these variables are defined here as global and are defined as False for proper functioning. Will later be defined as true to finally define snake speed.
    global global_snake_speed1
    global global_snake_speed2
    global global_snake_speed3
    global global_snake_speed4
    global global_snake_speed0

    global_snake_speed1 = False
    global_snake_speed2 = False
    global_snake_speed3 = False
    global_snake_speed4 = False
    global_snake_speed0 = False
    '''end of global define function thingies'''

    #randomly generates the x and y coordinates for the food
    spawn_food_x = round(random.randrange(25, screen_size_x - snake_size - 25) / snake_size) * snake_size
    spawn_food_y = round(random.randrange(25, screen_size_y - snake_size - 25) / snake_size) * snake_size

    #while the game is not over, it will run this:
    while game_over != True:
 
        #if the player died, it will bring them to this screen
        #this screen is to ask the plaer to either quit, restart, or go to the speed menu
        while close_game == True:
            dis.fill(orange)
            death_message("You died! :(", red) #message to display when player dies
            directory_menu("Press R to restart, S to change speed, or Q to quit", red)
            pygame.display.update()
 
            for event in pygame.event.get(): #detects button presses to either quit or restart game
                if event.type == pygame.KEYDOWN:
                    #this is to comepletly kill the game
                    if event.key == pygame.K_q: #detects Q presses
                        print("quitting game")
                        game_over = True
                        game_close = False
                    #this is to restart the game
                    if event.key == pygame.K_r: #detects R presses
                        print("restarting game")
                        gameLoop2() #this func is special as it bring the game to the secondary "game" as that one will not prompt the player to select the speed. function is under "def gameLoop2"
                    if event.key == pygame.K_s: #go to speed menu
                        print("going to menu")
                        gameLoop()
            if game_over:
                break

        while inmenu == True:
            dis.fill(orange)
            menu_message("Pick your snake speed!", red)
            menu_message2("1 = Slow, 2 = Normal, 3 = Fast", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print("set snake speed to 1: slow")
                        snake_speed = 5
                        global_snake_speed1 = True
                        inmenu = False
                    if event.key == pygame.K_2:
                        print("set snake speed to 2: normal")
                        snake_speed = 10
                        global_snake_speed2 = True
                        inmenu = False
                    if event.key == pygame.K_3:
                        print("setsnake speed to 3: fast")
                        snake_speed = 15
                        global_snake_speed3 = True
                        inmenu = False
                    if event.key == pygame.K_4:
                        print("setsnake speed to 3: fast")
                        snake_speed = 45
                        global_snake_speed4 = True
                        inmenu = False
                    if event.key == pygame.K_0:
                        global_snake_speed0 = True
                        inmenu = False

            if inmenu == False:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN: #movement controls
                #arrow key movement input
                if event.key == pygame.K_RIGHT: 
                    #when right arrow key is pressed, snake will go right
                    x1_movement_change = snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_LEFT: 
                    #when left arrow key is pressed, snake will go left
                    x1_movement_change = -snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_UP: 
                    #when up arrow key is pressed, snake will go left
                    x1_movement_change = 0
                    y1_movement_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    #when down arrow key is pressed, snake will go down
                    x1_movement_change = 0
                    y1_movement_change = snake_size
                #WASD movement input
                elif event.key == pygame.K_d:
                    #when d is pressed, snake will go right
                    x1_movement_change = snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_a:
                    #when a is pressed, snake will go left
                    x1_movement_change = -snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_w:
                    #when w is pressed, snake will go up
                    x1_movement_change = 0
                    y1_movement_change = -snake_size
                elif event.key == pygame.K_s:
                    #when s is pressed, snake will go down
                    x1_movement_change = 0
                    y1_movement_change = snake_size

        if x1 >= screen_size_x or x1 < 0 or y1 >= screen_size_y or y1 < 0:
            close_game = True #ends game if snake is out of bounds

        x1 += x1_movement_change
        y1 += y1_movement_change

        dis.fill(orange)
        pygame.draw.rect(dis, black, [spawn_food_x, spawn_food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                close_game = True
        
        snake_body(snake_size, snake_list)
        total_score(snake_length - 1)
        pygame.display.update()

        if x1 == spawn_food_x and y1 == spawn_food_y:
            print("ate food")
            spawn_food_x = round(random.randrange(25, screen_size_x - snake_size - 25) / snake_size) * snake_size
            spawn_food_y = round(random.randrange(25, screen_size_y - snake_size - 25) / snake_size) * snake_size
            print(f"score now {snake_length}")
            snake_length += 1

        if global_snake_speed1 == True:
            real_snake_speed = 5
        elif global_snake_speed2 == True:
            real_snake_speed = 10
        elif global_snake_speed3 == True:
            real_snake_speed = 15
        elif global_snake_speed4 == True:
            real_snake_speed = 37.5
        elif global_snake_speed0 == True:
            real_snake_speed = 0
            break

        clock.tick(real_snake_speed)

    pygame.quit()
    quit()

def gameLoop2():
    game_over = False
    close_game = False
    inmenu = True

    x1 = 400
    y1 = 225

    x1_movement_change = 0
    y1_movement_change = 0

    snake_list = []
    snake_length = 1

    #randomly generates the x and y coordinates for the food
    spawn_food_x = round(random.randrange(25, screen_size_x - snake_size - 25) / snake_size) * snake_size
    spawn_food_y = round(random.randrange(25, screen_size_y - snake_size - 25) / snake_size) * snake_size

    #while the game is not over, it will run this:
    while game_over != True:

        #if the player died, it will bring them to this screen
        #this screen is to ask the plaer to either quit, restart, or go to the speed menu
        while close_game == True:
            dis.fill(orange)
            death_message("You died!", red) #message to display when player dies
            directory_menu("Press R to restart, S to change speed, or Q to quit", red)
            pygame.display.update()
 
            for event in pygame.event.get(): #detects button presses to either quit or restart game
                if event.type == pygame.KEYDOWN:
                    #this is to comepletly kill the game
                    if event.key == pygame.K_q: #detects Q presses
                        print("quitting game")
                        game_over = True
                        game_close = False
                    #this is to restart the game
                    if event.key == pygame.K_r: #detects R presses
                        print("restarting game")
                        gameLoop2()
                    if event.key == pygame.K_s: #go to speed menu
                        print("going to menu")
                        gameLoop()
            if game_over:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN: #movement controls
                #arrow key movement input
                if event.key == pygame.K_RIGHT:
                    #when right arrow key is pressed, snake will go right
                    x1_movement_change = snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_LEFT:
                    #when left arrow key is pressed, snake will go left
                    x1_movement_change = -snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_UP:
                    #when up arrow key is pressed, snake will go left
                    x1_movement_change = 0
                    y1_movement_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    #when down arrow key is pressed, snake will go down
                    x1_movement_change = 0
                    y1_movement_change = snake_size
                #WASD movement input
                elif event.key == pygame.K_d:
                    #when d is pressed, snake will go right
                    x1_movement_change = snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_a:
                    #when a is pressed, snake will go left
                    x1_movement_change = -snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_w:
                    #when w is pressed, snake will go up
                    x1_movement_change = 0
                    y1_movement_change = -snake_size
                elif event.key == pygame.K_s:
                    #when s is pressed, snake will go down
                    x1_movement_change = 0
                    y1_movement_change = snake_size

        if x1 >= screen_size_x or x1 < 0 or y1 >= screen_size_y or y1 < 0:
            close_game = True #ends game if snake is out of bounds

        x1 += x1_movement_change
        y1 += y1_movement_change

        dis.fill(orange)
        pygame.draw.rect(dis, black, [spawn_food_x, spawn_food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                close_game = True
        
        snake_body(snake_size, snake_list)
        total_score(snake_length - 1)
        pygame.display.update()

        if x1 == spawn_food_x and y1 == spawn_food_y:
            print("ate food")
            spawn_food_x = round(random.randrange(25, screen_size_x - snake_size - 25) / snake_size) * snake_size
            spawn_food_y = round(random.randrange(25, screen_size_y - snake_size - 25) / snake_size) * snake_size
            print(f"score now {snake_length}")
            snake_length += 1

        if global_snake_speed1 == True:
            real_snake_speed = 5
        elif global_snake_speed2 == True:
            real_snake_speed = 10
        elif global_snake_speed3 == True:
            real_snake_speed = 15
        elif global_snake_speed4 == True:
            real_snake_speed = 37.5
        elif global_snake_speed0 == True:
            real_snake_speed = 0
            break

        clock.tick(real_snake_speed)

    pygame.quit()
    quit()

gameLoop()
