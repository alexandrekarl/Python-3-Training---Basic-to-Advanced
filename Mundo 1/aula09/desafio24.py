nomecidade = input('Digite o nome de uma cidade:')
dividido = nomecidade.split() #dividir em várias strings o nome da cidade
primeironome = dividido[0] #primeiro nome da cidade
primeironomemin = primeironome.lower() #torná-la minúscula
print('A primeira palavra da cidade começa com santo?:','santo' in primeironomemin)
