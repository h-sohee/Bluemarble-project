import random
import time

map = {
    '출발': {
        'money': +200000
    },
    '타이베이': {
        'money': +200000
    },
    '황금열쇠': {
        'money': +200000
    },
    '마닐라': {
        'money': +200000
    },
    '제주도': {
        'money': +200000
    },
    '싱가포르': {
        'money': +200000
    },
    '황금열쇠': {
        'money': +200000
    },
    '카이로': {
        'money': +200000
    },
    '이스탄불': {
        'money': +200000
    },
    '무인도': {
        'money': +200000
    },
    '아테네': {
        'money': +200000
    },
    '황금열쇠': {
        'money': +200000
    },
    '코펜하겐': {
        'money': +200000
    },
    '스톡홀름': {
        'money': +200000
    },
    '콩코드여객기': {
        'money': +200000
    },
    '베른': {
        'money': +200000
    },
    '황금열쇠': {
        'money': +200000
    },
    '베를린': {
        'money': +200000
    },
    '오타와': {
        'money': +200000
    },
    '사회복지기금 접수처': {
        'money': +200000
    },
    '부에노스아이레스': {
        'money': +200000
    },
    '황금열쇠': {
        'money': +200000
    },
    '상파울루': {
        'money': +200000
    },
    '시드니': {
        'money': +200000
    },
    '부산': {
        'money': +200000
    },
    '하와이': {
        'money': +200000
    },
    '리스본': {
        'money': +200000
    },
    '퀸엘리자베스호': {
        'money': +200000
    },
    '마드리드': {
        'money': +200000
    },
    '우주여행': {
        'money': +200000
    },
    '도쿄': {
        'money': +200000
    },
    '콜롬비아호': {
        'money': +200000
    },
    '파리': {
        'money': +200000
    },
    '로마': {
        'money': +200000
    },
    '황금열쇠': {
        'money': +200000
    },
    '런던': {
        'money': +200000
    },
    '뉴욕': {
        'money': +200000
    },
    '사회복지기금지불처': {
        'money': +200000
    },
    '서울': {
        'money': +200000
    }
}


# 주사위 굴리기
def RollDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2


# 플레이어 수 정하기
def count_player():
    while True:
        x = int(input("플레이어 수를 정하세요.(2~4)"))
        while x not in {2, 3, 4}:
            x = int(input("플레이어 수를 정하세요.(2~4)"))
        break
    return x


# 게임판 보여주기
def field():
    time.sleep(0.5)
    place = ["start",'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
    price = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    field = []
    for i in range(0,16):
        field.append({'place': place[i], 'price': price[i]})
    return field


game_field = field()
show_field = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

print(count_player())
# print(map)
# print(RollDice())
