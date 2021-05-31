import pygame
import time
import random
pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load("zero.mp3")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green =(0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (53,115,255)
block_color1= (255,0,0)

car_width = 50



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()



carImg = pygame.image.load('bus1.png')
carIcon = pygame.image.load('busicon.png')

pygame.display.set_icon(carIcon)

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Total Points: "+str(count),True,white)
    gameDisplay.blit(text,(0,0))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text,True,white)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    time.sleep(3)
    message_display('You Crashed!')

def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()#button forming
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf,textRect = text_objects(msg,smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf,textRect)


def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect = text_objects("Colspeed",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)

        button("GO!",150,450,100,50,green,bright_green,"play")
        button("Quit",550,450,100,50,red,bright_red,"quit")
        

        pygame.display.update()
        clock.tick(15)

def game_loop():

    pygame.mixer.music.play(5)
    
    
    x = (display_width * 0.5)
    y = (display_height * 0.75)
    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_startx1 = random.randrange(10,display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0


    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -12
                elif event.key == pygame.K_RIGHT:
                    x_change = 12

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            

        x += x_change
        gameDisplay.fill(black)
        for i in range(1):
            things(thing_startx,thing_starty,thing_width,thing_height,block_color)
            thing_starty += thing_speed
            for i in range(1):
                 things(thing_startx1,thing_starty,thing_width,thing_height,block_color1)
                 thing_starty += thing_speed
                 
                
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width-5)
            thing_startx1 = random.randrange(200,600)
        

            
            dodged += 1
            thing_speed += 0.01
           # thing_width += (dodged)

        if y < thing_starty + thing_height:
            
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx+thing_width:
                
                crash()
            if x > thing_startx1 and x < thing_startx1 + thing_width or x+car_width > thing_startx1 and x+car_width < thing_startx1+thing_width:
                
                crash()
                
        pygame.display.update()
        clock.tick(45)
game_intro()        
game_loop()
pygame.quit()
quit()



