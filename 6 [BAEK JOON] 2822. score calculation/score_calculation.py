import sys

score = []
index_data = [];
sum_data = 0;
for i in range(8):
    score.append(int(sys.stdin.readline().strip()))

score_copy = score[:]
score.sort(reverse=True)
for j in range(5):
     index_data.append(1+score_copy.index(score[j]))
     sum_data += score[j]

index_data.sort()
print(sum_data)
print(*index_data)