import random
import time


# 주사위 굴리기
def RollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice = dice1, dice2
    print(dice[0], dice[1])
    return dice


# 플레이어 수 정하기
def count_player():
    while True:
        x = int(input("플레이어 수를 정하세요.(2~4)"))
        while x not in {2, 3, 4}:
            x = int(input("플레이어 수를 정하세요.(2~4)"))
        break
    return x


# print(count_player())
# print(RollDice())
