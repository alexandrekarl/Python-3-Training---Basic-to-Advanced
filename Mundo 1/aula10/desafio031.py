km = float(input('Digite a distância de sua viagem em km:'))
if km>200:
    print(f'Com {km}km rodados, o preço é de {km*0.45} reais')
else:
    print(f'Com {km}km rodados, o preço é de {km*0.50} reais')