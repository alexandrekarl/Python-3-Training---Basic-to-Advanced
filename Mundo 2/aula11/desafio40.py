n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
media = (n1+n2)/2
if media > 7:
    print(f'A sua média ficou {media}, então você está aprovado!')
elif media < 5:
    print(f'A sua média ficou {media}, então você está reprovado!')
else:
    print(f'A sua média ficou {media}, então você está em recuperação!')
