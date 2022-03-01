velocidade = int(input('Digite a velocidade do carro em km/h:'))
if velocidade>80:
    print(f'Você foi multado pois estava a {velocidade} km/h e a sua multa será de {(velocidade-80)*7}')
else:
    print(f'Parabéns, você estava a {velocidade}km/h e não houve multa')
