import pygame, sys
from graphics import *
import time
from time import process_time
import random
from threading import Thread
from tkinter import *
from tkinter import  messagebox

alive=True
screen = pygame.display.set_mode()
level=1
bg = pygame.image.load('bg.png')
bg_width = 800
pygame.display.set_caption('Robot Apocalypse')
surfacew = 1054
surfacel = 562
surface = pygame.display.set_mode((surfacew,surfacel))
black = (0, 0, 0)
white = (255,255,255)
prettyblue = (224,255,255)
blue = (0,255,0)
score = 0
list_robots = []
robolist = []
scorelist = []
curr = True

Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Level 1!','Welcome! In order to unlock the door, you must solve each of the puzzles.')

pygame.init()
white = (255, 255, 255)

X = 780
Y = 439
display_surface = pygame.display.set_mode((X, Y ))

pygame.display.set_caption('Try to escape!')

image = pygame.image.load('creepy_door.webp')
bool = True
while bool:
    display_surface.fill(white)
    display_surface.blit(image, (0, 0))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            bool = False
        else:
            pygame.display.update()

Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Level 1!','Level 1 is variables. Variables are used to store different types of values. These values can be integers, rationals (floats), or words (strings).')
messagebox.showinfo('Example', 'Example: x = 5. Print (x). What do you think prints out?')
messagebox.showinfo('Answer', 'If you said 5, you are correct!')
messagebox.showinfo('Quiz!','Now that you know what a variable is, you will have to pass the quiz! x = 35. print (x). What do you think prints out?')

def main():
    screen = pygame.display.set_mode((1052, 562))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False
    score = 0
    while not done:
        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.init()
        pygame.display.flip()
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        print(type(text))
                        if text == '35':
                            done = True
                            messagebox.showinfo('yay!','Good job, you got it correct! :)')
                            messagebox.showinfo('Key','You have received a key to unlock the door!')
                        else:
                            messagebox.showinfo('try again!!','good try, but that is not the correct answer.')
                    if event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                    else:
                        text += event.unicode

if __name__ == '__main__':
    pygame.init()
    main()

pygame.init()

Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Instructions.', 'Each of the red squares are robots. You must shoot them and survive!')

def background():
    surface.fill(black)
    surface.blit(bg, (0,0))

target_img = pygame.image.load('target.png')
target_img = pygame.transform.scale(target_img, (40, 40))
target_rect = target_img.get_rect()

def move_target(target_img, target_rect):
    hi = True
    clock = pygame.time.Clock()
    while hi == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    alive = False
                if event.key == pygame.K_SPACE:
                    print("spacebar")
                    shoot(target_img, target_rect,score)
        keys_pressed = pygame.key.get_pressed()
        surface.blit(bg, (target_rect.x, target_rect.y), target_rect)
        if keys_pressed[pygame.K_LEFT]:
            target_rect.x -= 5
        if keys_pressed[pygame.K_RIGHT]:
            target_rect.x += 5
        if keys_pressed[pygame.K_UP]:
            target_rect.y -= 5
        if keys_pressed[pygame.K_DOWN]:
            target_rect.y += 5
        xrect = surface.blit(target_img, target_rect)
        show_robot()
        pygame.display.update()
        clock.tick(60)
        hi = False

def shoot(target_img, target_rect, score,):
    index = target_rect.collidelist(robolist)
    if index != -1:
        score+=1
        print(target_rect)
        shot = True
        scorelist.append(robolist[index])
        del robolist[index]
        del list_robots[index]
        screen.blit(bg, (0,0))
        screen.blit(target_img, target_rect)
        show_robot()
        pygame.display.flip()

def generate_robot():
    x=random.randint(40,760)
    y=random.randint(40,560)
    robo=(x,y)
    list_robots.append(robo)
    show_robot()
    pygame.display.update(robolist)
    return robo, x, y

def show_robot():
    for q in range(len(list_robots)):
        robocoord=list_robots[q]
        robox, roboy=robocoord
        srobot = pygame.draw.rect(surface, (255,0,0), (robox, roboy,64,64), 0)
        check = False
        for i in robolist:
            if i == srobot:
                check = True
        if check == False:
            robolist.append(srobot)

def die(score, curr):
    print("in die")
    curr = False
    screen.fill(white)
    message("     Your Score: " + str(score)+ "     YOU DIED")
    time.sleep(10)
    pygame.display.update()
    return curr

def win(level, score, curr):
    print("in win")
    curr = False
    level+=1
    screen.fill(white)
    message("     Your Score: " + str(score)+ "     YOU WON!")
    print("before sleep 10")
    time.sleep(5)
    pygame.display.update()
    return curr

def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def message(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((surfacew/2),(surfacel/2))
    surface.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)

def realmain(alive, curr):
    background()
    robot=len(list_robots)
    message("Level "+ str(level))
    while alive==True:
        print(scorelist)
        score = len(scorelist)
        robot=len(robolist)
        beg = process_time()
        myTime = 0
        generate_robot()
        pygame.display.update()
        if robot==2/(level/2):
            curr = die(score, curr)
            alive=False
        if score>=18*(level/2):
            print("win")
            curr = win(level, score, curr)
            alive=False
        looptime = process_time()
        while looptime-beg <5:
            move_target(target_img, target_rect)
            looptime = process_time()
    if curr == False:
        alive = False
        exit()

realmain(alive, curr)
pygame.quit()
quit()
