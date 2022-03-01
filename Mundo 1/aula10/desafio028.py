import random

n1 = random.randrange(0, 5+1)
n2 = int(input('Digite um número de 0 a 5:'))
print(f'O computador pensou no número {n1} e você no número {n2}')
print(f'você pensou no número do computador' if n1 == n2 else 'você não pensou no número do computador')

