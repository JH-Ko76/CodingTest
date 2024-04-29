decoding = ['A','B','C','D','E','F','G' , 'H' ,'I' ,'J' ,'K', 'L', 'M', 'N' ,'O','P' ,'Q' ,'R' ,'S' ,'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
incoding = []


n = input()

for i in n:
    num = decoding.index(i);
    incoding.append(decoding[num-3])


print(*incoding, sep='');
