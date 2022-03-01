nomecompleto = str(input('Digite o nome completo:'))
nomedividido = nomecompleto.split()
print(f'O primeiro nome é: {nomedividido[0]} e o último nome é: {nomedividido.pop()}')