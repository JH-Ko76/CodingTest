#Link https://www.acmicpc.net/problem/2712
data = {'lb' : ['kg',0.4536] , 'kg' : ['lb', 2.2046], 'l' : ['g', 0.2642] , 'g' : ['l',3.7854]}

n = int(input())
output = []
for i in range(n):
    num_data, st = input().split()
    output.append(str(format(float(num_data) * (data[st][1]) , ".4f")) + ' ' + data[st][0])
 
for j in range(n):
    print(output[j])