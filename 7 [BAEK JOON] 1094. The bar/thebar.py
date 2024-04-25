import sys

//64cm bar를 반으로 자른 값을 저장한 리스트
barlist = [64, 32, 16, 8 , 4 , 2 , 1]
//막대기를 카운트할 변수 
bar_count = 0

x = (int(sys.stdin.readline().strip()))

//반복문으로 가지고있는 막대기의 길이를 하나씩 가져온다.
// x >= i 경우만 count 값을 증가 (x가 23이면 64, 32는 될수가 없기에 제외된다.) 
// 처음 16이 들어가고 x에서 16을 빼면 7이 남기 때문에 8은 버리게 된다. 
// 따라서 총 4개가 된다. 
for i in barlist:
    if(x >= i):
        bar_count+=1
        x -=i
    if( x == 0 ):
        break

print(bar_count)