a = float(input('Digite o comprimento da reta 1:'))
b = float(input('Digite o comprimento da reta 2:'))
c = float(input('Digite o comprimento da reta 3:'))
if (abs(b - c) < a < (b + c)) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b) and (a == b == c):
    print(f'Há a existência de um triângulo equilátero')
elif (abs(b - c) < a < (b + c)) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b) and ((a == b and b != c) or (a == c and a != b) or (b == c and b != a)):
    print(f'Há a existência de um triângulo isósceles')
elif (abs(b - c) < a < (b + c)) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b) and (a != b) and (a != c) and (b != c):
    print(f'Há a existência de um triângulo escaleno')
else:
    print(f'Não há um triângulo')
#PODERIA APENAS TER FEITO A CONDIÇÃO DE IGUALDADE E DIFERENÇA ENTRE LADOS, O RESTO O ELSE FAZ!!!