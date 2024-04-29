#반복할 전투 횟수 
n = int(input())
#유닛 정보를 담을 2차원리스트
battle_unit  = []

#2차원 리스트에서 값을 찾기 위한 카운트 값 
dalf_count = 0
ron_count = 1


# n * 2 전투 한번 당 각 진영의 데이터를 한 묶음으로 입력받기 때문에 2를 곱했다.
for i in range (n*2) :
    battle_unit.append(list(map(int, input().split())))

#전투 결과 출력 반복문
for j in range(n):
    dalf_data = 0
    ron_data = 0
	
    #각 진영의 유닛의 능력치를 합산한다.
    dalf_data += (battle_unit[dalf_count][0] * 1 + battle_unit[dalf_count][1] * 2 + battle_unit[dalf_count][2] * 3 +  battle_unit[dalf_count][3] * 3
                 + battle_unit[dalf_count][4] * 4 + battle_unit[dalf_count][5] * 10)

    ron_data += (battle_unit[ron_count][0] * 1 + battle_unit[ron_count][1] * 2 + battle_unit[ron_count][2] * 2 + battle_unit[ron_count][3] * 2 +
                 battle_unit[ron_count][4] * 3 + battle_unit[ron_count][5] * 5 + battle_unit[ron_count][6] * 10)
	
    #묶음으로 받은 데이터에서 1번 진영은 무조건 짝수, 2번진영은 홀 수에 있다 생각해서 각각 +2를 함 
    dalf_count += 2
    ron_count += 2
    
    #출력문에는 j+1을 하여 각 전투가 몇번째인지 출력한다. 
    if (dalf_data > ron_data):
        print('Battle ' + str(j+1) +': Good triumphs over Evil')
    elif (ron_data > dalf_data):
        print('Battle ' + str(j+1) +': Evil eradicates all trace of Good')
    else:
        print('Battle ' + str(j+1) +': No victor on this battle field')
