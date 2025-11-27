import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame

pygame.mixer.music.load("song.mp3") #Eric Matyas
pygame.mixer.music.play(-1)

level = -1
target=""
target2=""
message=""
gemacht=False

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def draw():
    global level, target,target2,message
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Enter the text to encrypt:", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level == 2:
        screen.blit("back", (0, 0))
        screen.draw.text("Enter the amount to rotate (e.g. 3):", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(target2, center=(400, 180), fontsize=24, color=(255, 255, 0))
    elif level == 3:
        screen.blit("back",(0,0))
        screen.draw.text("Text to encrypt:", center=(400, 130), fontsize=24, color=(25, 200, 255))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(255, 255, 0))
        screen.draw.text("Encrypted text:", center=(400, 230), fontsize=24, color=(25, 200, 255))
        screen.draw.text(message, center=(400, 280), fontsize=24, color=(255, 255, 0))        

def on_key_down(key, unicode=None):
    global level, target,target2
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        if level==1:
            target = ""
        if level==2:
            target2=""
    elif key == keys.RETURN and level >0 and level<3:
        level +=1
    elif unicode and key != keys.RETURN and level==1:
        target += unicode
    elif unicode and key != keys.RETURN and level==2:
        target2 += unicode

def update():
    global level,gemacht,message,target,target2
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==3:
        if not gemacht:
            message=caesar_encrypt(target,int(target2))
            gemacht=True
        if keyboard.space:
            level=0
    if level==0:
        target=""
        target2=""
        message=""
        gemacht=False


pgzrun.go()
