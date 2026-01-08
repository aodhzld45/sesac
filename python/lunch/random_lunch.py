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
absent_people = []
while True:
    absent_person = input('결석자 입력 \n')

    if absent_person not in names:
        break
    if absent_person in names:
        names.remove(absent_person)
        absent_people.append(absent_person)

print(f'결석자 : {absent_people}')

    
# 섞음.
random.shuffle(names)
names_lengh = len(names)


# n명의 인원으로 조를 짜고 싶다.
# n = 4
n = int(input('몇명 한 조 할까요?'))

# n으로 나눠 떨어지면 그대로 쓴다.
# n으로 나누어 떨이지지 않으면 1을 더한다.
# 나누고 올림한다.

group_count = math.ceil(names_lengh / n)
print(group_count)

# 내가 바라는 data의 형태이다.
# team1 = [a, b, c, d, ]
# team2 = [e, f, g, h]

# teams = [team1, team2, ..., teamn]

# teams = [[] for _ in range(group_count)]
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

for i in range(group_count):
    team = teams[i]

    print(f"{i+1}번 팀 :", *team)