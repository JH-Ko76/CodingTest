while True:
    num = input()
    if num == '0':
        break
    while True:
        if(len(str(num)) == 1):
            print(num)
            break
        num = str(sum(map(int, list(num))))