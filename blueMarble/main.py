import drawMap
import pygame
import random

pygame.init()
land = ['출발', '타이베이', '싱가포르', '카이로', '이스탄불',
        '무인도', '아테네', '코펜하겐', '베를린', '오타와',
        '사회복지', '상파울루', '시드니', '리스본', '마드리드',
        '우주여행', '런던', '뉴욕', '접수처', '서울']
pPos = [[605, 570], [505, 570], [405, 570], [305, 570], [205, 570],
        [105, 570], [105, 490], [105, 410], [105, 330], [105, 250],
        [105, 170], [205, 170], [305, 170], [405, 170], [505, 170],
        [605, 170], [605, 250], [605, 330], [605, 410], [605, 490]]
clock = pygame.time.Clock()


# 플레이어 수 정하기
def countPlayer():
    while True:
        x = int(input("플레이어 수를 정하세요.(2~4)"))
        while x not in {2, 3, 4}:
            x = int(input("플레이어 수를 정하세요.(2~4)"))
        break
    return x


# 플레이어 만들기
def makePlayer(cp):
    pList = []

    for x in range(1, cp + 1):
        player = {'position': pPos[0], 'where': land[0], 'money': 2000000, 'land': "없음", 'alive': 1}
        pList.append(player)
    #
    # print(pList[1], pList[1].get('money'))
    return pList


# 주사위 굴리기
def rollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice = dice1, dice2
    return dice


# 게임 시작
def playGame():
    diceFlag = None
    start = False
    cp = countPlayer()
    count = -1
    pList = []

    playerList = makePlayer(cp)

    for x in range(1, cp + 1):
        nPos = 0
        pList.append(nPos)

    while not start:
        clock.tick(10)

        for event in pygame.event.get():
            # 종료버튼 클릭
            if event.type == pygame.QUIT:
                start = True
            # 주사위 굴리기 버튼 클릭
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if 330 < mouse_pos[0] < 470 and 410 < mouse_pos[1] < 470:
                    diceFlag = True
                    count = count + 1

        # 맵그리기
        drawMap.drawMap(cp, playerList)

        if diceFlag:
            dice = rollDice()
            diceFlag = False
            move = dice[0]+dice[1]
            pList[count % cp] = pList[count % cp] + move

            if pList[count % cp] > 19:
                pList[count % cp] = pList[count % cp] - 20

            playerList[count % cp]['position'] = pPos[pList[count % cp]]

        pygame.display.flip()

    pygame.quit()


playGame()


