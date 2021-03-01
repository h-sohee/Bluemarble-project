import pygame
import time
import sys

pygame.init()

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
BLUE = 0, 100, 255
YELLOW = 230, 230, 0
GREEN = 100, 200, 100
GRAY = 200, 200, 200

titleImg = pygame.image.load("images/title.png")
startImg = pygame.image.load("images/start.png")
clickStartImg = pygame.image.load("images/clickedStart.png")

infoImg = pygame.image.load("images/info.png")
twoImg = pygame.image.load("images/two.png")
clickTwoImg = pygame.image.load("images/clickedTwo.png")
threeImg = pygame.image.load("images/three.png")
clickThreeImg = pygame.image.load("images/clickedThree.png")
fourImg = pygame.image.load("images/four.png")
clickFourImg = pygame.image.load("images/clickedFour.png")

mapImg = pygame.image.load("images/map.png")
rollImg = pygame.image.load("images/roll.png")
clickRollImg = pygame.image.load("images/clickedRoll.png")
quitImg = pygame.image.load("images/quit.png")
clickQuitImg = pygame.image.load("images/clickedQuit.png")

p1Img = pygame.image.load("images/p1.png")
p2Img = pygame.image.load("images/p2.png")
p3Img = pygame.image.load("images/p3.png")
p4Img = pygame.image.load("images/p4.png")


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blue Marble Game")

clock = pygame.time.Clock()


def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    # pygame 초기화
    pygame.init()
    FPSCLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.display.set_caption('창고 관리')
    BASICFONT = pygame.font.SysFont('malgungothic', 50)     # 한글 폰트

    mainMenu()  # 시작 화면 생성

    # while True: # 메인 게임 루프
    #     playerMenu()


class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mPos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mPos[0] > x and y + height > mPos[1] > y:
            SCREEN.blit(img_act, (x_act, y_act))
            if click[0] and action is not None:
                time.sleep(0.5)
                action()
        else:
            SCREEN.blit(img_in, (x, y))


def quitGame():
    pygame.quit()
    sys.exit()


def playGame():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)

        mapDraw = SCREEN.blit(mapImg, (80, 50))
        rollButton = Button(rollImg, 370, 350, 100, 100, clickRollImg, 370, 350, quitGame)
        p1 = SCREEN.blit(p1Img, (600, 50))
        p2 = SCREEN.blit(p2Img, (600, 170))
        p3 = SCREEN.blit(p3Img, (600, 290))
        p4 = SCREEN.blit(p4Img, (600, 410))
        pygame.display.update()
        clock.tick(15)


def playerMenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)

        infoText = SCREEN.blit(infoImg, (100, 100))
        twoButton = Button(twoImg, 200, 300, 132, 141, clickTwoImg, 200, 300, playGame)
        threeButton = Button(threeImg, 400, 300, 132, 141, clickThreeImg, 400, 300, playGame)
        fourButton = Button(fourImg, 600, 300, 132, 141, clickFourImg, 600, 300, playGame)
        pygame.display.update()
        clock.tick(15)


def mainMenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill(WHITE)

        titleText = SCREEN.blit(titleImg, (160, 100))
        startButton = Button(startImg, 350, 300, 300, 130, clickStartImg, 350, 300, playerMenu)
        pygame.display.update()
        clock.tick(15)


if __name__ == '__main__':
    main()


