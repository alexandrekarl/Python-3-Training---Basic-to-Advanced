import datetime

anonascimento = int(input('Digite o seu ano de nascimento:'))
idade = datetime.date.today().year - anonascimento
if idade <= 9:
    print(f'MIRIM')
elif (idade > 9) and (idade <= 14):
    print('INFANTIL')
elif (idade > 14) and (idade <= 19): #PODERIA TER ESCRITO APENAS <=19, pois ele vai condição por condição de cima para baixo!!!
    print('JUNIOR')
elif (idade > 19) and (idade <= 20):
    print('SENIOR')
else:
    print('MASTER')