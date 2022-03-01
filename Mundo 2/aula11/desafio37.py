numero = int(input('Digite um número:'))
basedeconversao = str(input('Digite 1 para binário, 2 para octal e 3 para hexadecimal:'))
if basedeconversao == 1:
    print(f'Com a base de conversão binária, {numero} ficará: {bin(numero)}')
elif basedeconversao == 2:
    print(f'Com a base de conversão octal, {numero} ficará {oct(numero)}: ')
else:
    print(f'Com a base de conversão hexadecimal, {numero} ficará: {hex(numero)} ')