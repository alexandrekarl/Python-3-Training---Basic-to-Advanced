import math
catop = float(input('Digite o cateto oposto:'))
catadj = float(input('Digite o catadj:'))
#print(f'A hipotenusa de {catop} {catadj} é {((catop**2)+(catadj**2))**(1/2)}')
print(f'A hipotenusa de {catop} {catadj} é {math.hypot(catop , catadj)}')
