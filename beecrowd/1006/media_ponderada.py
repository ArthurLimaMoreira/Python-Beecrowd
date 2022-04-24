'''
    
    PESOS:
        A   -   PESO 2
        B   -   PESO 3
        C   -   PESO 5
    
'''
PESOA = 2
PESOB = 3
PESOC = 5

A = float(input('\nDigite a nota da prova A: '))
B = float(input('\nDigite a nota da prova B: '))
C = float(input('\nDigite a nota da prova C: '))

media_max = 10
media = (PESOA*A + PESOB*B + PESOC*C)/media_max

print(f'MEDIA = {media:,.2f}')
