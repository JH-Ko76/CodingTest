# 과일 주스의 양
A,B,C = map(int, input().split())
# 사용할 양
I,J,K = map(int, input().split())

ratio = min(A/I,B/J, C/K)

format0 = (A - (I * ratio))
format1 = (B - (J * ratio))
format2 = (C - (K * ratio))

print(format0,format1,format2)
