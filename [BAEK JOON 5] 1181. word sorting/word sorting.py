import sys

alpa = []
Set_List = []
re_list = []

n = int(sys.stdin.readline())

for i in range(n):
    alpa.append(sys.stdin.readline().strip());

Set_List = set(alpa)
re_list = list(Set_List)
re_list.sort()
re_list.sort(key = len)


print(*re_list, sep='\n');
