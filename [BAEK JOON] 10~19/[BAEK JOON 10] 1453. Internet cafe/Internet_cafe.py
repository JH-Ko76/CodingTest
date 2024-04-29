n = int(input())
ct_list = list(map(int, input().split()))
count = 0
values = []

for i in range(n):
    if ct_list[i] in values:
        count += 1
    else:
        values.append(ct_list[i])
print(count)