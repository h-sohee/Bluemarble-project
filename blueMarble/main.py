import drawScreen
import pygame
import random
from tkinter import *
from tkinter import messagebox

clock = pygame.time.Clock()

# 도시이름
land = ['출발', '타이베이', '싱가포르', '카이로', '이스탄불',
        '무인도', '아테네', '코펜하겐', '황금카드', '오타와',
        '사회복지', '상파울루', '시드니', '리스본', '마드리드',
        '우주여행', '런던', '뉴욕', '접수처', '서울']
# 도시별 좌표
pPos = [[517, 545], [432, 545], [347, 545], [262, 545], [177, 545],
        [92, 545], [92, 460], [92, 375], [92, 290], [92, 205],
        [92, 120], [177, 120], [262, 120], [347, 120], [432, 120],
        [517, 120], [517, 205], [517, 290], [517, 375], [517, 460]]
# [도시가격, 통행료, 건물가격, 건물개수]
landMoney = [0, [50000, 20000, 10000, 0], [80000, 40000, 20000, 0], [100000, 60000, 30000, 0], [120000, 80000, 40000, 0],
             0, [140000, 100000, 50000, 0], [160000, 120000, 60000, 0], 0, [200000, 160000, 80000, 0],
             0, [220000, 180000, 90000, 0], [240000, 220000, 110000, 0], [260000, 220000, 110000, 0], [280000, 240000, 120000, 0],
             0, [300000, 260000, 130000, 0], [320000, 280000, 150000, 0], 0, [350000, 350000, 170000, 0]]
# 황금카드
goldCard = ["병원비 지불: 병원에서 건강진단을 받았습니다. 병원비 10000원을 납부합니다.",
            "복권당첨: 복권에 당첨되었습니다. 당첨금 200000원을 받습니다.",
            "이사: 뒤로 두칸 이동하세요.",
            "고속도로: 출발지까지 이동해서 월급을 받습니다.",
            "생일 축하: 모두에게 생일축하를 받으세요. 전원에게 축하금 10000원씩 받습니다."]


def main():
    pygame.init()
    drawScreen.mainMenu()
    cp = drawScreen.countPlayer()
    playGame(cp)


# 플레이어 만들기
def makePlayer(cp):
    pList = []

    for x in range(1, cp + 1):
        player = {'position': pPos[0], 'money': 1000000, 'land': [], 'event': 0, 'space': 15, 'live': True}
        pList.append(player)

    return pList


# 주사위 굴리기
def rollDice(playerList, count, cp):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    move = 0

    # 무인도 탈출조건
    if 0 < playerList[count % cp]['event'] < 5:
        if dice1 == dice2 or playerList[count % cp]['event'] == 4:
            playerList[count % cp]['event'] = 0
            move = dice1 + dice2
        else:
            move = 0
    # 우주여행
    elif playerList[count % cp]['event'] == 5:
        move = 0
    elif playerList[count % cp]['event'] == 6:
        choice = playerList[count % cp]['space']

        if choice - 15 < 0:
            move = 20 + choice - 15
        else:
            move = choice - 15

        playerList[count % cp]['event'] = 0
    elif playerList[count % cp]['event'] == 0:
        move = dice1 + dice2

    return move, dice1, dice2


# 플레이어 이동
def movePlayer(move, count, cp, pList, playerList):
    pList[count % cp] = pList[count % cp] + move

    # 월급
    if pList[count % cp] > 19:
        playerList[count % cp]['money'] += 200000
        pList[count % cp] = pList[count % cp] - 20

    print(count % cp, move, land[pList[count % cp]])
    return pList[count % cp]


# 주인 있는 땅인지 확인
def checkLand(cp, playerList, nPos):
    check = False

    for i in range(0, cp):
        x = len(playerList[i]['land'])
        for j in range(0, x):
            if playerList[i]['land'][j] == land[nPos]:
                check = True
                return check, i

    return check, i


# 우승자 확인
def checkWinner(cp, playerList):
    temp = []

    for i in range(0, cp):
        temp.append((playerList[i]['money'], i))

    temp.sort()
    print(temp)

    return temp[cp - 1][1]


# 게임 시작
def playGame(cp):
    Tk().wm_withdraw()
    diceFlagged = None
    count = -1
    pList = []

    playerList = makePlayer(cp)

    for x in range(0, cp):
        nPos = 0
        pList.append(nPos)

    while playerList[count % cp]['live']:
        clock.tick(10)

        for event in pygame.event.get():
            # 종료버튼 클릭
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            # 주사위 굴리기 버튼 클릭
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 370 < mouse_pos[0] < 470 and 350 < mouse_pos[1] < 450:
                    diceFlagged = True
                    count = count + 1

        msg = ""
        if playerList[count % cp]['event'] == 5:
            playerList[count % cp]['event'] = 6

        # 맵그리기
        drawScreen.drawMap(count, cp, playerList)

        # 턴 횟수 종료
        if count == cp * 20:
            w = checkWinner(cp, playerList)
            msg = '게임이 종료되었습니다. 우승자는 플레이어 ' + str(w + 1) + '입니다. 게임을 새로 시작하시겠습니까?'
            choose = drawScreen.ynMessageShow(msg, count, cp, playerList)
            if choose:
                main()
            else:
                break

        if diceFlagged:
            if playerList[count % cp]['event'] == 5:
                playerList[count % cp]['event'] += 1

            move, dice1, dice2 = rollDice(playerList, count, cp)
            nPos = movePlayer(move, count, cp, pList, playerList)
            playerList[count % cp]['position'] = pPos[nPos]

            check, p = checkLand(cp, playerList, nPos)

            # 주인 없는 땅에 도착
            if not check:
                d = dice1, dice2
                # 무인도
                if land[nPos] == land[5]:
                    msg = str(d) + '가 나왔습니다.당신은 무인도에 갖혔습니다.' + str(
                        3 - playerList[count % cp]['event']) + '턴이 지나거나 주사위를 던져 같은 수가 나오게 하세요.'
                    drawScreen.yMessageShow(msg, count, cp, playerList)
                    playerList[count % cp]['event'] += 1
                # 출발 위치
                elif land[nPos] == land[0]:
                    pass
                # 사회복지
                elif land[nPos] == land[10]:
                    msg = str(d) + '가 나왔습니다.당신은 사회복지기금으로 100000원을 지불해야합니다.'
                    drawScreen.yMessageShow(msg, count, cp, playerList)
                    if playerList[count % cp]['money'] < 100000:
                        msg = '당신은 지불할 돈이 부족합니다.'
                        messagebox.showinfo('사회복지기금-돈 부족', msg)
                    else:
                        playerList[count % cp]['money'] -= 100000
                        landMoney[18] += 100000
                # 접수처
                elif land[nPos] == land[18]:
                    msg = str(d) + '가 나왔습니다.당신은 사회복지기금으로 모인 ' + str(landMoney[18]) + '원을 받았습니다.'
                    drawScreen.yMessageShow(msg, count, cp, playerList)
                    playerList[count % cp]['money'] += landMoney[18]
                    landMoney[18] = 0
                # 우주여행
                elif land[nPos] == land[15]:
                    space = drawScreen.cityClicked(count, cp, playerList)
                    playerList[count % cp]['space'] = space
                    playerList[count % cp]['event'] = 5
                # 황금카드
                elif land[nPos] == land[8]:
                    card = random.randint(0, 4)
                    msg = str(d) + '가 나왔습니다.' + goldCard[card]
                    choose = drawScreen.yMessageShow(msg, count, cp, playerList)
                    if choose:
                        if card == 0:
                            playerList[count % cp]['money'] -= 10000
                        elif card == 1:
                            playerList[count % cp]['money'] += 200000
                        elif card == 2:
                            nPos = movePlayer(-2, count, cp, pList, playerList)
                            playerList[count % cp]['position'] = pPos[nPos]
                        elif card == 3:
                            nPos = movePlayer(12, count, cp, pList, playerList)
                            playerList[count % cp]['position'] = pPos[nPos]
                        elif card == 4:
                            for i in range(len(playerList)):
                                if i == count % cp:
                                    playerList[i]['money'] += 10000 * (len(playerList) - 1)
                                else:
                                    playerList[i]['money'] -= 10000

                # 구매
                else:
                    msg = str(d) + '가 나왔습니다.' + str(land[nPos]) + ' 땅은 ' + str(
                        landMoney[nPos][0]) + '원입니다. 땅을 사겠습니까?'
                    choose = drawScreen.yMessageShow(msg, count, cp, playerList)
                    if choose:
                        if playerList[count % cp]['money'] < landMoney[nPos][0]:
                            msg = '당신은 지불할 돈이 부족합니다. 땅을 구매할 수 없습니다.'
                            drawScreen.yMessageShow(msg, count, cp, playerList)
                        else:
                            playerList[count % cp]['land'].append(land[nPos])
                            playerList[count % cp]['money'] -= landMoney[nPos][0]
            # 주인 있는 땅에 도착
            else:
                # 다른 플레이어 도시에 도착 - 통행료
                if p != (count % cp):
                    msg = str(d) + ' 가 나왔습니다.' + str(land[nPos]) + ' 땅은 플레이어 ' + str(p + 1) + '의 도시입니다. 통행료 ' + str(landMoney[nPos][1]) + '원을 내세요.'
                    drawScreen.yMessageShow(msg, count, cp, playerList)
                    # 돈 부족
                    if playerList[count % cp]['money'] < landMoney[nPos][1]:
                        msg = '돈이 부족합니다. 소유한 땅을 판매하세요.'
                        drawScreen.yMessageShow(msg, count, cp, playerList)
                        # 도시 판매 불가 - 파산
                        if len(playerList[count % cp]['land']) == 0:
                            msg = '판매할 땅이 없습니다. 파산입니다.'
                            drawScreen.yMessageShow(msg, count, cp, playerList)
                            playerList[count % cp]['live'] = False
                        # 도시 판매
                        else:
                            msg = playerList[count % cp]['land'][0] + '땅을 판매합니다. (제일 먼저 구매한 땅)'
                            drawScreen.yMessageShow(msg, count, cp, playerList)

                            for i in range(len(land)):
                                if land[i] == playerList[count % cp]['land'][0]:
                                    playerList[count % cp]['money'] += int(
                                        (landMoney[i][0] + landMoney[i][2] * landMoney[i][3]) / 2)
                                    if playerList[count % cp]['money'] >= landMoney[nPos][1]:
                                        break

                            del playerList[count % cp]['land'][0]
                            playerList[p]['money'] += landMoney[nPos][1]
                    else:
                        playerList[count % cp]['money'] -= landMoney[nPos][1]
                        playerList[p]['money'] += landMoney[nPos][1]
                # 본인 땅에 도착 - 건물 생성
                else:
                    msg = str(d) + ' 가 나왔습니다.' + str(land[nPos]) + ' 땅은 당신의 도시입니다. 건물을 지으시겠습니까? 건물생성 비용은 ' + str(
                        landMoney[nPos][2]) + '원입니다.'
                    choose = drawScreen.ynMessageShow(msg, count, cp, playerList)
                    if choose:
                        if playerList[count % cp]['money'] < landMoney[nPos][0]:
                            msg = '당신은 지불할 돈이 부족합니다. 건물을 생성할 수 없습니다.'
                            drawScreen.yMessageShow(msg, count, cp, playerList)
                        else:
                            msg = "건물을 지었습니다. 도시의 통행료가 증가했습니다."
                            drawScreen.yMessageShow(msg, count, cp, playerList)
                            playerList[count % cp]['money'] -= landMoney[nPos][2]
                            landMoney[nPos][3] += 1
                            landMoney[nPos][1] += landMoney[nPos][2] * landMoney[nPos][3]
            diceFlagged = False

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
