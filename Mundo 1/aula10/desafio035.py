a = float(input('Digite o comprimento da reta 1:'))
b = float(input('Digite o comprimento da reta 2:'))
c = float(input('Digite o comprimento da reta 3:'))
if (abs(b - c) < a < (b + c)) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b):
    print(f'Há a existência de um triângulo')
else:
    print(f'Não há um triângulo')
