import pygame
import tkinter

win = tkinter.Tk()
SCREEN_SIZE = [win.winfo_screenwidth()-100, 700]

BLACK = 0, 0, 0
WHITE = 255, 255, 255

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Blue Marble")

pygame.font.init()
myFont = pygame.font.SysFont("경기천년제목", 20, True, False)


def writeCountry(s, x, y):
    text_Title = myFont.render(s, True, BLACK)
    text_Rect = text_Title.get_rect()
    text_Rect.x = x
    text_Rect.y = y
    screen.blit(text_Title, text_Rect)


def drawMap():
    screen.fill(WHITE)

    # 틀 그리기
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
    writeCountry("사회복지", 110, 110)
    writeCountry("오타와", 110, 190)
    writeCountry("베를린", 110, 270)
    writeCountry("코펜하겐", 110, 350)
    writeCountry("아테네", 110, 430)
    writeCountry("무인도", 110, 510)

    writeCountry("상파울루", 210, 110)
    writeCountry("이스탄불", 210, 510)
    writeCountry("시드니", 310, 110)
    writeCountry("카이로", 310, 510)
    writeCountry("리스본", 410, 110)
    writeCountry("싱가포르", 410, 510)
    writeCountry("마드리드", 510, 110)
    writeCountry("타이베이", 510, 510)

    writeCountry("우주여행", 610, 110)
    writeCountry("런던", 610, 190)
    writeCountry("뉴욕", 610, 270)
    writeCountry("접수처", 610, 350)
    writeCountry("서울", 610, 430)
    writeCountry("출발", 610, 510)




