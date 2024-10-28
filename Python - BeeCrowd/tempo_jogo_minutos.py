hi, mi, hf, mf = map(int, input().split())

if hi == hf and mi == mf:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
elif hi == hf and mi > mf:
    print(f'O JOGO DUROU 23 HORA(S) E {(mf + 60) - mi} MINUTO(S)')
elif hf >= hi and mf >= mi:
    print(f'O JOGO DUROU {hf - hi} HORA(S) E {mf - mi} MINUTO(S)')
elif hf > hi and mf < mi:
    print(f'O JOGO DUROU {(hf - 1) - hi} HORA(S) E {(mf + 60) - mi} MINUTO(S)')
elif hf < hi and mf >= mi:
    print(f'O JOGO DUROU {(hf + (24 - hi))} HORA(S) E {mf - mi} MINUTO(S)')
elif hf < hi and mf < mi:
    print(f'O JOGO DUROU {(hf + (23 - hi))} HORA(S) E {(mf + 60) - mi} MINUTO(S)')
