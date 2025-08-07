#初始化
import pygame
import sys

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

#主程式
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # 背景填深灰色
    #pygame.display.flip() 這行不要打，因為要等sixpartline畫完再一次刷新螢幕
    clock.tick(60)

    sixpartline()

pygame.quit()
sys.exit()