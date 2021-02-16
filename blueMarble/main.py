import drawMap
import pygame
import random

pygame.init()

start = False
clock = pygame.time.Clock()

while not start:
    clock.tick(10)

    for event in pygame.event.get():
        # 종료버튼
        if event.type == pygame.QUIT:
            start = True

        # 맵그리기
        drawMap.drawMap()

    pygame.display.flip()

pygame.quit()


# 주사위 굴리기
def rollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice = dice1, dice2
    return dice


# 플레이어 수 정하기
def countPlayer():
    while True:
        x = int(input("플레이어 수를 정하세요.(2~4)"))
        while x not in {2, 3, 4}:
            x = int(input("플레이어 수를 정하세요.(2~4)"))
        break
    return x


# 플레이어 만들기
def makePlayer(p):
    p = {'before_where': 0, 'where': 0, 'money': 2000000, 'alive': 1}
    return p


player_list = []
cp = countPlayer()
for x in range(1, cp + 1):
    player = set()
    player_list.append(makePlayer(player))

print(player_list)

# print(RollDice()[0], RollDice()[1])
# print(count_player())
# print(RollDice())


