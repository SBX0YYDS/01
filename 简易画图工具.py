
import sys
import pygame
from pygame.locals import *
from pygame.math import Vector2

#初始化
pygame.init()

#常用定义
size = Width,Height = 960,540 #窗口大小960,540
FPS = 60 #帧数
title = "简易画图工具"

screen = pygame.display.set_mode(size,0,32) #显示窗口
pygame.display.set_caption(title) #标题
#图片 = pygame.image.load("").convert_alpha() #图片
clock = pygame.time.Clock()#帧数调整
color = (0,0,0) #设置颜色

try :
    font = pygame.font.Font("GameFonts/simsun.ttc",15)
    fonts = "GameFonts/simsun.ttc"
except pygame.error :
    font = pygame.font.Font(None,15)
    fonts = None


class ZiDraw():
    def __init__(self, fonts = None, size = 15):
        self.font = pygame.font.Font(fonts, size)

    def text(self, text, juchi = False, color = (255,255,255)):
        self.text_surface = font.render(text, juchi, color)
        tx,ty = self.text_surface.get_size()
        self.tx = tx
        self.ty = ty

    def draw(self, pos, screen = screen):
        screen.blit(self.text_surface, pos)

class WinTip1():
    def __init__(self, font_s = None, size = 15):
        self.font = pygame.font.Font(font_s, size)
        if fonts == None:
            self.font = pygame.font.Font(fonts, size)
        self.time = 0
        self.w = 200
        self.h = 60
        self.x = Width - self.w
        self.y = Height - self.h
        self.inp = True

    def text(self, text, mun = 1, color = (255,125,0)):
        draw_x = self.x
        draw_y = self.y - self.h *mun
        self.rect = pygame.rect.Rect((draw_x, draw_y), (self.w, self.h))
        self.text_surface = self.font.render(text, True, color)
        tw, th = self.text_surface.get_size()

        self.tx = draw_x + self.w // 2 - tw // 2
        self.ty = draw_y + self.h // 2 - th // 2

    def draw(self, time = 2, color = (255,125,0)):
        pygame.draw.rect(screen, color, self.rect, 1)
        screen.blit(self.text_surface, (self.tx, self.ty))

        if self.time >= time*FPS:
            self.time = 0
            self.inp = False
            return
        
        self.time += 1

class DrawRect():
    def __init__(self):
        pass



zi_en = ZiDraw(None)
zi_zh = ZiDraw(fonts)
#tip = WinTip1(None,30)
all_tip = []
mun = 0

while True :

    screen.fill(color)
    mouse_down = False
    mx,my = pygame.mouse.get_pos()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONUP :
            if event.button == 1:
                mouse_down = True

    if mouse_down == True:
        mun += 1
        tip = WinTip1(None,30)
        all_tip.append(tip)
        tip.text(f"{mx,my}",mun = mun)
    
    for nums,tips in enumerate(all_tip):
        
        if not tips.inp :
            all_tip.remove(tips)
            mun -= 1
        tips.draw()
        zi_en.text(f"{mun}")
        zi_en.draw((0,0))


    zi_en.text(f"({mx},{my})")
    zi_en.draw((1,Height-zi_en.ty-1))

    pygame.display.update() #刷新
    clock.tick(FPS) #帧数


#keys = pygame.key.get_pressed()
"""

        if mouse_down == True:
            arrow = Arrow(mx, my, 10, "image/pyhave/箭2.png")
            allarrow.append(arrow)
        for arrows in allarrow[:] :
            arrows.run(bing.x_change, bing.y_change)
            if not arrows.inp:
                allarrow.remove(arrows)
            arrows.draw()

            
"""
