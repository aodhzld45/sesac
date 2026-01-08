import math
import random
from pprint import pprint

names = [
    "손오공", "베지터", "손오반", "피콜로", "크리링",
    "야무치", "천진반", "차오즈", "부르마", "트랭크스",
    "손오천", "치치", "비델", "미스터 사탄", "마인 부우",
    "프리저", "셀", "기뉴", "자봉", "도도리아",
]


# 결석 로직
def remove_absent_person(names):
    absent_people = []
    while True:
        absent_person = input('결석자 입력 \n')

        if absent_person not in names:
            break
        if absent_person in names:
            names.remove(absent_person)
            absent_people.append(absent_person)

    print(f'결석자 : {absent_people}')

    return names

def get_group_count():
    n = int(input('몇명 한 조 할까요?'))
    group_count = math.ceil(names_lengh / n)
    return group_count






def get_random_team():
    teams = []
    for _ in range(group_count):
        teams.append([]) # team에 대한 그릇.

    # print(names)
    # print(teams)

    for i in range(names_lengh):
        name = names[i]

        team_index = i % group_count
        team = teams[team_index]

        team.append(name)
    return teams





def print_teams(teams):
    for i in range(group_count):
        team = teams[i]

        print(f"{i+1}번 팀 :", *team)

# 결석자 제외
names = remove_absent_person(names)

names_lengh = len(names)
# 랜덤으로 섞어
random.shuffle(names)

# 조 개수 찾아
group_count = get_group_count()

# 조 만들어
teams = get_random_team()

print_teams(teams)
