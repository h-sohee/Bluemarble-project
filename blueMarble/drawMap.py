import pygame

SCREEN_SIZE = [1200, 700]

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
BLUE = 0, 100, 255
YELLOW = 230, 230, 0
GREEN = 100, 200, 100
GREEN2 = 255, 0, 255


screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Blue Marble")

pygame.font.init()
myFont = pygame.font.SysFont("경기천년제목", 20, True, False)


def writeText(s, x, y):
    textTitle = myFont.render(s, True, BLACK)
    textRect = textTitle.get_rect()
    textRect.x = x
    textRect.y = y
    screen.blit(textTitle, textRect)


# 플레이어 그리기
def drawPlayer(cp, pl):
    pColor = [RED, YELLOW, BLUE, GREEN]

    for i in range(1, cp+1):
        pygame.draw.circle(screen, pColor[i-1], [800, 120*i], 30)
        pygame.draw.rect(screen, pColor[i-1], [800, 120*i, 300, 80], 3)
        writeText(str(i), 790, 115+((i-1)*120))
        writeText("돈 :", 830, 15+(120*i))
        writeText("땅 :", 830, 45+(120*i))
        writeText(str(pl[i-1].get('money')), 870, 15 + (120 * i))
        writeText(pl[i-1].get('land'), 870, 45+(120*i))

        pygame.draw.circle(screen, pColor[i-1], [pl[i-1].get('position')[0]+(i*20), pl[i-1].get('position')[1]], 8)


def drawMap(cp, pl):
    screen.fill(WHITE)

    drawPlayer(cp, pl)

    # 지도 그리기
    pygame.draw.line(screen, BLACK, [100, 100], [700, 100], 3)
    pygame.draw.line(screen, BLACK, [100, 100], [100, 580], 3)
    pygame.draw.line(screen, BLACK, [100, 580], [700, 580], 3)
    pygame.draw.line(screen, BLACK, [700, 100], [700, 580], 3)

    pygame.draw.line(screen, BLACK, [100, 180], [700, 180], 3)
    pygame.draw.line(screen, BLACK, [200, 100], [200, 580], 3)
    pygame.draw.line(screen, BLACK, [600, 100], [600, 580], 3)
    pygame.draw.line(screen, BLACK, [100, 500], [700, 500], 3)

    pygame.draw.line(screen, BLACK, [100, 260], [200, 260], 3)
    pygame.draw.line(screen, BLACK, [100, 340], [200, 340], 3)
    pygame.draw.line(screen, BLACK, [100, 420], [200, 420], 3)

    pygame.draw.line(screen, BLACK, [600, 260], [700, 260], 3)
    pygame.draw.line(screen, BLACK, [600, 340], [700, 340], 3)
    pygame.draw.line(screen, BLACK, [600, 420], [700, 420], 3)

    pygame.draw.line(screen, BLACK, [300, 100], [300, 180], 3)
    pygame.draw.line(screen, BLACK, [400, 100], [400, 180], 3)
    pygame.draw.line(screen, BLACK, [500, 100], [500, 180], 3)

    pygame.draw.line(screen, BLACK, [300, 500], [300, 580], 3)
    pygame.draw.line(screen, BLACK, [400, 500], [400, 580], 3)
    pygame.draw.line(screen, BLACK, [500, 500], [500, 580], 3)

    # 도시이름
    writeText("사회복지", 110, 110)
    writeText("오타와", 110, 190)
    writeText("베를린", 110, 270)
    writeText("코펜하겐", 110, 350)
    writeText("아테네", 110, 430)
    writeText("무인도", 110, 510)

    writeText("상파울루", 210, 110)
    writeText("이스탄불", 210, 510)
    writeText("시드니", 310, 110)
    writeText("카이로", 310, 510)
    writeText("리스본", 410, 110)
    writeText("싱가포르", 410, 510)
    writeText("마드리드", 510, 110)
    writeText("타이베이", 510, 510)

    writeText("우주여행", 610, 110)
    writeText("런던", 610, 190)
    writeText("뉴욕", 610, 270)
    writeText("접수처", 610, 350)
    writeText("서울", 610, 430)
    writeText("출발", 610, 510)

    # 주사위 굴리기 버튼
    pygame.draw.rect(screen, GREEN2, [330, 410, 140, 60])
    writeText("주사위 굴리기", 350, 430)



