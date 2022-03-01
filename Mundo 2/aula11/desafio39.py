import datetime

anonascimento = int(input('Digite o seu ano de nascimento:'))
idade = datetime.date.today().year - anonascimento
if idade > 18:
    print(f'Você está com: {idade} anos e se passaram {idade-18} anos do seu alistamento')
elif idade == 18:
    print(f'Você está com: {idade} anos, aliste-se')
else:
    print(f'Você está com {idade} anos, e faltam {18-idade} anos para o seu alistamento')
