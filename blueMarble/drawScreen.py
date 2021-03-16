from time import sleep

import pygame
import sys

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

p1Img = pygame.image.load("images/p1.png")
p2Img = pygame.image.load("images/p2.png")
p3Img = pygame.image.load("images/p3.png")
p4Img = pygame.image.load("images/p4.png")

clock = pygame.time.Clock()
pygame.display.set_caption("Blue Marble")

textAlignLeft = 0
textAlignRight = 1
textAlignCenter = 2
textAlignBlock = 3

pygame.font.init()

font = pygame.font.SysFont("malgungothicsemilight", 15, True, False)


def createButton(img_in, x, y, width, height, img_act, x_act, y_act):
    mPos = pygame.mouse.get_pos()
    if x + width > mPos[0] > x and y + height > mPos[1] > y:
        SCREEN.blit(img_act, (x_act, y_act))
    else:
        SCREEN.blit(img_in, (x, y))


def writeText(s, size, c, x, y):
    f = pygame.font.SysFont("malgungothicsemilight", size, True, False)
    textTitle = f.render(s, True, c)
    textRect = textTitle.get_rect()
    textRect.x = x
    textRect.y = y
    SCREEN.blit(textTitle, textRect)


# 텍스트 줄바꿈
def drawText(text, color, rect, align=textAlignLeft, bkg=None):
    lineSpacing = -2
    spaceWidth, fontHeight = font.size(" ")[0], font.size("Tg")[1]

    listOfWords = text.split(" ")
    if bkg:
        imageList = [font.render(word, 1, color, bkg) for word in listOfWords]
        for image in imageList:
            image.set_colorkey(bkg)
    else:
        imageList = [font.render(word, False, color) for word in listOfWords]

    maxLen = rect[2]
    lineLenList = [0]
    lineList = [[]]
    for image in imageList:
        width = image.get_width()
        lineLen = lineLenList[-1] + len(lineList[-1]) * spaceWidth + width
        if len(lineList[-1]) == 0 or lineLen <= maxLen:
            lineLenList[-1] += width
            lineList[-1].append(image)
        else:
            lineLenList.append(width)
            lineList.append([image])

    lineBottom = rect[1]
    lastLine = 0
    for lineLen, lineImages in zip(lineLenList, lineList):
        lineLeft = rect[0]
        if align == textAlignRight:
            lineLeft += + rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)
        elif align == textAlignCenter:
            lineLeft += (rect[2] - lineLen - spaceWidth * (len(lineImages) - 1)) // 2
        elif align == textAlignBlock and len(lineImages) > 1:
            spaceWidth = (rect[2] - lineLen) // (len(lineImages) - 1)
        if lineBottom + fontHeight > rect[1] + rect[3]:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + i * spaceWidth, lineBottom
            SCREEN.blit(image, (round(x), y))
            lineLeft += image.get_width()
        lineBottom += fontHeight + lineSpacing

    if lastLine < len(lineList):
        drawWords = sum([len(lineList[i]) for i in range(lastLine)])
        remainingText = ""
        for text in listOfWords[drawWords:]:
            remainingText += text + " "
        return remainingText
    return ""


# 플레이어 그리기
def drawPlayer(cp, pl, pColor):
    for i in range(1, cp + 1):
        if i == 1:
            pygame.draw.circle(SCREEN, pColor[i - 1], [650, 80], 20)
            pygame.draw.rect(SCREEN, pColor[i - 1], [650, 80, 300, 80], 1)
            writeText(str(i), 30, BLACK, 640, 60)
            writeText("돈 :", 15, BLACK, 680, 60)
            writeText(str(pl[i - 1]['money']), 15, BLACK, 710, 60)
            writeText("땅 :", 15, BLACK, 680, 80)

            textRect = pygame.Rect(710, 80, 200, 80)
            drawTextRect = textRect.inflate(-5, -5)
            drawText(str(pl[i - 1]['land']), (0, 0, 0), drawTextRect, textAlignBlock)
        else:
            pygame.draw.circle(SCREEN, pColor[i - 1], [650, 130 * i - 50], 20)
            pygame.draw.rect(SCREEN, pColor[i - 1], [650, 130 * i - 50, 300, 80], 1)
            writeText(str(i), 30, BLACK, 640, 130 * i - 70)
            writeText("돈 :", 15, BLACK, 680, 130 * i - 70)
            writeText(str(pl[i - 1]['money']), 15, BLACK, 710, 130 * i - 70)
            writeText("땅 :", 15, BLACK, 680, 130 * i - 50)

            textRect = pygame.Rect(710, 130 * i - 50, 200, 80)
            drawTextRect = textRect.inflate(-5, -5)
            drawText(str(pl[i - 1]['land']), (0, 0, 0), drawTextRect, textAlignBlock)

        pygame.draw.circle(SCREEN, pColor[i - 1], [pl[i - 1]['position'][0] + ((i - 1) * 20), pl[i - 1]['position'][1]], 8)


# 플레이 화면
def drawMap(count, cp, pl):
    pColor = [RED, YELLOW, BLUE, GREEN]
    SCREEN.fill(WHITE)

    count += 1
    writeText("현재 순서: 플레이어 " + str(count % cp + 1), 20, pColor[count % cp], 10, 10)

    # 맵 이미지 출력
    SCREEN.blit(mapImg, (80, 50))

    # 주사위 굴리기 버튼
    createButton(rollImg, 370, 350, 100, 100, clickRollImg, 370, 350)

    drawPlayer(cp, pl, pColor)


# 시작화면
def mainMenu():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 350 < mouse_pos[0] < 650 and 350 < mouse_pos[1] < 480:
                    return

        SCREEN.fill(WHITE)

        # 타이틀 이미지 출력
        SCREEN.blit(titleImg, (160, 100))
        # 시작버튼
        createButton(startImg, 350, 350, 300, 150, clickStartImg, 350, 350)

        pygame.display.update()
        clock.tick(15)


# 플레이어 수 정하기
def countPlayer():
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 200 < mouse_pos[0] < 332 and 300 < mouse_pos[1] < 441:
                    return 2
                elif 400 < mouse_pos[0] < 532 and 300 < mouse_pos[1] < 441:
                    return 3
                elif 600 < mouse_pos[0] < 732 and 300 < mouse_pos[1] < 441:
                    return 4

        SCREEN.fill(WHITE)

        SCREEN.blit(infoImg, (100, 100))
        # 인원 수 버튼
        createButton(twoImg, 200, 300, 132, 141, clickTwoImg, 200, 300)
        createButton(threeImg, 400, 300, 132, 141, clickThreeImg, 400, 300)
        createButton(fourImg, 600, 300, 132, 141, clickFourImg, 600, 300)

        pygame.display.update()
        clock.tick(15)
