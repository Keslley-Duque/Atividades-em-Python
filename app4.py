#a = int(input('Entre com um numero: '))
#div = 0
#for x in range(1, a + 1):
#    resto = a % x
#    print(x, resto)
#    if resto == 0:
#        div += 1
#if div == 2:
#    print('Numero {} é primo'.format(a))
#else:
#    print('Numero {} não é primo'.format(a))



#a = int(input('Entre com um numero: '))
#for num in range (a + 1):
#    div = 0
#    for x in range(1, num + 1):
#        resto = num % x
#        #print(x, resto)
#        if resto == 0:
#            div += 1
#    if div == 2:
#        print(num)

#nota = int(input('Entre com a nota: '))
#while nota > 10:
#    nota = int(input('Nota invalida! Entre com a nota corretamente: '))

#a = 0
#while a <= 10:
#    print(a)
#    a += 1    

a = int(input('Primeira nota: '))
while a > 10:
    a = int(input('Voce digitou errado! Primeira nota: '))
b = int(input('Segunda nota: '))
while b > 10:
    b = int(input('Voce digitou errado! Segunda nota: '))
c = int(input('Terceira nota: '))
while c > 10:
    c = int(input('Voce digitou errado! Terceiro nota: '))
d = int(input('Quarta nota: '))
while d > 10:
    d = int(input('Voce digitou errado! Quarta nota: '))

media = (a + b + c + d)/4
print('Media: {}'.format(media))    