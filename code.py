import pygame   #importing needed libraries
import time
import random


#initializing all pygame imported modules
pygame.init()   

#initializing colors
blue = (0,0,255)          
red =  (255,0,0)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,102)
green = (0,255,0)

#initializing width and height of the game window
dis_width = 600         
dis_height = 400

#creating the window and naming the window
dis=pygame.display.set_mode(( dis_width, dis_height))
pygame.display.set_caption('Paamb Kali (snake)')

#create clock object to keep track of time
clock = pygame.time.Clock()

#every change happens in multiples of 10
snake_block = 10


#initializing font style
font_style = pygame.font.SysFont("bahnschrift",20)
score_font = pygame.font.SysFont("comicsansms",20)

#functions
#to track score points
def Your_score(score):
    value = score_font.render("Your Score: "+ str(score) + "                                                                                                  ", True, white,black)
    textRect = value.get_rect()
    dis.blit(value,textRect)

#creating snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    pygame.draw.rect(dis, red,[ x[0], x[1], snake_block, snake_block])

#Display message, dimentions and color
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/5, dis_height/2.2])

#main game program
def gameLoop():
    game_over = False    #intializing false which means that user didn't lose nor wants to quit
    game_close = False
     
    x1 = dis_width/2     #start position of snake
    y1 = dis_height/2

    x1_change = 0        #change to add to the position of x y cordinates
    y1_change = 0

    last_key = ""        #to keep track of the last key pressed
    snake_speed = 15     #initializing the frame rate 

    snake_List = []       #initializing empty list which will contain the snake body coordinates
    Length_of_snake = 1   #initializing the length of the snake to be 1

    #the x and y cordinates of the first food, using random fun. will give a random number
    #the snake moves 10 pixels in each iteration, the cordinates of food must be in multiples of 10 to match with the cordinates of snake
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  
    foody = round(random.randrange(30, dis_height - snake_block) / 10.0) * 10.0  
    
    while not game_over: #if the game if not over(user don't want to quit) - gamee_over = False

        while game_close == True:  #if the user lost
            #display a you lost message with the score and ask for user input to play again or quit
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)   
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            
            #Check to see if any events(mouse movement, click, key press, etc) happened
            for event in pygame.event.get():
                #if the event happened is a key press
                if event.type==pygame.KEYDOWN:    
                    if event.key==pygame.K_q:    #if the pressed key is q
                        game_over = True         #setting game_over true which will end the game
                        game_close = False
                    if event.key==pygame.K_c:    #if the pressed key is c
                        gameLoop()               #calling gameloop function which will restart the game
        #checking for events (when game_over and game_close is false) - user didn't lose nor wants to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:      #if the user closes the window by clicking exit button, the game will end (game_over = True)
                game_over = True
            if event.type == pygame.KEYDOWN:   #checking if the event detected is a key press 
                if event.key == pygame.K_LEFT:    #if the key pressed is the left arrow key and the last_key is not right arrow key, the x cordinate will decrease by 10 pixels
                    if last_key != "right":
                        x1_change = -snake_block
                        y1_change = 0
                        last_key = "left"          #setting value of last_key to left
                elif event.key==pygame.K_RIGHT:  #if the key pressed is right arrow key and the last_key is not left arrow key, the x cordinate should increase by 10 pixels
                    if last_key != "left":
                        x1_change = snake_block
                        y1_change = 0
                        last_key = "right"       #last_key is set to right
                elif event.key==pygame.K_UP:     #if the key pressed is up arrow key and the last_key pressed is not the down arrow key, y cordinate is decreased by 10 pixels
                    if last_key != "down":
                        y1_change = -snake_block
                        x1_change = 0
                        last_key = "up"         #last_key is set to up
                elif event.key==pygame.K_DOWN:  #if the key pressed is down arrow key and the last_key is not up, y cordinate is incrreased by 10
                    if last_key != "up":
                        y1_change = snake_block
                        x1_change = 0
                        last_key = "down"       #last_key is set to down

        #If the snake hit boundary on one end, this block will let the snake come out from the opposite end
        if x1 >= dis_width:
            x1 = -10
        elif x1 < -10:
            x1 = dis_width
        elif y1 >= dis_height:
            y1 = 20 
        elif y1 < 20:
            y1 = dis_height 
            
        #changng the cordinates with respect to the key pressed
        x1 += x1_change
        y1 += y1_change

        #background color - yellow
        dis.fill(yellow)

        #creating food in a random cordinate generated(foodx,foody) with 10 pixels height and width and blue color  
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])

        #displaying/rendering the snake with the cordinates updated by the key press    
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        #Create the moving effect by deleting the first element of list as snake cordinates are updated
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #taking the coordinates of the snake body blocks and checking if it is equal to the head coordinates
        #if any of the body coordinates is equal to the head coordinates, it means that the snake hits it's own body which will result in losing the game
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        #updating the values of snake list and snake block
        our_snake(snake_block, snake_List)
        #the score will be (length of snake - 1)
        Your_score(Length_of_snake - 1)
        
        #updating the display with the changes
        pygame.display.update()
        
        #checking if the coordinates of food matches with the any of the body block coordinates, length of snake is increased by 1 and snake speed(frame rate) is increased 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
            foody = round(random.randrange(30, dis_height - snake_block)/10.0)*10.0
            Length_of_snake +=1        
            snake_speed = snake_speed + 1

        #framerate
        clock.tick(snake_speed)




    #deactivates pygame modules (quit)
    pygame.quit()
    quit()
gameLoop()  #calling gameloop function to initially start the game
