valor = float(input('Digite o valor da casa:'))
salario = float(input('Digite o seu salário:'))
tempo = float(input('Digite em quantos anos você vai pagar:'))
prestacaoanual = (valor/tempo)
if prestacaoanual > (salario*0.3):
    print('Empréstimo negado!')
else:
    print('Empréstimo deferido!')