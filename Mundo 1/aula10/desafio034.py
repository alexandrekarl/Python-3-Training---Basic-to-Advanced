salario = float(input('Digite o seu salário:'))
if salario>1250:
    print(f'O seu salário ficará {(salario*1.1):.2f} com 10%')
else:
    print(f'O seu salário ficará {(salario*1.15):.2f} com 15%')