N = int(input())
astr, b, cstr = input().split()
a = int(astr)
c = int(cstr)

if b == '+':
    if a + c <= N:
        print('OK')
    else:
        print('OVERFLOW')
elif b == '*':
    if a * c <= N:
        print('OK')
    else:
        print('OVERFLOW')