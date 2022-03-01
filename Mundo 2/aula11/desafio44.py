print(f"{'LOJAS ALEXANDRE':=^40}")
valor = float(input('Digite o valor a ser pago:'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3]2x cartão
[4] 3x ou mais no cartão''')
pagamento = int(input('Digite a condição de pagamento: '))
if pagamento == 1:
    print(f'O total será de {valor*0.9}')
elif pagamento == 2:
    print(f'O total será de {valor*0.95}')
elif pagamento == 3:
    print(f'O total será de {valor}')
elif pagamento == 4:
    print(f'O total será de {valor*1.2}')
else:
    print('Opção errada')
