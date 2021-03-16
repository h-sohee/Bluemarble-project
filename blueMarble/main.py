import drawScreen
import pygame
import random
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

# 도시 건물가격 설정하기
# 우주여행 이벤트
# 게임 종료 조건 -> 파산/턴 횟수

clock = pygame.time.Clock()
land = ['출발', '타이베이', '싱가포르', '카이로', '이스탄불',
        '무인도', '아테네', '코펜하겐', '베를린', '오타와',
        '사회복지', '상파울루', '시드니', '리스본', '마드리드',
        '우주여행', '런던', '뉴욕', '접수처', '서울']
pPos = [[510, 535], [426, 535], [342, 535], [259, 535], [175, 535],
        [91, 535], [91, 452], [91, 370], [91, 287], [91, 204],
        [91, 122], [175, 122], [259, 122], [342, 122], [426, 122],
        [510, 122], [510, 204], [510, 287], [510, 370], [510, 452]]
# [도시가격, 통행료, 건물비]
landMoney = [0, [100000, 20000, 50000], [100000, 30000, 50000], [100000, 40000, 50000], [100000, 50000, 50000],
             0, [200000, 30000, 50000], [200000, 40000, 50000], [200000, 50000, 50000], [200000, 60000, 50000],
             0, [300000, 40000, 50000], [300000, 50000, 50000], [300000, 60000, 50000], [300000, 70000, 50000],
             0, [400000, 50000, 50000], [400000, 60000, 50000], 0, [400000, 100000, 50000]]


def main():
    pygame.init()
    # drawScreen.mainMenu()
    cp = drawScreen.countPlayer()
    playGame(cp)


# 플레이어 만들기
def makePlayer(cp):
    pList = []

    for x in range(1, cp + 1):
        player = {'position': pPos[0], 'money': 1000000, 'land': [], 'building': {}, 'island': 0, 'space': False, 'live': True}
        pList.append(player)

    return pList


# 주사위 굴리기
def rollDice(playerList, count, cp):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1, dice2)
    
    # 무인도 탈출조건
    if playerList[count % cp]['island'] > 0:
        if dice1 == dice2 or playerList[count % cp]['island'] > 3:
            playerList[count % cp]['island'] = 0
            dice = dice1, dice2
        else:
            dice = 0, 0
    elif playerList[count % cp]['island'] == 0:
        dice = dice1, dice2

    return dice, dice1, dice2


# 플레이어 이동
def movePlayer(dice, count, cp, pList, playerList):
    move = dice[0] + dice[1]
    pList[count % cp] = pList[count % cp] + move

    # 월급
    if pList[count % cp] > 19:
        playerList[count % cp]['money'] += 200000
        pList[count % cp] = pList[count % cp] - 20

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

    return temp[cp-1][1]


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

        # 맵그리기
        drawScreen.drawMap(count, cp, playerList)

        # 턴 횟수 종료
        if count == cp * 10:
            w = checkWinner(cp, playerList)
            msg = '게임이 종료되었습니다. 우승자는 플레이어 ' + str(w + 1) + '입니다.\n게임을 새로 시작하시겠습니까?'
            if messagebox.askyesno('종료', msg):
                main()
            else:
                break

        if diceFlagged:
            dice, dice1, dice2 = rollDice(playerList, count, cp)
            nPos = movePlayer(dice, count, cp, pList, playerList)
            playerList[count % cp]['position'] = pPos[nPos]
            
            check, p = checkLand(cp, playerList, nPos)

            if not check:
                # 무인도
                if land[nPos] == land[5]:
                    m = dice1, dice2
                    msg = str(m) + '가 나왔습니다.\n당신은 무인도에 갖혔습니다.\n' + str(3 - playerList[count % cp]['island']) + '턴이 지나거나 주사위를 던져 같은 수가 나오게 하세요.'
                    messagebox.showinfo('무인도', msg)
                    playerList[count % cp]['island'] += 1
                # 출발 위치
                elif land[nPos] == land[0]:
                    pass
                # 사회복지
                elif land[nPos] == land[10]:
                    msg = str(dice) + '가 나왔습니다.\n당신은 사회복지기금으로 100000원을 지불해야합니다.'
                    messagebox.showinfo('사회복지기금', msg)
                    if playerList[count % cp]['money'] < 100000:
                        msg = '당신은 지불할 돈이 부족합니다.'
                        messagebox.showinfo('사회복지기금-돈 부족', msg)
                        pass
                    else:
                        playerList[count % cp]['money'] -= 100000
                        landMoney[18] += 100000
                # 접수처
                elif land[nPos] == land[18]:
                    msg = str(dice) + '가 나왔습니다.\n당신은 사회복지기금으로 모인 ' + str(landMoney[18]) + '원을 받았습니다.'
                    messagebox.showinfo('접수처', msg)
                    playerList[count % cp]['money'] += landMoney[18]
                    landMoney[18] = 0
                # 우주여행 -> 어떻게 선택???
                elif land[nPos] == land[15]:
                    msg = str(dice) + '가 나왔습니다.\n당신은 다음 턴에 원하는 장소로 이동할 수 있습니다. 어디로 이동하시겠습니까?'
                    messagebox.showinfo('우주여행', msg)
                # 구매
                else:
                    msg = str(dice) + '가 나왔습니다.\n' + str(land[nPos]) + ' 땅은 ' + str(landMoney[nPos][0]) + '원입니다. 땅을 사겠습니까?'
                    if messagebox.askyesno('땅 구매', msg):
                        if playerList[count % cp]['money'] < landMoney[nPos][0]:
                            msg = '당신은 지불할 돈이 부족합니다.'
                            messagebox.showinfo('땅 구매-돈 부족', msg)
                            pass
                        else:
                            playerList[count % cp]['land'].append(land[nPos])
                            playerList[count % cp]['money'] -= landMoney[nPos][0]
            else:
                # 통행료
                if p != (count % cp):
                    # 도시 판매
                    if playerList[count % cp]['money'] < landMoney[nPos][1]:
                        playerList[count % cp]['live'] = False
                        # del playerList[count % cp]['land']

                    msg = str(dice) + ' 가 나왔습니다.\n' + str(land[nPos]) + ' 땅은 플레이어 ' + str(p + 1) + '의 도시입니다. 통행료 ' + str(landMoney[nPos][1]) + '원을 내세요.'
                    messagebox.showinfo('통행료', msg)
                    playerList[count % cp]['money'] -= landMoney[nPos][1]
                    playerList[p]['money'] += landMoney[nPos][1]
                # 건물 생성
                else:
                    print("플레이어 ", p, count % cp)
                    msg = str(dice) + ' 가 나왔습니다.\n' + str(land[nPos]) + ' 땅은 당신의 도시입니다. 건물을 지으시겠습니까?\n건물은 ' + str(landMoney[nPos][2]) + '원입니다.'
                    messagebox.showinfo('건물 생성', msg)
                    playerList[count % cp]['money'] -= landMoney[nPos][2]
            diceFlagged = False

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
