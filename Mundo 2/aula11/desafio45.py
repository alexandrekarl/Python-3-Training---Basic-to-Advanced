import random
import time

jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolhacomputador = (random.choice(jokenpo))
escolhausuario = input('Escolha entre: Pedra, Papel ou Tesoura:')
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
if (escolhausuario == 'Pedra') and (escolhacomputador == 'Tesoura'):
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto você ganhou!!')
elif (escolhausuario == 'Pedra') and (escolhacomputador == 'Papel'):
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto você perdeu!!')
elif (escolhausuario == 'Papel') and (escolhacomputador == 'Tesoura'):
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto você perdeu!!')
elif (escolhausuario == 'Papel') and (escolhacomputador == 'Pedra'):
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto você ganhou!!')
elif (escolhausuario == 'Tesoura') and (escolhacomputador == 'Pedra'):
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto você perdeu!!')
elif (escolhausuario == 'Tesoura') and (escolhacomputador == 'Papel'):
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto você ganhou!!')
elif escolhausuario == escolhacomputador:
    print(f'Você escolheu:{escolhausuario} e o computador escolheu:{escolhacomputador}, portanto deu empate!!')
else:
    print('Digite corretamente!')

#PODE SER FEITO COM IFs dentro de 3 IFs principais, que são as jogadas do usuário ou computador, pois são 3 as possíveis.





