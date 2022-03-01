import calendar
ano = int(input('Digite um ano:'))
if calendar.isleap(ano):
    print('É bissexto!')
else:
    print('Não é bissexto!')

