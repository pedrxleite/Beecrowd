N = -1
while N < 0 or N > 101:
    N = int(input())
    if 86 <= N <= 100:
        print('A')
    elif 61 <= N <= 85:
        print('B')
    elif 36 <= N <= 60:
        print('C')
    elif 1 <= N <= 35:
        print('D')
    else:
        print('E')
