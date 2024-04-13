score = [];
number = 0;
for i in range (5) :
    b = list(map(int, input().split()))
    score.append(sum(b));
    number = score.index(max(score));

print(number+1,max(score));