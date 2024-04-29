import sys


n = list(map(int, sys.stdin.readline().split()))

sumdata = 0
sequence = []
sequence.append(0)

for i in range(1000):
    for j in range(i):
        sequence.append(i)


for k in range(n[0], n[1]+1):
    sumdata = sequence[k] + sumdata


print(sumdata)
