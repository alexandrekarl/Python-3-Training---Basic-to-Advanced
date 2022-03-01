n1 = int(input('Digite o primeiro número inteiro:'))
n2 = int(input('Digite o segundo número inteiro:'))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}, ou seja, o primeiro valor informado é maior')
elif n2 > n1:
    print(f'O número {n2} é maior que {n1}, ou seja, o segundo valor informado é maior')
else:
    print(f'O número {n1} é igual ao número {n2}, ou seja, os dois são iguais')