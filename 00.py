#初始化
import pygame
import sys
import random

pygame.init()

screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

#畫六分線和判定線
def sixpartline():
    for p in range(1, 6):
        pygame.draw.line(screen, (255,255,255), (200*p,0), (200*p,600), 1)
    pygame.draw.line(screen, (128,0,0), (0,540), (1200,540), 10)
    pygame.display.flip()

#方塊生成與下落
class Block:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self,screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 199, 20))
    def move(self, speed):
        self.y += speed


#主程式
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # 背景填深灰色
    #pygame.display.flip() 這行不要打，因為要等sixpartline執行完再一次刷新螢幕
    clock.tick(60)

    sixpartline()

pygame.quit()
sys.exit()