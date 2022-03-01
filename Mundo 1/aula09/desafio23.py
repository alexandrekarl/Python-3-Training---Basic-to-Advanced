n1 = int(input('Digite um número de 0 a 9999:'))
n2 = str(n1)
if n1 > 9999:
    print('Número inválido, maior que 9999')
if n1 < 10:
    print(f'Tem a unidade: {n2[0]}')
if (n1 < 100) and (n1 >= 10):
    print(f'Tem a unidade: {n2[1]} e a dezena: {n2[0]}')
if (n1 > 100) and (n1<1000):
    print(f'Tem a unidade: {n2[2]} e a dezena: {n2[1]} e a centena: {n2[0]}')
if (n1 > 1000):
    print(f'Tem a unidade: {n2[3]} e a dezena: {n2[2]} e a centena: {n2[1]} e o milhar: {n2[0]}')



