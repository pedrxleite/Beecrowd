c1, c2, c3, c4, c5 = map(int, input().split())
if c1 < c2 and c2 < c3 and c3 < c4 and c4 < c5:
    print('C')
elif c1 > c2 and c2 > c3 and c3 > c4 and c4 > c5:
    print('D')
else:
    print('N')