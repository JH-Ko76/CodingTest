mushroom = []
score = 0
for i in range(10):
    mushroom.append(int(input()))

for j in mushroom:
    score += j
    if score >= 100:
        if (score-100) <= 100 - (score-j):
            break
        else:
            score-=j
            break
print(score)