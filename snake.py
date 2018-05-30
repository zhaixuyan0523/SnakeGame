# -*- coding:utf-8 -*-    
__author__ = 'zhai'
__date__ = '2018/5/30 19:05'
import random
import pygame
import sys
from pygame.locals import *

# 方块的颜色
redColor = pygame.Color(255, 0, 0)
# 界面颜色
blackColor = pygame.Color(0, 0, 0)
# 蛇的颜色
whiteColor = pygame.Color(255, 255, 255)


# 游戏结束函数
def gameOver():
    pygame.quit()
    sys.exit()


# 主函数
def main():
    # 初始化 pygame
    pygame.init()
    # 控制游戏速度
    fpsClock = pygame.time.Clock()
    # 创建窗口
    playSurface = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('贪吃蛇')
    # 蛇的初始化位置及长度
    snakePosition = [100, 100]
    snakeBody = [[100, 100], [80, 100], [60, 100]]
    # 初始化目标方块位置
    targetPosiion = [300, 300]
    # 目标方块存活标志
    targetFlag = 1
    # 方向变量
    direction = 'right'
    changeDirection = direction
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirection = 'right'
                if event.key == K_LEFT:
                    changeDirection = 'left'
                if event.key == K_UP:
                    changeDirection = 'up'
                if event.key == K_DOWN:
                    changeDirection = 'down'
                # esc退出
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 确定方向
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # 根据方向移动蛇头的位置
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20

        # 增加蛇的长度
        snakeBody.insert(0, list(snakePosition))
        if snakePosition[0] == targetPosiion[0] and snakePosition[1] ==targetPosiion[1]:
            targetFlag = 0
        else:
            snakeBody.pop()
        if targetFlag == 0:
            # 随机生成目标方块
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            targetPosiion = [int(x*20), int(y*20)]
            targetFlag = 1
        playSurface.fill(blackColor)

        for position in snakeBody:
            # 画蛇
            pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))
            # 画矩形
            pygame.draw.rect(playSurface, redColor, Rect(targetPosiion[0], targetPosiion[1], 20, 20))

        # 更新显示到屏幕页面
        pygame.display.flip()

        # 判断游戏结束
        if snakePosition[0] > 620 or snakePosition[0] < 0:
            gameOver()
        elif snakePosition[1] > 460 or snakePosition[1] <0:
            gameOver()
        fpsClock.tick(5)

if __name__ == '__main__':
    main()