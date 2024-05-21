arr = []
test = []
count = 0
index = 0
for i in range(9):
	arr.append(list(map(int, input().split())))

for j in arr:
    test.append(max(j))

for k in arr:
    count += 1
    if(max(k) == max(test)):
       index += k.index(max(test))
       print(max(test))
       print(count, index + 1)
       break