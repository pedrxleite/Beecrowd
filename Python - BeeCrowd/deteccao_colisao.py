reta1 = [int(x) for x in input().split()]
reta2 = [int(x) for x in input().split()]

if reta1[2] < reta2[0] or reta2[2] < reta1[0] or reta1[3] < reta2[1] or reta2[3] < reta1[1]:
        print('0')
else:
        print('1')
